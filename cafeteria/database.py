import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import sqlite3

# Establece la conexión:
try:
    conexion = sqlite3.Connection("Restaurante")
    cur = conexion.cursor()
    print("Conexión realizada con éxito")
except sqlite3.OperationalError as e:
    print(e)

def cargarCamarero(camareros):
    try:
        cur.execute("SELECT * FROM CAMAREROS ORDER BY(idCamarero)")
        listado = cur.fetchall()
        camareros.clear()
        for n in listado:
            camareros.append(n)
        conexion.commit()
        print("Carga de camareros realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarProducto(productos):
    try:
        cur.execute("SELECT * FROM SERVICIOS ORDER BY(idServicio)")
        listado = cur.fetchall()
        productos.clear()
        for n in listado:
            productos.append(n)
        conexion.commit()
        print("Carga de productos realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()


# Camareros:
def altaCamarero(fila, camareros):
    try:
        cur.execute('insert into camareros (nombre, password) values(?,?)', fila)
        conexion.commit()
        print("Alta de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

def modificaCamarero(fila, id, camareros):
    try:
        cur.execute(
            "update camareros set nombre = '" + str(fila[0]) + "', password = '" + str(fila[1]) + "' where idcamarero = " + id + "")
        conexion.commit()
        print("Modificación de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

def bajaCamarero(id, camareros):
    try:
        cur.execute("delete from camareros where idcamarero = "+id+"")
        conexion.commit()
        print("Baja de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

# Productos:
def altaProducto(fila, productos):
    try:
        cur.execute('insert into servicios (servicio, precio) values(?,?)', fila)
        conexion.commit()
        print("Alta de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def modificaProducto(fila, id, productos):
    try:
        cur.execute("update servicios set servicio = '" + str(fila[0]) + "', precio = '"+ str(fila[1])+"' where idservicio = '"+id+"'")
        conexion.commit()
        print("Modificación de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def bajaProducto(id, productos):
    try:
        cur.execute("delete from servicios where idservicio = "+id+"")
        conexion.commit()
        print("Baja de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

# Recursos:
def buscaPWD(id):
    try:
        cur.execute("select password from camareros where idcamarero = " + id + "")
        password = str(cur.fetchone())
        for char in "(),'":
            password = password.replace(char, '')
        conexion.commit()
    except sqlite3.Error as e:
        print(e)
    return password

def login(user, pwd):
    try:
        cur.execute("select idCamarero from camareros where idCamarero = '"+user+"'")
        user = str(cur.fetchone())
        for char in "(),'":
            user = user.replace(char, '')
        cur.execute("select password from camareros where password = '"+pwd+"'")
        password = str(cur.fetchone())
        for char in "(),'":
            password = password.replace(char, '')
        fila = (user, password)
        conexion.commit()
    except sqlite3.Error as e:
        print(e)
    return fila

def cargaComunidad():
    i = 0
    cur.execute("select comunidad from comunidades")
    list = Gtk.ListStore(str)
    all_rows = cur.fetchall()
    list.clear()
    for row in all_rows:
        i = i + 1
        list.append([row[0]])
    return list

def cargaProvincias(comunidad):
    i = 0
    cur.execute(
        "select provincia from provincias where comunidad_id in (Select id from comunidades where comunidad='" + comunidad + "')")
    list = Gtk.ListStore(str)
    all_rows = cur.fetchall()
    for row in all_rows:
        i = i + 1
        list.append([row[0]])
    return list

def cargaMunicipios(provincia):
    i = 0
    cur.execute(
            "select municipio from municipios where provincia_id in (Select id from provincias where provincia='" + provincia + "')")
    row = cur.fetchone()
    list = Gtk.ListStore(str)
    all_rows = cur.fetchall()
    for row in all_rows:
        i = i + 1
        list.append([row[0]])
    return list


