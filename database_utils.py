import mysql.connector
import bcrypt


def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="olakase1",
            database="libreria",
            port=3306
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def verificar_usuario(username_or_email, password):
    conexion = conectar_db()
    if not conexion:
        return False, "No se pudo conectar a la base de datos"

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT USUARIO, CONTRASENA FROM usuarios WHERE USUARIO = %s OR CORREO = %s", 
                       (username_or_email, username_or_email))

        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()

        if resultado:
            usuario_db, contrasena_db = resultado
            if bcrypt.checkpw(password.encode('utf-8'), contrasena_db.encode('utf-8')):
                return True, usuario_db
            
        return False, "Usuario o contraseña incorrecta"
    except mysql.connector.Error as err:
        return False, f"Error al verificar usuario: {err}"   



def agregar_usuario(username, email, password):
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"

    try:
        cursor = conexion.cursor()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute(
            "INSERT INTO usuarios (USUARIO, CORREO, CONTRASENA, CONTRASENA_ORIGINAL) VALUES (%s, %s, %s,%s)",
            (username, email, hashed_pw, password)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, "Usuario registrado con éxito"

    except mysql.connector.errors.IntegrityError as e:
        if "1062" in str(e):
            return False, "El nombre de usuario o correo ya está registrado"
        return False, "Error desconocido: " + str(e)

    except mysql.connector.Error as err:
        return False, f"Error al registrar usuario: {err}"
    
def buscar_libro_autor(name, author):
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"
    try:
        cursor = conexion.cursor()
        if name and author:           
            cursor.execute("SELECT * FROM libros WHERE NOMBRE = %s AND AUTOR = %s", (name, author))
        elif name:            
            cursor.execute("SELECT * FROM libros WHERE NOMBRE = %s", (name,))
        elif author:           
            cursor.execute("SELECT * FROM libros WHERE AUTOR = %s", (author,))
        else:
            return False, "Debes proporcionar al menos un criterio de búsqueda"        
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()        
        return  resultado
    except mysql.connector.Error as err:
        return False, f"Error al buscar libro: {err}"


def agregar_libro(name, author, publication, genre, synopsis, portada):
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO libros (NOMBRE, AUTOR, PUBLICACION, GENERO, SINOPSIS, PORTADA) VALUES (%s,%s,%s,%s,%s,%s)",
            (name, author, publication, genre, synopsis, portada)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, "Libro agregado con éxito"
    except mysql.connector.Error as err:
        return False, f"Error al agregar libro: {err}"

     

def eliminar_libro(name):
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE NOMBRE = %s", (name,))
        
        # Verifica si se ha eliminado al menos un registro
        if cursor.rowcount == 0:
            return False, f"No se encontró un libro con el nombre '{name}'"
        
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, "Libro eliminado con éxito"
    except mysql.connector.Error as err:
        return False, f"Error al eliminar libro: {err}"

def consultar_inventario():
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT NOMBRE, AUTOR FROM libros ORDER BY NOMBRE ASC")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado
    except mysql.connector.Error as err:
        return False, f"Error al consultar inventario: {err}"

def consultar_info_libro(nombre):
    conexion = conectar_db()
    if not conexion:
        return False, "Error al conectar con la base de datos"
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros WHERE NOMBRE = %s", (nombre,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado
    except mysql.connector.Error as err:
        return False, f"Error al consultar información del libro: {err}"



