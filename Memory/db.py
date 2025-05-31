# memory/db.py

import sqlite3
from pathlib import Path

DB_PATH = Path("memory.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            thread_id TEXT PRIMARY KEY,
            format TEXT,
            intent TEXT,
            raw_text TEXT
        )
        """)
