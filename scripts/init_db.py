import psycopg
from psycopg import sql

from shared.config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_ADMIN_USER,
    POSTGRES_ADMIN_PASSWORD,
    POSTGRES_APP_USER,
    POSTGRES_APP_PASSWORD,
    POSTGRES_DB,
)


def create_database():
    if not POSTGRES_ADMIN_PASSWORD or not POSTGRES_APP_PASSWORD:
        raise RuntimeError(
            "POSTGRES_ADMIN_PASSWORD and POSTGRES_APP_PASSWORD must be set in .env"
        )

    connection = psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_ADMIN_USER,
        password=POSTGRES_ADMIN_PASSWORD,
        dbname="postgres",
        autocommit=True,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT 1 FROM pg_roles WHERE rolname = %s",
                (POSTGRES_APP_USER,),
            )

            user_exists = cursor.fetchone()

            if not user_exists:
                cursor.execute(
                    sql.SQL("CREATE ROLE {} LOGIN PASSWORD {}").format(
                        sql.Identifier(POSTGRES_APP_USER),
                        sql.Literal(POSTGRES_APP_PASSWORD),
                    )
                )
                print(f"Created PostgreSQL user: {POSTGRES_APP_USER}")
            else:
                print(f"PostgreSQL user already exists: {POSTGRES_APP_USER}")

            cursor.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (POSTGRES_DB,),
            )

            database_exists = cursor.fetchone()

            if not database_exists:
                cursor.execute(
                    sql.SQL("CREATE DATABASE {} OWNER {}").format(
                        sql.Identifier(POSTGRES_DB),
                        sql.Identifier(POSTGRES_APP_USER),
                    )
                )
                print(f"Created PostgreSQL database: {POSTGRES_DB}")
            else:
                print(f"PostgreSQL database already exists: {POSTGRES_DB}")

    finally:
        connection.close()


def verify_database():
    connection = psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_APP_USER,
        password=POSTGRES_APP_PASSWORD,
        dbname=POSTGRES_DB,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user")
            database_name, username = cursor.fetchone()

            print(f"Connected database: {database_name}")
            print(f"Connected user: {username}")
            print("PostgreSQL setup successful")

    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
    verify_database()