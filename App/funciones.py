import sqlite3

def crear_db():
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Crear las tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Colectivos (
        id_colectivo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo CHAR(1) NOT NULL CHECK(tipo IN ('U', 'I'))
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Horarios_col (
        id_horario_col INTEGER PRIMARY KEY AUTOINCREMENT,
        id_colectivo INTEGER NOT NULL,
        tipo_hor CHAR(1) NOT NULL CHECK(tipo_hor IN ('S', 'V')),
        dias INTEGER NOT NULL,
        estado CHAR(1) NOT NULL CHECK(estado IN ('h', 'i')),
        FOREIGN KEY (id_colectivo) REFERENCES Colectivos (id_colectivo)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS detalle_horarios (
        id_detalle_horario INTEGER PRIMARY KEY AUTOINCREMENT,
        id_horario_col INTEGER NOT NULL,
        hora_salida TIME NOT NULL,
        hora_llegada TIME NOT NULL,
        FOREIGN KEY (id_horario_col) REFERENCES Horarios_col (id_horario_col)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Carreras (
        id_carrera INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Materias (
        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        id_carrera INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        comision TEXT ,       
        estado CHAR(1) NOT NULL CHECK(estado IN ('h', 'i')),
        FOREIGN KEY (id_carrera) REFERENCES Carreras (id_carrera)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detalle_materias (
        id_detalle_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        id_materia INTEGER NOT NULL,
        tipo TEXT,
        dias INTEGER NOT NULL,
        aula TEXT,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        FOREIGN KEY (id_materia) REFERENCES Materias (id_materia)
    )
    ''')

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()



def Buscar_Colectivos(trayecto):

    conexion = sqlite3.connect("app.db")
    cursor = conexion.cursor()
    
    cursor.execute(f"""Select c.nombre as nombre, c.tipo as trayecto, h.tipo_hor as tipo_hor, h.dias as dias ,d.hora_salida as salida, d.hora_llegada as llegada, h.estado as estado 
    from Colectivos as c
    join Horarios_col as h on c.id_colectivo=h.id_colectivo
    join detalle_horarios as d on d.id_horario_col=h.id_horario_col
    where c.tipo ='{trayecto}' and h.estado = 'h'
    """)

    colectivos = cursor.fetchall()
    conexion.close()

    return colectivos



def leer_datos():
    # Abrir el archivo en modo lectura
    with open('datos.txt', 'r') as file:
        lines = file.readlines()
    
    datos_sql = []
    
    # Procesar cada bloque de 24 líneas
    for i in range(0, len(lines), 25):
        empresa = lines[i + 4].strip()  # La empresa está en la línea 5 (índice 4)
        hora_1 = lines[i + 7].strip()  # La primera hora está en la línea 8 (índice 7)
        hora_2 = lines[i + 11].strip()  # La segunda hora está en la línea 12 (índice 11)
        
        # Agregar los datos en formato SQL
        datos_sql.append((empresa, hora_1, hora_2))
    
    # Mostrar los datos listos para insertar en SQL
    for empresa, hora_1, hora_2 in datos_sql:
        num = 4
        if empresa== "Intercordoba":
            num = 5
        elif empresa == "Eder":
            num = 6
        hora2 = hora_2[:5] + ":00"
        hora1 = hora_1[:5] + ":00"
        print(f"INSERT INTO tabla detalle_horarios (id_horario_col, hora_salida, hora_llegada) VALUES ({num}, '{hora1}', '{hora2}');")



def guardar_carrera(nombre):
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    
    cursor.execute(f"Insert into Carreras(nombre) values ('{nombre}')")
    
    conn.commit()
    conn.close()


def guardar_materia(id,nombre,comision):
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

   
    cursor.execute(f"Insert into Materias(id_carrera,nombre,comision,estado) values ({id},'{nombre}','{comision}','h')")
    
    conn.commit()
    conn.close()


def guardar_detalle_mat(id_materia, tipo ,dias ,aula ,hora_inicio,hora_fin):
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

   
    cursor.execute(f"Insert into Detalle_materias (id_materia,tipo,dias,aula,hora_inicio,hora_fin) values ({id_materia}, '{tipo}' ,{dias} ,'{aula}' ,'{hora_inicio}','{hora_fin}')")
    
    conn.commit()
    conn.close()



def buscar_carreras():
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    
    cursor.execute(f"select * from carreras")
    
    carreras = cursor.fetchall()
    conn.close()

    return carreras

def buscar_materias():
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    
    cursor.execute(f"select id_materia , nombre from Materias")
    
    materias = cursor.fetchall()
    conn.close()

    return materias


def Buscar_materias_completo():

    conexion = sqlite3.connect("app.db")
    cursor = conexion.cursor()
    
    cursor.execute(f"""Select c.nombre as carrera, m.id_materia as id , m.nombre as materia, m.comision as comision, d.tipo as tipo, d.dias as dias, d.aula as aula, d.hora_inicio as inicio, d.hora_fin as fin
    from Detalle_materias as d
    join Materias as m on d.id_materia=m.id_materia
    join Carreras as c on m.id_carrera=c.id_carrera
    where  m.estado = 'h'
    """)

    materias = cursor.fetchall()
    conexion.close()

    return materias






if __name__ == "__main__":
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Crear las tablas
    cursor.execute(''' select * from carreras
    
        
    ''')
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    

"""delete from Detalle_materias where id_detalle_materia > 0
select * from detalle_materias
"""
