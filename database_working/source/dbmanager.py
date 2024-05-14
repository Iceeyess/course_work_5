import psycopg2


class DBManager:

    def __init__(self, host: str, database: str, port: int, username: str, password: str) -> None:
        self.host = host
        self.database = database
        self.port = port
        self.username = username
        self.password = password

    def __enter__(self):
