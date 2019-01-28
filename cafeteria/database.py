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

 # Cargar tablas:
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

def cargarFactura(facturas, mesa):
    try:
        if mesa == 0:
            cur.execute("SELECT * FROM FACTURAS ORDER BY(idFactura)")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
        else:
            cur.execute("SELECT * FROM FACTURAS WHERE IDMESA = '"+str(mesa)+"' ORDER BY(idFactura)")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
        conexion.commit()
        print("Carga de facturas realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarComanda(comandas):
    try:
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = cur.fetchone()
        #CONTINUAR
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()



# Gestion de camareros:
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

# Gestion de productos:
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

 # Gestion líneas de venta:
def altaLinea(fila, comandas, servicio):
    try:
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = cur.fetchone()
        for char in "(),'":
            factura = factura.replace(char, '')
        cur.execute("SELECT CANTIDAD FROM LINEAFACTURAS WHERE IDSERVICIO = '"+servicio+"' AND IDFACTURA = '"+factura+"'")
        cantidad = cur.fetchone()
        for char in "(),'":
            cantidad = cantidad.replace(char, '')
        if cantidad != "None":
            cantidad = int(cantidad + 1)
            cur.execute("SELECT IDVENTA FROM LINEAFACTURAS WHERE IDSERVICIO = '" + servicio + "' AND IDFACTURA = '" + factura + "'")
            id = cur.fetchone()
            cur.execute("update lineafacturas set cantidad = '" + cantidad + " where idventa = '" + id + "'")
        else:
            cantidad = 1;
            fila = fila + cantidad;
            cur.execute('insert into lineafacturas (idfactura, idservicio, cantidad) values(?,?,?)', fila)
        conexion.commit()
        print("Inserción de línea de venta realizada con éxito")
        #cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def altaFactura(fila, facturas):
    try:
        cur.execute('insert into facturas (dnicliente, idcamarero, idmesa, fecha) values(?,?,?,?)', fila)
        conexion.commit()
        print("Alta de factura realizada con éxito")
    except sqlite3.Error as e:
        print(e)

 # Gestion de clientes:
def altaCliente(fila):
    try:
        cur.execute("insert into clientes (dni, apellidos, nombre, comunidad, provincia, ciudad) values (?, ?, ?, ?, ?, ?)", fila)
        conexion.commit()
        print("Alta de cliente realizada con éxito")
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

def cargaMesas():
    try:
        cur.execute("SELECT ESTADO FROM MESAS ORDER BY(idMesa)")
        listado = cur.fetchall()
        conexion.commit()
        print("Carga de productos realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()
    return listado


