# memory/shared_memory.py

from uuid import uuid4
from Memory.db import get_connection, init_db

init_db()

def generate_thread_id() -> str:
    return str(uuid4())

def save(thread_id: str, data: dict):
    with get_connection() as conn:
        conn.execute(
            "REPLACE INTO memory (thread_id, format, intent, raw_text) VALUES (?, ?, ?, ?)",
            (thread_id, data.get("format"), data.get("intent"), data.get("raw_text"))
        )

def load(thread_id: str) -> dict:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM memory WHERE thread_id = ?", (thread_id,)).fetchone()
        return dict(row) if row else None

def list_all() -> dict:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM memory").fetchall()
        return {row["thread_id"]: dict(row) for row in rows}
