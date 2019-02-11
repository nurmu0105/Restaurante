import locale
import os
import random

import gi
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

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

# MÉTODOS PARA CARGAR/ACTUALIZAR LOS TREEVIEW:
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
            cur.execute("SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura) "
                        "FROM Facturas left join LineaFacturas "
                        "on LineaFacturas.IdFactura = Facturas.IdFactura "
                        "GROUP BY Facturas.IdFactura;")
            listado = cur.fetchall()
            facturas.clear()
            for n in listado:
                facturas.append(n)
        else:
            cur.execute(
                "SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura) "
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

def cargarComanda(comandas):
    try:
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = str(cur.fetchone())
        for char in "(),'":
            factura = factura.replace(char, '')
        cur.execute("SELECT IDSERVICIO, CANTIDAD FROM LINEAFACTURAS WHERE IDFACTURA = '"+factura+"'")
        listado = cur.fetchall()
        comandas.clear()
        for n in listado:
            comandas.append(n)
        conexion.commit()
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def limpiarComandas(comandas):
    try:
        comandas.clear()
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

# MÉTODOS RELACIONADOS CON LA GESTIÓN DE CAMAREROS:
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

# MÉTODOS RELACIONADOS CON LA GESTIÓN DE PRODUCTOS:
def altaProducto(fila, productos):
    try:
        cur.execute('insert into servicios (servicio, precio, categoria) values(?,?,?)', fila)
        conexion.commit()
        print("Alta de producto realizada con éxito")
        cargarProducto(productos)
    except sqlite3.Error as e:
        print(e)

def modificaProducto(fila, id, productos):
    try:
        cur.execute("update servicios set servicio = '" + str(fila[0]) + "', precio = '"+ str(fila[1])+"', categoria = '"+str(fila[2])+"' where idservicio = '"+id+"'")
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

 # MÉTODOS RELACIONADOS CON LA GESTIÓN DE FACTURAS + LINEAS FACTURAS
def altaLinea(comandas, servicio):
    try:
        #Obtenemos el id de la última factura registrada
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = str(cur.fetchone())
        for char in "(),'":
            factura = factura.replace(char, '')
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
        print("Inserción de línea de venta realizada con éxito")
        cargarComanda(comandas)
    except sqlite3.Error as e:
        print(e)

def bajaLinea(comandas, servicio):
    try:
        #Obtenemos el id de la última factura registrada y el id de la linea de venta asociada a ese servicio y factura
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = str(cur.fetchone())
        for char in "(),'":
            factura = factura.replace(char, '')

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
        cargarComanda(comandas)
    except sqlite3.Error as e:
        print(e)

def altaCliente(fila):
    try:
        cur.execute("insert into clientes (dni, apellidos, nombre, comunidad, provincia, ciudad) values (?, ?, ?, ?, ?, ?)", fila)
        conexion.commit()
        print("Alta de cliente realizada con éxito")
    except sqlite3.Error as e:
        print(e)

def altaFactura(fila):
    try:
        cur.execute('insert into facturas (dnicliente, idcamarero, idmesa, fecha) values(?,?,?,?)', fila)
        conexion.commit()
        print("Alta de factura realizada con éxito")
    except sqlite3.Error as e:
        print(e)

def bajaFactura(facturas):
    try:
        cur.execute("SELECT MAX(IDFACTURA) FROM FACTURAS")
        factura = str(cur.fetchone())
        for char in "(),'":
            factura = factura.replace(char, '')
        cur.execute("delete from facturas where idFactura = " + factura + "")
        cur.execute("delete from lineafacturas where idFactura= " + factura + "")
        cargarFactura(facturas, 0)
    except sqlite3.Error as e:
        print(e)

def imprimir(idFactura, fechaFactura):
    try:
        cser = canvas.Canvas(str(idFactura) + '.pdf', pagesize=A4)
        cur.execute("select IDVENTA, S.SERVICIO, CANTIDAD, S.PRECIO "
                    "from lineaFacturas L, servicios S "
                    "where L.idFactura = " + str(idFactura) + " and S.idServicio = L.idServicio")
        listado = cur.fetchall()
        conexion.commit()

        #Cabecera:
        cser.setLineWidth(2) #Tamaño de linea
        cser.line(0, 800, 610, 800)
        cser.line(0, 700, 610, 700)

        #Establecer fecha:
        cser.setLineWidth(0.20)
        cser.drawString(500, 680, str(fechaFactura))
        cser.line(480, 677, 580, 677)

        #Escribir productos:
        textlistado = 'Factura'
        cser.drawString(255, 605, textlistado)
        cser.line(50, 598, 525, 598)
        x = 50
        y = 568
        total = 0

        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 115
                    cser.drawString(x, y, str(registro[i]))
                var1 = int(registro[2])
                var2 = registro[3].split()[0]
                var2 = locale.atof(var2)
                var2 = round(float(var2), 2)
                subtotal = var1 * var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x = x + 120
            cser.drawString(x, y, str(subtotal))
            y = y - 20
            x = 50

        y = y - 20
        cser.line(50, y, 525, y)
        y = y - 20
        x = 400

        #Escribir el total:
        cser.drawString(x, y, 'Total:')
        x = 480
        total = round(float(total), 2)
        total = locale.currency(total)
        cser.drawString(x, y, str(total))

        #Pie:
        cser.setLineWidth(2)
        cser.line(0, 40, 610, 40)

        #Impresión del pdf:
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        print(os.getcwd())
        os.system('/usr/bin/xdg-open ' + dir + '/' + str(idFactura) + '.pdf')
        print('Factura preparada para impresión')
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def imprimirFactura(idFactura):
    try:
        cser = canvas.Canvas(str(idFactura) + '.pdf', pagesize=A4)
        cur.execute("select IDVENTA, S.SERVICIO, CANTIDAD, S.PRECIO "
                    "from lineaFacturas L, servicios S "
                    "where L.idFactura = "+str(idFactura)+" and S.idServicio = L.idServicio")
        listado = cur.fetchall()
        conexion.commit()

        textlistado = 'Factura'
        cser.line(50, 380, 525, 300)
        cser.drawString(255, 705, textlistado)
        cser.line(50, 700, 525, 700)
        x = 50
        y = 680
        total = 0

        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 120
                    cser.drawString(x, y, str(registro[i]))
                var1 = int(registro[2])
                var2 = registro[3].split()[0]
                var2 = locale.atof(var2)
                var2 = round(float(var2),2)
                subtotal = var1*var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x= x + 120
            cser.drawString(x, y, str(subtotal))
            y = y - 20
            x = 50

        y = y - 20
        cser.line(50, y, 525, y)
        y = y - 20
        x = 400
        cser.drawString(x, y, 'Total:')
        x = 485
        total = round(float(total),2)
        total = locale.currency(total)
        cser.drawString(x, y, str(total))

        cser.showPage()
        cser.save()
        dir = os.getcwd()
        print(os.getcwd())
        os.system('/usr/bin/xdg-open '+dir+'/'+str(idFactura)+'.pdf')
        print('Factura preparada para impresión')
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

#def altaFactura(fila, facturas, idmesa):
#    try:
#        cur.execute('insert into facturas (idcliente, idcamarero, idmesa, fecha) values(?,?,?,?)', fila)
#        conexion.commit()
#        print("Alta de factura realizada con éxito")
#        cargarFactura(facturas,idmesa)
#    except sqlite3.Error as e:
#        print(e)

 # MÉTODOS AUXILIARES:
def cargaComunidad():
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

def ocuparMesa(estado, mesa):
    try:
        cur.execute("update mesas set estado = '"+estado+"' where idmesa = '"+str(mesa)+"'")
        conexion.commit()
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def generarMenuDia():
    try:
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'ENTRANTE'")
        entrantes = cur.fetchall()
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'Plato'")
        platos = cur.fetchall()
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'POSTRE'")
        postres = cur.fetchall()
        index = 0
        p = 0
        lista = []
        for n in platos:
            p = p + 1
        while index < 3:
            num1 = random.randint(1, p)
            num2 = 0
            for n in platos:
                if num2 == num1:
                    if platos[num2] not in lista:
                        print(platos[num2])
                        lista.append(n)
                        print(lista)
                        index = index + 1
                else:
                    num2 = num2 + 1

    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

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



