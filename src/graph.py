from py2neo import Graph
from src.config import Config
from src.utils import retry


@retry(10, exceptions=(Exception))
def connect():
    return Graph(
        host=Config.NEO4J_HOST,
        port=Config.NEO4J_PORT,
        user=Config.NEO4J_USER,
        password=Config.NEO4J_PASSWORD,
    )


graph = connect()