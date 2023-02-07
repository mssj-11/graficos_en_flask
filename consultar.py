#   Este ejemplo no es necesario para el ninguno de los proyectos del repositorio pero es otro ejemplo de realizar consultas.
import sqlite3

# Conectarse a la base de datos
con = sqlite3.connect("empleados.db")

# Crear un cursor
cur = con.cursor()

# Ejecutar una consulta
cur.execute("SELECT edad, count(*) FROM empleados GROUP BY edad")

# Obtener resultados
resultados = cur.fetchall()

# Imprimir resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión
con.close()