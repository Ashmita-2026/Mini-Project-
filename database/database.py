import sqlite3

DB_PATH = "system_health.db"


def initialize_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM system_info")

    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO system_info (key, value) VALUES (?, ?)",
            [
                ("app_name", "System Health Dashboard"),
                ("version", "1.0.0"),
                ("owner", "SRE Project")
            ]
        )

    connection.commit()
    connection.close()


def get_system_info():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT key, value FROM system_info")
    rows = cursor.fetchall()

    connection.close()

    return {key: value for key, value in rows}


def check_database():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        connection.close()
        return "UP"
    except sqlite3.Error:
        return "DOWN"