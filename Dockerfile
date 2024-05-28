FROM apache/airflow:2.9.0

# Install PostgreSQL development libraries
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY dags /opt/airflow/dags
COPY scripts /opt/airflow/scripts

# Uncomment the following line if you have a custom airflow.cfg
# COPY airflow.cfg /opt/airflow/airflow.cfg
