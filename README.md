# airflow-dbt-snowflake

## Step 1: Create two Python virtual environments (from project root)
A) Airflow environment
```python3 -m venv venv_airflow
source venv_airflow/bin/activate
python -m pip install --upgrade pip```

B) dbt environment
In a new terminal (or deactivate first), from project root:
```python3 -m venv venv_dbt
source venv_dbt/bin/activate
python -m pip install --upgrade pip```