import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table for storing scan results."""
    try:
        sql_create_results_table = """CREATE TABLE IF NOT EXISTS results (
                                        id integer PRIMARY KEY,
                                        device text NOT NULL,
                                        ip text NOT NULL
                                    );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_results_table)
    except sqlite3.Error as e:
        print(e)

def insert_result(conn, device, ip):
    """Insert a new scan result into the results table."""
    sql = '''INSERT INTO results(device, ip) VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (device, ip))
    conn.commit()
    return cur.lastrowid