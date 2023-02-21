import sqlite3
from pathlib import Path


def create_db_conn(db_name: str = 'go.sqlite') -> sqlite3.Connection:
    cwd = Path(__file__).parent
    db_path = cwd / db_name
    db_conn = sqlite3.connect(db_path)
    db_conn.row_factory = sqlite3.Row
    return db_conn
