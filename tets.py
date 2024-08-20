import sqlite3

def verify_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Listar todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Tables:")
    for table in tables:
        print(f"Table: {table[0]}")
    
    conn.close()

verify_tables('/home/markbusking/projectos/VINIPEDIA/DB/wines.db')
