import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


class Config:
    DEBUG = os.getenv("DEBUG", default=False)
    BIND_HOST = os.getenv("BIND_HOST", default="127.0.0.1")
    BIND_PORT = os.getenv("BIND_PORT", default=5000)

    POSTGRES_USER = os.getenv("POSTGRES_USER", "root")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "root")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    NEO4J_HOST = os.getenv("NEO4J_HOST", default="localhost")
    NEO4J_PORT = os.getenv("NEO4J_PORT", default=7687)
    NEO4J_USER = os.getenv("NEO4J_USER", default="neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", default="root")
