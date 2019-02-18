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

def cargarFactura2(facturas, dni):
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

        if encontrado == True:
            cur.execute(
                "SELECT Facturas.IDFACTURA, Facturas.DNICLIENTE, Facturas.IDCAMARERO, Facturas.IDMESA, Facturas.FECHA, count(LineaFacturas.IdFactura) "
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
        return encontrado
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def cargarComanda(factura, comandas):
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
def altaLinea(factura, comandas, servicio):
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

def altaCliente(fila, clientes):
    try:
        cur.execute("insert into clientes (dni, apellidos, nombre, comunidad, provincia, ciudad) values (?, ?, ?, ?, ?, ?)", fila)
        conexion.commit()
        print("Alta de cliente realizada con éxito")
        cargarCliente(clientes)
    except sqlite3.Error as e:
        print(e)

def bajaCliente(dni, clientes):
    try:
        cur.execute("delete from clientes where dni = '"+dni+"'")
        print("Baja de cliente realizada con éxito")
        conexion.commit()
        cargarCliente(clientes)
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def altaFactura(fila):
    try:
        cur.execute('insert into facturas (dnicliente, idcamarero, idmesa, fecha) values(?,?,?,?)', fila)
        conexion.commit()
        print("Alta de factura realizada con éxito")
    except sqlite3.Error as e:
        print(e)

def bajaFactura(idFactura, facturas):
    try:
        vacio = False
        cur.execute("SELECT * FROM LINEAFACTURAS WHERE IDFACTURA = '"+str(idFactura)+"'")
        listado = cur.fetchall()
        print("La factura "+idFactura+" tiene "+str(len(listado))+" líneas de venta")
        if len(listado) == 0:
            cur.execute("delete from facturas where idFactura = " + str(idFactura) + "")
            #cur.execute("delete from lineafacturas where idFactura= " + str(idFactura) + "")
            cargarFactura(facturas, 0)
            vacio = True
        else:
            print("No se puede borrar la factura "+idFactura+" porque ya tiene pedidos asociados")
            vacio = False
        return vacio
    except sqlite3.Error as e:
        print(e)

def buscaFactura(idmesa):
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

def imprimirFactura(idFactura,fechaFactura, clienteFactura):
    try:
        cser = canvas.Canvas('FACTURA_'+str(idFactura) + '.pdf', pagesize=A4)
        cur.execute("select IDVENTA, S.SERVICIO, CANTIDAD, S.PRECIO "
                    "from lineaFacturas L, servicios S "
                    "where L.idFactura = " + str(idFactura) + " and S.idServicio = L.idServicio")
        listado = cur.fetchall()
        cur.execute("select dni, nombre, apellidos, comunidad, provincia, ciudad from clientes where dni = '"+str(clienteFactura)+"'")
        cliente = cur.fetchall()
        conexion.commit()

        #Cabecera:
        pdfmetrics.registerFont(TTFont('Sawasdee', 'Sawasdee.ttf'))
        cser.setFillColorCMYK(0.0000,0.1933,0.5546,0.0667,alpha=None)
        cser.rect(0,790,800,100,stroke=0,fill=1)
        cser.rect(538,0,60,800,stroke=0, fill=1)
        cser.setFillColor(black)
        cser.setFontSize(10)
        cser.drawString(243, 816, 'THE')
        cser.setFont('Sawasdee',60)
        cser.drawString(240, 769, 'Green Side')
        cser.drawString(239,770, 'Green Side')
        cser.setFontSize(10)
        cser.drawString(485, 758, 'RESTAURANT')
        cser.rotate(270)
        cser.setFont('Sawasdee', 10)
        cser.drawString(-600,560,"Av. Francisco Regalado 44, Combarro, Pontevedra 36993 | +34 986 000 000 | info@greenside.com")
        cser.rotate(-270)
        cser.setFontSize(10)

        #Datos de la factura:
        cser.setFillColorCMYK(0.0000, 0.1933, 0.5546, 0.0667, alpha=None)
        cser.setFontSize(15)
        cser.drawString(350, 680, "Factura "+str(idFactura))
        cser.setFillColor(black)
        cser.setFontSize(10)
        cser.drawString(350, 665, "Fecha factura: "+str(fechaFactura))

        #Datos del cliente:
        cser.setFillColorCMYK(0.0000, 0.1933, 0.5546, 0.0667, alpha=None)
        cser.setFontSize(15)
        for row in cliente:
            cser.drawString(70, 680, str(row[1])+" "+str(row[2]))
            cser.setFillColor(black)
            cser.setFontSize(10)
            cser.drawString(70, 665, str(row[0]))
            cser.drawString(70, 650, str(row[5])+", "+str(row[4])+", "+str(row[3]))
        cser.setFillColor(black)

        #Escribir productos:
        cser.setFont("Helvetica-Bold", 10)
        cser.setFillColorCMYK(0.0000, 0.1933, 0.5546, 0.0667, alpha=None)
        cser.drawString(70, 530, "ID")
        cser.drawString(107, 530, "SERVICIO")
        cser.drawString(244, 530, "CANTIDAD")
        cser.drawString(315, 530, "PRECIO")
        cser.drawString(420, 530, "TOTAL")
        cser.setFont("Sawasdee",10)
        cser.setFillColor(black)
        x = 70
        y = 500
        total = 0

        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 100
                    cser.drawRightString(x, y, str(registro[i]))
                var1 = int(registro[2])
                var2 = registro[3].split()[0]
                #var2 = locale.atof(var2)
                var2 = round(float(var2), 2)
                subtotal = var1 * var2
                print()
            x = x - 10
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x = x + 80
            cser.drawString(x, y, str(subtotal))
            y = y - 20
            x = 70

        y = y - 20
        y = y - 20

        #Escribir el total:
        cser.setFont("Helvetica-Bold", 10)
        cser.setFillColorCMYK(0.0000, 0.1933, 0.5546, 0.0667, alpha=None)
        cser.drawString(315, y, 'TOTAL A PAGAR:')
        cser.setFillColor(black)
        cser.setFontSize(11)
        x = 457
        total = round(float(total), 2)
        total = locale.currency(total)
        cser.drawRightString(x, y, str(total))

        #Impresión del pdf:
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/FACTURA_' + str(idFactura) + '.pdf')
        print('Factura preparada para impresión')
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

def imprimirRecibo(idFactura):
    try:
        cser = canvas.Canvas('RECIBO_'+str(idFactura) + '.pdf', pagesize=A6)
        cur.execute("select IDVENTA, S.SERVICIO, CANTIDAD, S.PRECIO "
                    "from lineaFacturas L, servicios S "
                    "where L.idFactura = "+str(idFactura)+" and S.idServicio = L.idServicio")
        listado = cur.fetchall()
        conexion.commit()

        #Cabecera:
        pdfmetrics.registerFont(TTFont('Sawasdee', 'Sawasdee.ttf'))
        cser.setFont("Sawasdee",8)
        cser.drawString(28,385, "THE")
        cser.setFontSize(30)
        cser.drawString(25, 360, "Green Side")
        cser.setFontSize(8)
        cser.drawString(129, 350, "RESTAURANT")
        cser.drawString(225, 350, "FACTURA Nº:")
        cser.drawString(225,340,str(idFactura))
        cser.setLineWidth(3)
        cser.line(0, 320, 525, 320)

        cser.drawString(25, 280, "ID")
        cser.drawString(45, 280, "SERVICIO")
        cser.drawString(130, 280, "CANTIDAD")
        cser.drawString(177, 280, "PRECIO")
        cser.drawString(235, 280, "TOTAL")
        x = 25
        y = 265
        total = 0

        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 20
                else:
                    x = x + 70
                    cser.drawRightString(x, y, str(registro[i]))
                var1 = int(registro[2])
                var2 = registro[3].split()[0]
                #var2 = locale.atof(var2)
                var2 = round(float(var2),2)
                subtotal = var1*var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x= x + 58
            cser.drawRightString(x, y, str(subtotal))
            y = y - 10
            x = 25

        y = y - 5
        cser.setLineWidth(1)
        cser.line(23, y, 270, y)
        y = y - 20
        cser.setFont("Helvetica-Bold",8)
        cser.drawString(155, y, 'TOTAL A PAGAR:')
        total = round(float(total),2)
        total = locale.currency(total)
        cser.drawString(235, y, str(total))

        #Pie_
        cser.setFont("Sawasdee",12)
        cser.drawCentredString(150,50,"GRACIAS POR SU VISITA")
        cser.setLineWidth(3)
        cser.line(0, 30, 525, 30)
        cser.setFont('Helvetica', 5)
        cser.drawCentredString(150,15,"Av. Francisco Regalado 44, Combarro | +34 986 000 000 | info@greenside.com")

        #Guardar y abrir pdf:
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        print(os.getcwd())
        os.system('/usr/bin/xdg-open '+dir+'/'+'RECIBO_'+str(idFactura)+'.pdf')
        print('Factura preparada para impresión')
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()

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



