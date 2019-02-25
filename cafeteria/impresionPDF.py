import datetime
import locale
import os
import random
import sqlite3

# Establece la conexión:
from reportlab.lib.colors import black, white, forestgreen
from reportlab.lib.pagesizes import A4, A6
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

try:
    conexion = sqlite3.Connection("Restaurante")
    cur = conexion.cursor()
except sqlite3.OperationalError as e:
    print(e)

def imprimirFactura(idFactura,fechaFactura, clienteFactura):
    '''Impresión de facturas
        Realiza la consulta a la base de datos para obtener los datos necesarios y genera la factura
        en pdf. '''
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
    '''Imprimir recibo
        Se realiza una consulta a la base de datos para obtener la información necesaria
        y se genera un recibo sin los datos personales del cliente en pdf'''
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


def imprimirMenu():
    '''Imprimir menu
        Recorre el listado de platos obtenido del métofo generaMenuDia situándolos en el pdf,
        una vez realizado imprime el mismo y los muestra por pantalla'''
    dia = datetime.datetime.now().strftime("%d")
    mes = datetime.datetime.now().strftime("%m")
    ano = datetime.datetime.now().strftime("%Y")
    mes = int(mes) - 1
    fecha = "%s_" % dia + "%s_" % (mes + 1) + "%s" % ano
    cser = canvas.Canvas('MENU_' + str(fecha) + '.pdf', pagesize=A4)
    listado = generarMenuDia()

    #Decorado
    cser.setFillColor(white)
    cser.drawInlineImage("./imgs/fondo.jpg",0,0)
    cser.rect(65, 65, 465, 900, stroke=0, fill=1)
    pdfmetrics.registerFont(TTFont('Sawasdee', 'Sawasdee.ttf'))
    cser.setFillColor(forestgreen)
    cser.setFontSize(13)
    cser.drawString(116, 763, 'THE')
    cser.setFont('Sawasdee', 75)
    cser.drawString(110, 704, 'Green Side')
    cser.drawString(109, 705, 'Green Side')
    cser.setFontSize(13)
    cser.drawString(410, 690, 'RESTAURANT')
    cser.setFillColor(forestgreen)
    cser.setStrokeColor(forestgreen)

    #Categorías:
    cser.setFontSize(17)
    cser.drawString(107,617, "Entrantes")
    cser.drawString(106.5, 617, "Entrantes")
    cser.line(107, 608, 490, 608)
    cser.drawString(107, 470, "Platos")
    cser.drawString(106.5, 470, "Platos")
    cser.line(107, 463, 490, 463)
    cser.drawString(107, 325, "Postres")
    cser.drawString(106.5, 325, "Postres")
    cser.line(107, 320, 490, 320)
    cser.setFontSize(13)
    cser.setFillColor(black)

    #Imprimir platos:
    x = 120
    y = 590
    index = 0
    for registro in listado:
        cser.drawString(x, y, registro[0])
        #cser.drawRightString(483, y, registro[1])
        y = y - 25
        index = index + 1
        if index == 3 or index == 6:
            y = y - 70

    #Pie:
    cser.setFillColor(forestgreen)
    cser.setFont('Sawasdee', 36)
    cser.drawCentredString(295, 160, 'PRECIO 10.90€')
    cser.drawString(309, 159, '10.90€')
    cser.setFillColor(black)
    cser.setFont('Sawasdee', 19)
    cser.drawCentredString(295, 130, '(Pan, bebida y café incluídos)')

    #Impresión del pdf:
    cser.showPage()
    cser.save()
    dir = os.getcwd()
    os.system('/usr/bin/xdg-open ' + dir + '/MENU_' + str(fecha) + '.pdf')
    print('Factura preparada para impresión')


def generarMenuDia():
    '''GENERADOR DEL MENÚ DEL DÍA
        Método que se encarga de guardar en listas las tuplas correspondientes a cada categoría
        y recorrer dichas listas para sacar el plato correspondiente a una posición aleatoria
        comprobando que no haya repeticiones'''

    try:
        #Se guardan en variables los datos consultados a la BD
        cur.execute("SELECT SERVICIO, PRECIO FROM SERVICIOS WHERE CATEGORIA = 'Entrante'")
        entrantes = cur.fetchall()
        cur.execute("SELECT SERVICIO, PRECIO FROM SERVICIOS WHERE CATEGORIA = 'Plato'")
        platos = cur.fetchall()
        cur.execute("SELECT SERVICIO, PRECIO FROM SERVICIOS WHERE CATEGORIA = 'Postre'")
        postres = cur.fetchall()
        conexion.commit() #Se corta la conexion

        #Se guardan en variables la longitud de dichas consultas
        en = len(entrantes)
        pl = len(platos)
        po = len(postres)

        listado = []

        #Se procede a realizar los bucles siempre y cuando de cada categoría haya más de tres platos
        if en > 3 and pl > 3 and po > 3:
            index = 0 #Se inicializa el indice
            while index < 3:
                num1 = random.randint(1, en)
                num2 = 0
                for n in entrantes:
                    #Se recorre la lista y mientras num2 no sea igual que num1, vamos sumándole 1
                    if num2 == num1:
                        if entrantes[num2] not in listado:
                            #Si es igual comprobamos si ya está en la lista para guardar el dato en caso negativo
                            listado.append(n)
                            index = index + 1
                    else:
                        num2 = num2 + 1
            #Fin del primer bucle (ENTRANTES)

            index = 0 #Se resetea la variable
            while index < 3:
                num1 = random.randint(1, en)
                num2 = 0
                for n in platos:
                    if num2 == num1:
                        if platos[num2] not in listado:
                            listado.append(n)
                            index = index + 1
                    else:
                        num2 = num2 + 1
            #Fin del segundo bucle (PLATOS)

            index = 0 #Se resetea la variable
            while index < 3:
                num1 = random.randint(1, en)
                num2 = 0
                for n in postres:
                    if num2 == num1:
                        if postres[num2] not in listado:
                            listado.append(n)
                            index = index + 1
                    else:
                        num2 = num2 + 1
            #Fin del tercer bucle (POSTRES)
            return listado
    except sqlite3.Error as e:
        print(e)
        conexion.rollback()