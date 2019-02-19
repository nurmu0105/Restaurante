import locale
import os
import random
import sqlite3

# Establece la conexión:
from reportlab.lib.colors import black
from reportlab.lib.pagesizes import A4, A6
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

try:
    conexion = sqlite3.Connection("Restaurante")
    cur = conexion.cursor()
except sqlite3.OperationalError as e:
    print(e)

def imprimirFactura(idFactura,fechaFactura, clienteFactura):
    try:
        print("INTERIOR: "+str(idFactura))
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


def generarMenuDia():
    try:
        #Se guardan en variables los platos de cada categoría
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'ENTRANTE'")
        entrantes = cur.fetchall()
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'Plato'")
        platos = cur.fetchall()
        cur.execute("SELECT * FROM SERVICIOS WHERE CATEGORIA = 'POSTRE'")
        postres = cur.fetchall()

        #En variables se almacena la longitud de los resultados anteriores
        en = len(entrantes)
        p = len(platos)
        po = len(postres)

        index = 0
        lista = []

        while index < 3:
            num1 = random.randint(1, 5)
            num2 = 0
            for n in entrantes:
                if num2 == num1:
                    if entrantes[num2] not in lista:
                        lista.append(n)
                        print(lista)
                        index = index + 1
                else:
                    num2 = num2 + 1

       # index = 0
        #while index < 3:
         #   num1 = random.randint(1, p)
          #  num2 = 0
           # for n in platos:
            ##    if num2 == num1:
              #      if platos[num2] not in lista:
               #         lista.append(n)
                #        print(lista)
                 #       index = index + 1
              #  else:
               #     num2 = num2 + 1

   #     index = 0
    #    while index < 3:
     #       num1 = random.randint(1, po)
       #     num2 = 0
        #    for n in postres:
         #       if num2 == num1:
          #          if postres[num2] not in lista:
           #             lista.append(n)
            #            print(lista)
             #           index = index + 1
              #  else:
               #     num2 = num2 + 1

    except sqlite3.Error as e:
        print(e)
        conexion.rollback()