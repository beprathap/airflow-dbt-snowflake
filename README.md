# airflow-dbt-snowflake

## Step 1: Create two Python virtual environments (from project root)
### A) Airflow environment
```bash
# 1) Install Python 3.11
brew install python@3.11

# 2) Recreate the airflow venv with Python 3.11
/opt/homebrew/bin/python3.11 -m venv venv_airflow

# 3) Activate and upgrade pip
source airflow_venv/bin/activate
python -m pip install --upgrade pip
```

### B) dbt environment
In a new terminal (or deactivate first), from project root:
```bash
python3 -m venv venv_dbt
source venv_dbt/bin/activate
python -m pip install --upgrade pip
```

### C) Install Python
Mac:
```bash
brew install python@3.11
```

### D) Install postgresql for Airflow - Local Executor
Mac: 
```bash
brew install postgresql@16
brew services start postgresql@16
```
Other commands:
```bash
brew services restart postgresql@16
brew services stop postgresql@16
brew services list | grep postgresql
```

## How to connect every time (because you’re on port 5433):
Quick connect (local socket):
```bash
psql -p 5433 postgres
```
More explicit (TCP):
```bash
psql -h localhost -p 5433 postgres
```

## If you want to avoid remembering the port, add an alias in your shell config (~/.zshrc):
```bash
alias psqlpg='psql -h localhost -p 5433'
```

# If you’re inside psql and see prompts like:

postgres=# (ready)

postgres-# (it thinks your SQL command isn’t finished)

Exit psql
```bash
\q
```

Then run:
```bash
lsof -nP -iTCP:5433 -sTCP:LISTEN
```

Then:

psqlpg postgres
This installs:
postgres server
psql CLI
background service listening on port 5432

It includes the server and related command-line tools, making a separate postgresql-contrib package generally unnecessary as extensions are often managed differently on macOS or included by default.

Ensure your shell uses PostgreSQL 16 binaries (PATH):
echo 'export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
hash -r

Verify:
which psql
psql --version
which pg_ctl
pg_ctl --version


Postgres is running fine locally, but it’s configured to listen on port 5433 instead of the default 5432, so clients must explicitly connect using that port.



1️⃣ Connect to Postgres explicitly (one command)
psql -h localhost -p 5433 postgres


If this works, you’re done with Postgres setup.

2️⃣ Create Airflow DB + user (only after connection works)

Inside psql:

CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow OWNER airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
\q


Step 5️⃣ Verify connection as Airflow user (recommended)

From terminal:

psql -h localhost -p 5433 -U airflow airflow


You should see:

airflow=#


If this works, Postgres is 100% correct.


Airflow steps:

> delete and clear the local airflow setup first
in the project root directory

python3.11 -m venv airflow_venv
source airflow_venv/bin/activate
pip install --upgrade pip

export AIRFLOW_VERSION=3.1.5
export PYTHON_VERSION=3.11

Install Airflow:
pip install "apache-airflow[postgres]==${AIRFLOW_VERSION}" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install psycopg2-binary

then export env vars:
export AIRFLOW_HOME="$(pwd)/airflow_home"
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql+psycopg2://airflow:airflow@localhost:5433/airflow"
export AIRFLOW__CORE__EXECUTOR="LocalExecutor"


check airflow installation:

which airflow

I changed airflow webui password going manually to the simple_auth_manager_passwords.json.generated file



Run Airflow

pip install pandas
pip install snowflake-connector-python
pip install boto3


Now its time for dbt

>
python3.11 -m venv dbt_venv
source dbt_venv/bin/activate
pip install --upgrade pip
pip install dbt-snowflake
