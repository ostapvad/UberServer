# 1) To run tests or run database.py use localhost
# 2) Otherwise run in containers (default)

LOCAL_HOST = False

POSTGRES_DB_URL = "postgresql://user:pass@postgres-db:5432/demo"
MAIN_DB_URL = "http://uberserver-database-1:3100/v1/coords"


if LOCAL_HOST:
    POSTGRES_DB_URL = "postgresql://user:pass@localhost:5432/demo"
    MAIN_DB_URL = "http://localhost:8088/v1/coords"





