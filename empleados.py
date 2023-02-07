import sqlite3

con = sqlite3.connect("empleados.db")
cur = con.cursor()

# Crear la tabla empleados
cur.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
""")

# Agregar algunos registros a la tabla empleados
registros = [
    ("Juan", 25),
    ("María", 29),
    ("Pedro", 31),
    ("Lucía", 33),
    ("David", 40)
]

cur.executemany("""
INSERT INTO empleados (nombre, edad)
VALUES (?, ?)
""", registros)

con.commit()
conn.close()