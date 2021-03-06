#!/usr/local/bin/python
# coding: utf-8

import locale
import os
import random

import gi
from reportlab.lib.pagesizes import A4, A6
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import sqlite3
from reportlab.lib.colors import forestgreen, darkgreen, black, cornsilk
from reportlab.pdfbase.ttfonts import TTFont

# Establece la conexión:
try:
    conexion = sqlite3.Connection("Restaurante")
    cur = conexion.cursor()
    print("Conexión realizada con éxito")
except sqlite3.OperationalError as e:
    print(e)

# MÉTODOS PARA CARGAR/ACTUALIZAR LOS TREEVIEW:
def cargarCamarero(camareros):
    '''Carga de camareros
        Realiza la consulta necesaria contra la base de datos para obtener el listado con todos los datos
        de los camareros y lo carga en la lista asociada al treeView'''
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

def cargarCliente(clientes):
    '''Carga de clientes
        Realiza la consulta necesaria contra la base de datos para obtener el listado con todos los datos
        de los clientes y lo carga en la lista asociada al treeView'''
    try:
        cur.execute("SELECT DNI, NOMBRE, APELLIDOS, COMUNIDAD, PROVINCIA, CIUDAD FROM CLIENTES")
        listado = cur.fetchall()
        clientes.clear()
        for n in listado:
            clientes.append(n)
        conexion.commit()
        print("Carga de clientes realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarProducto(productos):
    '''Carga de productos
        Realiza la consulta necesaria contra la base de datos para obtener el listado con todos los datos
        de los productos y lo carga en la lista asociada al treeView'''
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
    '''Carga de factura por mesa
        Comprueba el número de la mesa seleccionada y realiza la consulta necesaria contra la base de datos
        para obtener el listado con todos los datos de las facturas y lo carga en la lista asociada al treeView'''
    try:
        if mesa == 0: #Si no hay mesa seleccionada
            cur.execute("SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura), Facturas.PAGADO "
                        "FROM Facturas left join LineaFacturas "
                        "on LineaFacturas.IdFactura = Facturas.IdFactura "
                        "GROUP BY Facturas.IdFactura;")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
        else: #Si se le envía el número de una mesa
            cur.execute(
                "SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura), Facturas.PAGADO "
                "FROM Facturas left join LineaFacturas "
                "on LineaFacturas.IdFactura = Facturas.IdFactura "
                "WHERE Facturas.IDMESA = '"+str(mesa)+"'"
                "GROUP BY Facturas.IdFactura;")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
        conexion.commit()
        print("Carga de facturas realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarFactura2(facturas, dni):
    '''Carga de facturas por dni
        Realiza la consulta necesaria contra la base de datos para obtener el listado con todos los datos
        de las facturas que lleven el dni introducido y lo carga en la lista asociada al treeView'''
    try:
        encontrado = False
        cur.execute("SELECT DNI FROM CLIENTES WHERE DNI = '"+str(dni)+"'")
        cliente = str(cur.fetchone())
        for char in "(),'":
            cliente = cliente.replace(char, '')
        if cliente != "None":
            encontrado = True
        else:
            encontrado = False

        if encontrado == True: #Si hay alguna coincidencia pone la booleana a true y realiza la carga
            cur.execute(
                "SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura), Facturas.PAGADO "
                "FROM Facturas left join LineaFacturas "
                "on LineaFacturas.IdFactura = Facturas.IdFactura "
                "WHERE Facturas.DNICLIENTE = '" + cliente + "'"
                                                          "GROUP BY Facturas.IdFactura;")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
            print("Carga de facturas realizada con éxito")
        conexion.commit()
        return encontrado #Devuelve la booleana con el estado
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarComanda(factura, comandas):
    '''Carga de comandas
        Realiza la consulta necesaria contra la base de datos para obtener el listado con todos los datos
        de las comandas asociadas a la factura seleccionada y lo carga en la lista asociada al treeView'''
    try:
        cur.execute("SELECT IDSERVICIO, CANTIDAD FROM LINEAFACTURAS WHERE IDFACTURA = '"+factura+"'")
        listado = cur.fetchall()
        comandas.clear()
        for n in listado:
            comandas.append(n)
        conexion.commit()
        print("Carga de comandas de la factura "+factura+" realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

# MÉTODOS RELACIONADOS CON LA GESTIÓN DE CAMAREROS:
def altaCamarero(fila, camareros):
    '''Insercción de camareros
        Realiza la sentencia necesaria para insertar camareros en la base de datos'''
    try:
        cur.execute('insert into camareros (nombre, password) values(?,?)', fila)
        conexion.commit()
        print("Alta de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

def modificaCamarero(fila, id, camareros):
    '''Modificación de camareros
        Realiza la sentencia necesaria para modificar camareros en la base de datos'''
    try:
        cur.execute(
            "update camareros set nombre = '" + str(fila[0]) + "', password = '" + str(fila[1]) + "' where idcamarero = " + id + "")
        conexion.commit()
        print("Modificación de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

def bajaCamarero(id, camareros):
    '''Baja de camareros
        Realiza la sentencia necesaria para eliminar camareros en la base de datos'''
    try:
        cur.execute("delete from camareros where idcamarero = "+id+"")
        conexion.commit()
        print("Baja de camarero realizada con éxito")
        cargarCamarero(camareros)
    except sqlite3.Error as e:
        print(e)

# MÉTODOS RELACIONADOS CON LA GESTIÓN DE PRODUCTOS:
def altaProducto(fila, productos):
    '''Insercción de productos
        Realiza la sentencia necesaria para insertar productos en la base de datos'''
    try:
        cur.execute('insert into servicios (servicio, precio, categoria) values(?,?,?)', fila)
        conexion.commit()
        print("Alta de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def modificaProducto(fila, id, productos):
    '''MOdificación de productos
        Realiza la sentencia necesaria para modificar productos en la base de datos'''
    try:
        cur.execute("update servicios set servicio = '" + str(fila[0]) + "', precio = '"+ str(fila[1])+"', categoria = '"+str(fila[2])+"' where idservicio = '"+id+"'")
        conexion.commit()
        print("Modificación de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def bajaProducto(id, productos):
    '''Baja de productos
        Realiza la sentencia necesaria para eliminar productos en la base de datos'''
    try:
        cur.execute("delete from servicios where idservicio = "+id+"")
        conexion.commit()
        print("Baja de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

 # MÉTODOS RELACIONADOS CON LA GESTIÓN DE FACTURAS + LINEAS FACTURAS
def altaLinea(factura, comandas, servicio):
    '''Insercción de lineas de venta
        Hace una consulta para obtener la cantidad del producto registrado en la factura indicada,
        si la cantidad es 0, se añade el primer producto,
        si la cantidad es superior a 0, se modifica el producto para aumentar la cantidad'''
    try:
        #Obtenemos la cantidad del producto registrado con el id que le envíamos desde el main
        cur.execute("SELECT CANTIDAD FROM LINEAFACTURAS WHERE IDSERVICIO = '"+servicio+"' AND IDFACTURA = '"+factura+"'")
        cantidad = str(cur.fetchone())
        for char in "(),'":
            cantidad = cantidad.replace(char, '')

        if cantidad != "None": #En caso de no ser null, sumamos uno a la cantidad y actualizamos la línea sacando antes su id mediante consulta
            cantidad = int(cantidad)
            cantidad = int(cantidad + 1)
            cur.execute("SELECT IDVENTA FROM LINEAFACTURAS WHERE IDSERVICIO = '" + servicio + "' AND IDFACTURA = '" + factura + "'")
            id = str(cur.fetchone())
            for char in "(),'":
                id = id.replace(char, '')
            cur.execute("update lineafacturas set cantidad = " + str(cantidad) + " where idventa = " + id + "")
        else: #En caso contrario, insertamos la linea con cantidad a 1
            cantidad = 1;
            fila = (factura, servicio, cantidad)
            cur.execute('insert into lineafacturas (idfactura, idservicio, cantidad) values(?,?,?)', fila)
        conexion.commit()
        print("Inserción de línea de venta en la factura "+factura+" realizada con éxito")
        cargarComanda(factura, comandas)
    except sqlite3.Error as e:
        print(e)

def bajaLinea(factura, comandas, servicio):
    '''Insercción de lineas de venta
        Hace una consulta para obtener la cantidad del producto registrado en la factura indicada,
        si la cantidad es 0, se elimina el producto,
        si la cantidad es superior a 0, se modifica el producto para reducir la cantidad'''
    try:
        cur.execute("SELECT IDVENTA FROM LINEAFACTURAS WHERE IDSERVICIO = '" + servicio + "' AND IDFACTURA = '" + factura + "'")
        id = str(cur.fetchone())
        for char in "(),'":
            id = id.replace(char, '')

        # Obtenemos la cantidad del producto registrado con el id que le envíamos desde el main
        cur.execute("SELECT CANTIDAD FROM LINEAFACTURAS WHERE IDVENTA = '"+id+"'")
        cantidad = str(cur.fetchone())
        for char in "(),'":
            cantidad = cantidad.replace(char, '')
        if cantidad != "None":
            cantidad = int(cantidad)
            if cantidad == 1:
                cur.execute("delete from lineafacturas where idventa = " + id + "")
            else:
                cantidad = cantidad - 1
                cur.execute("update lineafacturas set cantidad = " + str(cantidad) + " where idventa = " + id + "")
            print("Baja de línea de venta realizada con éxito")
        conexion.commit()
        cargarComanda(factura, comandas)
    except sqlite3.Error as e:
        print(e)

def validaCliente(self, widget, fila, clientes, dni):
    '''Valida clientes
        Busca si ya hay un cliente registrado en la base de datos con el dni introducido por el usuario '''
    try:
        encontrado = False
        cur.execute("SELECT DNI FROM CLIENTES WHERE DNI = '" + str(dni) + "'")
        cliente = str(cur.fetchone())
        for char in "(),'":
            cliente = cliente.replace(char, '')
        if cliente != "None":
            encontrado = True
        else:
            encontrado = False

        if encontrado == True:
            self.lblError.set_text("El DNI introducido ya pertenece a un cliente")
            self.abrirError(widget)
        else:
            altaCliente(fila, clientes)
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def altaCliente(fila, clientes):
    '''Alta de clientes
        Realiza la sentencia necesaria para insertar clientes en la base de datos'''
    try:
        cur.execute("insert into clientes (dni, apellidos, nombre, comunidad, provincia, ciudad) values (?, ?, ?, ?, ?, ?)", fila)
        conexion.commit()
        print("Alta de cliente realizada con éxito")
        cargarCliente(clientes)
    except sqlite3.Error as e:
        print(e)

def bajaCliente(dni, clientes):
    '''Baja de clientes
        Realiza la sentencia necesaria para eliminar clientes de la base de datos'''
    try:
        cur.execute("delete from clientes where dni = '"+dni+"'")
        print("Baja de cliente realizada con éxito")
        conexion.commit()
        cargarCliente(clientes)
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def altaFactura(fila):
    '''Alta de facturas
        Realiza la sentencia necesaria para insertar facturas en la base de datos'''
    try:
        cur.execute('insert into facturas (dnicliente, idcamarero, idmesa, fecha, pagado) values(?,?,?,?,?)', fila)
        conexion.commit()
        print("Alta de factura realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def bajaFactura(idFactura, facturas):
    '''Baja de facturas
        Comprueba si la factura seleccionada tiene asociadas lineas de venta,
        en caso afirmativo envía un mensaje de error,
        en caso negativo borra la factura de la base de datos'''
    try:
        vacio = False
        cur.execute("SELECT * FROM LINEAFACTURAS WHERE IDFACTURA = '"+str(idFactura)+"'")
        listado = cur.fetchall()
        print("La factura "+idFactura+" tiene "+str(len(listado))+" líneas de venta")
        if len(listado) == 0:
            cur.execute("delete from facturas where idFactura = " + str(idFactura) + "")
            cargarFactura(facturas, 0)
            vacio = True
        else:
            print("No se puede borrar la factura "+idFactura+" porque ya tiene pedidos asociados")
            vacio = False
        return vacio
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cobraFactura(idFactura, facturas):
    '''Cobros de facturas
        Actualiza el estado de la factura a pagado'''
    try:
        cur.execute("update facturas set pagado = 'SI' where idfactura = '"+str(idFactura)+"'")
        cargarFactura(facturas, 0)
        conexion.commit()
        print("La factura "+str(idFactura)+" ha sido pagada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def buscaFactura(idmesa):
    '''Buscar factura
        Coge la última factura registrada en la base de datos mediante la obtención del ID máximo'''
    try:
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS WHERE IDMESA = '"+str(idmesa)+"'")
        factura = str(cur.fetchone())
        for char in "(),'":
            factura = factura.replace(char, '')
        conexion.commit()
        return factura
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

 # MÉTODOS AUXILIARES:
def cargaComunidad():
    '''Cargar comunidades
        Obtiene todos los datos referentes a las comunidades de la base de datos y
        los añade a la lista asociada al treeview'''
    i = 0
    cur.execute("select comunidad from comunidades")
    list = Gtk.ListStore(str)
    all_rows = cur.fetchall()
    list.clear()
    for row in all_rows:
        i = i + 1
        list.append([row[0]])
    conexion.commit()
    return list

def cargaProvincias(comunidad):
    '''Cargar provincias
        Obtiene todos los datos referentes a las provincias de la base de datos y
        los añade a la lista asociada al treeview'''
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
    '''Cargar municipios
        Obtiene todos los datos referentes a los municipios de la base de datos y
        los añade a la lista asociada al treeview'''
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
    '''Cargar mesas
        Obtiene el estado de todas las mesas registradas en la base de datos y devuelve este listado'''
    try:
        cur.execute("SELECT ESTADO FROM MESAS ORDER BY(idMesa)")
        listado = cur.fetchall()
        conexion.commit()
        print("Carga de productos realizada con éxito")
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()
    return listado

def ocuparMesa(estado, mesa):
    '''Ocupar mesa
        Cambia el estado de la mesa a disponible o no disponible, según el string que haya recibido'''
    try:
        cur.execute("update mesas set estado = '"+estado+"' where idmesa = '"+str(mesa)+"'")
        conexion.commit()
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def buscaPWD(id):
    '''Buscas password
        Busca la contraseña asociada a el id recibido'''
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
    '''Obtencion de datos de inicio de sesion
        Obtiene el usuario y contraseña del usuario introducido'''
    try:
        cur.execute("select idCamarero from camareros where idCamarero = '"+user+"'")
        user = str(cur.fetchone())
        for char in "(),'":
            user = user.replace(char, '')
        cur.execute("select password from camareros where password = '"+pwd+"' and idCamarero = '"+user+"'")
        password = str(cur.fetchone())
        for char in "(),'":
            password = password.replace(char, '')
        fila = (user, password)
        conexion.commit()
        return fila
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()



