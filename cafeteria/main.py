import datetime

import gi
gi.require_version('Gtk','3.0')
import database
import gtk
from gi.repository import Gtk



class Main:
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('interfaz.glade')

    # Ventanas:
        self.venlogin = b.get_object("venlogin")
        self.venprincipal = b.get_object("venprincipal")
        self.venacerca = b.get_object("venacerca")
        self.venerror = b.get_object("venerror")
        self.venconfirma = b.get_object("venconfirma")
        self.vencliente = b.get_object("vencliente")
        self.vencomanda = b.get_object("vencomanda")
        self.vencalendario = b.get_object("vencalendario")
        self.venjornada = b.get_object("venjornada")

    # Botones:
        self.btnAbout = b.get_object("btnAbout")
        self.btnAcerca = b.get_object("btnAcerca")
        self.btnSalir = b.get_object("btnSalir")
        self.btnLogout = b.get_object("btnLogout")
        self.cancelConfirma = b.get_object("cancelConfirma")
        self.aceptConfirma = b.get_object("aceptConfirma")
        self.cancelCliente = b.get_object("cancelCliente")
        self.aceptCliente = b.get_object("aceptCliente")

    # Recursos:
        self.treeProductos = b.get_object("treeProductos")
        self.productos = b.get_object("productos")
        self.treeCamareros = b.get_object("treeCamareros")
        self.camareros = b.get_object("camareros")
        self.treeFacturas = b.get_object("treeFacturas")
        self.treeProductos2 = b.get_object("treeProductos2")
        self.treeComandas = b.get_object("treeComandas")
        self.comandas = b.get_object("comandas")
        self.facturas = b.get_object("facturas")
        self.Pestanas = b.get_object("Pestanas")
        self.lblError = b.get_object("lblError")
        self.btnError = b.get_object("btnError")
        self.lblAviso = b.get_object("lblAviso")
        self.lblConfirma = b.get_object("lblConfirma")
        self.jornadaPwd = b.get_object("jornadaPwd")
        self.password = ""
        self.eDni = True

    # Login:
        self.loginEnter = b.get_object("loginEnter")
        self.loginExit = b.get_object("loginExit")
        self.loginUser = b.get_object("loginUser")
        self.loginPwd = b.get_object("loginPwd")


    # Camareros:
        self.lblCamarero = b.get_object("lblCamarero")
        self.inputNombre = b.get_object("inputNombre")
        self.inputPassword = b.get_object("inputPassword")
        self.addCam = b.get_object("addCam")
        self.updateCam = b.get_object("updateCam")
        self.deleteCam = b.get_object("deleteCam")
        self.cleanCam = b.get_object("cleanCam")

    # Productos:
        self.lblProducto = b.get_object("lblProducto")
        self.lblNombre = b.get_object("lblNombre")
        self.lblPrecio = b.get_object("lblPrecio")
        self.addProduct = b.get_object("addProduct")
        self.updateProduct = b.get_object("updateProduct")
        self.deleteProduct = b.get_object("deleteProduct")
        self.cleanProduct = b.get_object("cleanProduct")

    # Gestion:
        self.addFactura = b.get_object("addFactura")
        self.printFactura = b.get_object("printFactura")
        self.lblFCamarero = b.get_object("lblFCamarero")
        self.lblFCliente = b.get_object("lblFCliente")
        self.btnFCliente = b.get_object("btnFCliente")
        self.lblFMesa = b.get_object("lblFMesa")
        self.lblFFecha = b.get_object("lblFFecha")
        self.btnFFecha = b.get_object("btnFFecha")
        self.clienteDNI = b.get_object("clienteDNI")
        self.clienteNombre = b.get_object("clienteNombre")
        self.clienteApellido = b.get_object("clienteApellido")
        self.clienteProv = b.get_object("clienteProv")
        self.clienteCiu = b.get_object("clienteCiu")
        self.clienteComu = b.get_object("clienteComu")
        self.calendar = b.get_object("calendar")
        self.comunidad = ''
        self.provincia = ''
        self.ciudad = ''
        self.servicio = ''
        self.idFactura = ''
        self.idMesa = ''
        self.fechaFactura = ''

    # Mesas:
        self.lblmesa1 = b.get_object("lblmesa1")
        self.lblmesa2 = b.get_object("lblmesa2")
        self.lblmesa3 = b.get_object("lblmesa3")
        self.lblmesa4 = b.get_object("lblmesa4")
        self.lblmesa5 = b.get_object("lblmesa5")
        self.lblmesa6 = b.get_object("lblmesa6")
        self.lblmesa7 = b.get_object("lblmesa7")
        self.lblmesa8 = b.get_object("lblmesa8")
        self.lblmesa9 = b.get_object("lblmesa9")
        self.mesas = (self.lblmesa1, self.lblmesa2, self.lblmesa3, self.lblmesa4, self.lblmesa5, self.lblmesa6, self.lblmesa7, self.lblmesa8, self.lblmesa9)


        dic = {'on_btnSalir_activate':self.salir,
               'on_loginExit_clicked':self.salir,
               'on_loginEnter_clicked':self.login,
               'on_ btnLogout_activate':self.logout,
               'on_btnFinJornada_activate':self.abrirJornada,
               'on_aceptJornada_clicked':self.terminarJornada,
               'on_cancelJornada_clicked':self.cerrarJornada,
               'on_btnMaximize_activate':self.maximizarVentana,
               'on_btnAbout_activate':self.abrirAbout,
               'on_btnAcerca_clicked':self.cerrarAbout,
               'on_btnError_clicked':self.cerrarError,
               'on_cancelConfirma_clicked':self.cerrarConfirma,
               'on_aceptConfirma_clicked':self.aceptarConfirma,
               'on_venprincipal_destroy':self.salir,
               'on_venprincipal_delete_event':self.salir,
               'on_venlogin_destroy':self.salir,
               'on_venlogin_delete_event':self.salir,
               'on_cleanCam_clicked':self.limpiarCam,
               'on_addCam_clicked':self.altaCamarero,
               'on_updateCam_clicked':self.modificaCamarero,
               'on_deleteCam_clicked':self.abrirConfirma,
               'on_cleanProduct_clicked':self.limpiarProd,
               'on_adProduct_clicked':self.altaProducto,
               'on_updateProduct_clicked':self.modificaProducto,
               'on_deleteProduct_clicked':self.abrirConfirma,
               'on_inputNombre_focus_out_event':self.mayus,
               'on_lblNombre_focus_out_event':self.mayus,
               'on_clienteApellido_focus_out_event':self.mayus,
               'on_clienteDNI_focus_out_event':self.mayus,
               'on_clienteNombre_focus_out_event':self.mayus,
               'on_treeCamareros_cursor_changed':self.seleccionaCamarero,
               'on_treeProductos_cursor_changed':self.seleccionaProducto,
               'on_treeProductos2_cursor_changed':self.seleccionaProducto2,
               'on_treeComandas_cursor_changed':self.seleccionaComanda,
               'on_clienteComu_changed':self.actualizarProvincias,
               'on_clienteProv_changed':self.actualizarMunicipios,
               'on_btnFCliente_clicked':self.abrirCliente,
               'on_cancelCliente_clicked':self.cerrarCliente,
               'on_aceptCliente_clicked':self.altaCliente,
               'on_addFactura_clicked':self.abrirComandas,
               'on_addLinea_clicked':self.gestionComandas,
               'on_deleteLinea_clicked':self.eliminarComandas,
               'on_aceptComanda_clicked':self.aceptarComanda,
               'on_cancelComanda_clicked':self.cancelarComanda,
               'on_cleanFactura_clicked': self.limpiarFact,
               'on_btnFFecha_clicked':self.abrirCalendario,
               'on_calendar_day_selected_double_click':self.cerrarCalendario,
               'on_treeFacturas_cursor_changed':self.seleccionaFactura,
               'on_printFactura_clicked':self.imprimeFactura,
               'on_mesa1_clicked':self.mesa1,
               'on_mesa2_clicked': self.mesa2,
               'on_mesa3_clicked': self.mesa3,
               'on_mesa4_clicked': self.mesa4,
               'on_mesa5_clicked': self.mesa5,
               'on_mesa6_clicked': self.mesa6,
               'on_mesa7_clicked': self.mesa7,
               'on_mesa8_clicked': self.mesa8,
               'on_mesa9_clicked': self.mesa9,
               }

        b.connect_signals(dic)
        self.loginUser.set_text("01")
        self.loginPwd.set_text("root")
        self.venlogin.show()
        print("Iniciando el programa")
        database.cargarCamarero(self.camareros)
        database.cargarProducto(self.productos)
        database.cargarFactura(self.facturas, 0)
        self.cargarComunidades()
        self.cargaMesas()
        self.inicializarCalendario()

    # Cerrar ventanas:
        self.venprincipal.connect('delete-event', lambda w, e: w.hide() or True)
        self.venacerca.connect('delete-event', lambda w, e: w.hide() or True)
        self.venerror.connect('delete-event', lambda w, e: w.hide() or True)
        self.venconfirma.connect('delete-event', lambda w, e: w.hide() or True)
        self.vencliente.connect('delete-event', lambda w, e: w.hide() or True)
        self.venlogin.connect('delete-event', lambda w, e: w.hide() or True)
        self.vencomanda.connect('delete-event', lambda w, e: w.hide() or True)
        self.vencalendario.connect('delete-event', lambda w, e: w.hide() or True)
        self.venjornada.connect('delete-event', lambda w, e: w.hide() or True)

    # MÉTODOS DE SELECCIÓN PARA LOS TREEVIEW
    def seleccionaCamarero(self, widget):
        model, iter = self.treeCamareros.get_selection().get_selected()
        if iter != None:
            self.lblCamarero.set_text(str(model.get_value(iter, 0)))
            self.inputNombre.set_text(model.get_value(iter, 1))
            self.password = database.buscaPWD(self.lblCamarero.get_text())
            self.inputPassword.set_text("**********")

    def seleccionaProducto(self, widget):
        model, iter = self.treeProductos.get_selection().get_selected()
        if iter != None:
            self.lblProducto.set_text(str(model.get_value(iter, 0)))
            self.lblNombre.set_text(model.get_value(iter, 1))
            precio = str(model.get_value(iter, 2))
            for char in '€':
                precio = precio.replace(char, '')
            self.lblPrecio.set_text(precio)

    def seleccionaProducto2(self, widget):
        model, iter = self.treeProductos2.get_selection().get_selected()
        if iter != None:
            self.servicio = str(model.get_value(iter, 0))

    def seleccionaComanda(self, widget):
        model, iter = self.treeComandas.get_selection().get_selected()
        if iter != None:
            self.servicio = str(model.get_value(iter, 0))

    def seleccionaFactura(self, widget):
        model, iter = self.treeFacturas.get_selection().get_selected()
        if iter != None:
            self.idFactura = model.get_value(iter, 0)
            self.idMesa = model.get_value(iter, 3)
            self.fechaFactura = model.get_value(iter, 4)

    # MÉTODOS RELACIONADOS CON EL ALTA DE CAMAREROS
    def altaCamarero(self, widget):
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        nombre = self.inputNombre.get_text()
        password = self.inputPassword.get_text()
        if len(nombre) > 0 and len(password) > 0:
            fila = (nombre, password)
            database.altaCamarero(fila, self.camareros)
            self.limpiarCam(widget)
            self.lblAviso.set_markup("<span color='gray'>Alta de camarero completada con éxito</span>")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def modificaCamarero(self, widget):
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        nombre = self.inputNombre.get_text()
        password = self.inputPassword.get_text()
        if self.lblCamarero.get_text() == "Seleccionar camarero":
            self.lblAviso.set_markup("<span color='gray'>No se ha seleccionado ningún camarero</span>")
        else:
            if len(nombre) > 0 and len(password) > 0:
                if password == "**********":
                    password = self.password
                fila = (nombre, password)
                database.modificaCamarero(fila, self.lblCamarero.get_text(), self.camareros)
                self.limpiarCam(widget)
                self.lblAviso.set_markup("<span color='gray'>Modificación de camarero completada con éxito</span>")
            else:
                self.lblError.set_text("Debe cubrir todos los campos")
                self.abrirError(widget)

    def bajaCamarero(self, widget):
        id = self.lblCamarero.get_text()
        database.bajaCamarero(id,self.camareros)
        self.limpiarCam(widget)
        self.lblAviso.set_markup("<span color='gray'>Baja de camarero completada con éxito</span>")

    # Productos
    def altaProducto(self, widget):
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        nombre = self.lblNombre.get_text()
        precio = self.lblPrecio.get_text()+" €"
        if len(nombre) > 0 and len(precio) > 0:
            fila = (nombre, precio)
            database.altaProducto(fila, self.productos)
            self.limpiarProd(widget)
            self.lblAviso.set_markup("<span color='gray'>Alta de producto completada con éxito</span>")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def modificaProducto(self, widget):
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        nombre = self.lblNombre.get_text()
        precio = self.lblPrecio.get_text()+" €"
        if self.lblCamarero.get_text() == "Seleccionar producto":
            self.lblAviso.set_markup("<span color='gray'>No se ha seleccionado ningún producto</span>")
        else:
            if len(nombre) > 0 and len(precio) > 0:
                fila = (nombre, precio)
                database.modificaProducto(fila, self.lblProducto.get_text(), self.productos)
                self.limpiarProd(widget)
                self.lblAviso.set_markup("<span color='gray'>Modificación de producto completada con éxito</span>")
            else:
                self.lblError.set_text("Debe cubrir todos los campos")
                self.abrirError(widget)

    def bajaProducto(self, widget):
        id = self.lblProducto.get_text()
        database.bajaProducto(id, self.productos)
        self.limpiarProd(widget)
        self.lblAviso.set_markup("<span color='gray'>Baja de producto completada con éxito</span>")

    def altaCliente(self, widget):
        self.clienteNombre.set_text(self.clienteNombre.get_text().title())
        self.clienteApellido.set_text(self.clienteApellido.get_text().title())
        self.clienteDNI.set_text(self.clienteDNI.get_text().upper())
        dni = self.clienteDNI.get_text()
        nombre = self.clienteNombre.get_text()
        apellido = self.clienteApellido.get_text()
        comunidad = str(self.clienteComu.get_active_text())
        provincia = str(self.clienteProv.get_active_text())
        ciudad = str(self.clienteCiu.get_active_text())
        if len(nombre) > 0 and len(apellido) > 0 and comunidad != "None" and provincia != "None" and ciudad != "None":
            self.validaDNI(widget)
            if self.eDni == False:
                fila = (dni, apellido, nombre, comunidad, provincia, ciudad)
                database.altaCliente(fila)
                self.limpiarCli(widget)
                self.lblFCliente.set_text(dni)
                self.cerrarCliente(widget)
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def gestionComandas(self, widget):
        '''Añadir tuplas a la tabla lineasFactura
            El método se ejecuta cuando se pulsa el botón añadir en la ventana vencomandas'''
        database.altaLinea(self.comandas, self.servicio)

    def eliminarComandas(self, widget):
        database.bajaLinea(self.comandas, self.servicio)

    def cancelarComanda(self, widget):
        database.bajaFactura(self.facturas)
        self.vencomanda.hide()

    def aceptarComanda(self, widget):
        database.limpiarComandas(self.comandas)
        database.ocuparMesa("No disponible", self.lblFMesa.get_text())
        database.cargarFactura(self.facturas, self.lblFMesa.get_text())
        self.cargaMesas()
        self.vencomanda.hide()
        self.lblFCliente.set_text("Seleccionar cliente")
        self.lblFMesa.set_text("Seleccionar mesa")
        self.inicializarCalendario()
        self.lblAviso.set_markup("<span color='gray'>Alta de factura completada con éxito</span>")



    # Validaciones:
    def validaDNI(self, widget):
        dni = self.clienteDNI.get_text()
        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    self.eDni = False
                    self.lblAviso.set_text('')
                else:
                    self.eDni = True
                    self.lblError.set_text("El DNI introducido debe ser un DNI válido")
                    self.abrirError(widget)
            else:
                self.eDni = True
                self.lblError.set_text("La longitud del DNI debe ser de 9 caracteres")
                self.abrirError(widget)
        except:
            self.eDni = True
            self.lblError.set_text("El DNI introducido debe ser un DNI válido")
            self.abrirError(widget)

    # Metodos recurso:
    def mayus(self, widget, date = None):
        ''' Pone las iniciales y la letra del DNI en mayúsculas '''
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        self.clienteDNI.set_text(self.clienteDNI.get_text().upper())
        self.clienteNombre.set_text(self.clienteNombre.get_text().title())
        self.clienteApellido.set_text(self.clienteApellido.get_text().title())

    def limpiarCam(self, widget):
        ''' Resetea todos los atributos de la pestaña Camareros '''
        self.lblCamarero.set_text("Seleccionar camarero")
        self.inputNombre.set_text("")
        self.inputPassword.set_text("")
        self.lblAviso.set_text("")

    def limpiarProd(self, widget):
        ''' Resetea todos los atributos de la pestaña Productos '''
        self.lblProducto.set_text("Seleccionar producto")
        self.lblNombre.set_text("")
        self.lblPrecio.set_text("")
        self.lblAviso.set_text("")

    def limpiarCli(self, widget):
        ''' Resetea todos los atributos de la ventana Clientes '''
        self.clienteDNI.set_text("")
        self.clienteNombre.set_text("")
        self.clienteApellido.set_text("")
        self.clienteComu.set_active(-1)
        self.clienteProv.set_active(-1)
        self.clienteCiu.set_active(-1)

    def limpiarFact(self, widget):
        ''' Resetea todos los atributos y variables recurso de la pestaña Facturas '''
        self. lblFMesa.set_text("Seleccionar mesa")
        self.lblFCliente.set_text("Seleccionar cliente")
        database.cargarFactura(self.facturas, 0) #Recarga el treeView para que muestre todas las facturas registradas
        self.inicializarCalendario()
        self.mesa = ""
        self.servicio = ""
        self.comunidad = ""
        self.provincia = ""
        self.ciudad = ""

    def cargarComunidades(self):
        lista = database.cargaComunidad()
        for name in lista:
            self.clienteComu.append_text(name[0])

    def actualizarProvincias(self, widget):
        self.comunidad = str(self.clienteComu.get_active_text())
        print(self.comunidad)
        self.cargarProvincias(widget)

    def cargarProvincias(self, widget):
        self.clienteProv.remove_all()
        lista = database.cargaProvincias(self.comunidad)
        for name in lista:
            self.clienteProv.append_text(name[0])

    def actualizarMunicipios(self, widget):
        self.provincia = str(self.clienteProv.get_active_text())
        self.cargarMunicipios(widget)

    def cargarMunicipios(self, widget):
        self.clienteCiu.remove_all()
        lista = database.cargaMunicipios(self.provincia)
        for name in lista:
            self.clienteCiu.append_text(name[0])

    def inicializarCalendario(self):
        dia = datetime.datetime.now().strftime("%d")
        mes = datetime.datetime.now().strftime("%m")
        ano = datetime.datetime.now().strftime("%Y")
        mes = int(mes) - 1
        self.fecha = "%s/" % dia + "%s/" % (mes + 1) + "%s" % ano
        self.lblFFecha.set_text(self.fecha)

    def imprimeFactura(self, widget):
        database.ocuparMesa("Disponible", self.idMesa)
        self.cargaMesas()
        database.imprimir(self.idFactura, self.fechaFactura)

    def terminarJornada(self, widget):
        user = self.lblFCamarero.get_text()
        password = self.jornadaPwd.get_text()
        if len(password):
            fila = database.login(user, password)
            if str(fila[0]) != 'None' and str(fila[1]) != 'None':
                i = 1
                for mesa in self.mesas:
                    database.ocuparMesa("Disponible", str(i))
                    i = i + 1
                self.cargaMesas()
                self.lblAviso.set_markup("<span color='gray'><b>Jornada finalizada</b></span>")
                print('Mesas liberadas con éxito')
                self.cerrarJornada(widget)
            else:
                self.lblError.set_text("Contraseña no válida")
                self.abrirError(widget)
        else:
            self.lblError.set_text("Debe introducir su contraseña")
            self.abrirError(widget)


    # Metodos gestion de mesas:
    def cargaMesas(self):
        i = 0
        listado = database.cargaMesas()
        for n in listado:
            estado = str(listado[i])
            for char in "(),'":
                estado = estado.replace(char, '')
            if estado == "No disponible":
                self.mesas[i].set_markup("<span color='red'>No disponible</span>")
            else:
                self.mesas[i].set_markup("<span color='green'>Disponible</span>")
            i = i + 1

    def mesa1(self, widget):
        self.mesa = 1
        self.estado = self.lblmesa1.get_text()
        database.cargarFactura(self.facturas, 1)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa2(self, widget):
        self.mesa = 2
        self.estado = self.lblmesa2.get_text()
        database.cargarFactura(self.facturas, 2)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa3(self, widget):
        self.mesa = 3
        self.estado = self.lblmesa3.get_text()
        database.cargarFactura(self.facturas, 3)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa4(self, widget):
        self.mesa = 4
        self.estado = self.lblmesa4.get_text()
        database.cargarFactura(self.facturas, 4)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa5(self, widget):
        self.mesa = 5
        self.estado = self.lblmesa5.get_text()
        database.cargarFactura(self.facturas, 5)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa6(self, widget):
        self.mesa = 6
        self.estado = self.lblmesa6.get_text()
        database.cargarFactura(self.facturas, 6)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa7(self, widget):
        self.mesa = 7
        self.estado = self.lblmesa7.get_text()
        database.cargarFactura(self.facturas, 7)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa8(self, widget):
        self.mesa = 8
        self.estado = self.lblmesa8.get_text()
        database.cargarFactura(self.facturas, 8)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")

    def mesa9(self, widget):
        self.mesa = 9
        self.estado = self.lblmesa9.get_text()
        database.cargarFactura(self.facturas, 9)
        if self.estado == "No disponible":
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
        else:
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")


    # Métodos gestión de ventanas:
    def abrirAbout(self, widget):
        self.venacerca.show()

    def cerrarAbout(self, widget):
        self.venacerca.hide()

    def abrirError(self, widget):
        self.venerror.show();

    def cerrarError(self, widget):
        self.venerror.hide()
        self.lblError.set_text("")

    def abrirCalendario(self, widget):
        dia = datetime.datetime.now().strftime("%d")
        mes = datetime.datetime.now().strftime("%m")
        ano = datetime.datetime.now().strftime("%Y")
        mes = int(mes) - 1
        self.calendar.select_month(int(mes), int(ano))
        self.calendar.select_day(int(dia))
        self.vencalendario.show()

    def cerrarCalendario(self, widget):
        ano, mes, dia = self.calendar.get_date()
        self.fecha = "%s/" % dia + "%s/" % (mes + 1) + "%s" % ano
        self.lblFFecha.set_text(self.fecha)
        self.vencalendario.hide()

    def abrirConfirma(self,widget):
        panel = self.Pestanas.get_current_page()
        if panel == 1:
            if self.lblCamarero.get_text() == "Seleccionar camarero":
                self.lblAviso.set_markup("<span color='gray'>No se ha seleccionado ningún camarero</span>")
            else:
                self.venconfirma.show()
        if panel == 2:
            if self.lblProducto.get_text() == "Seleccionar producto":
                self.lblAviso.set_markup("<span color='gray'>No se ha seleccionado ningún producto</span>")
            else:
                self.venconfirma.show()

    def cerrarConfirma(self, widget):
        self.venconfirma.hide()

    def abrirJornada(self, widget):
        self.venjornada.show()

    def cerrarJornada(self, widget):
        self.venjornada.hide()

    def abrirCliente(self, widget):
        self.vencliente.show()

    def abrirComandas(self, widget):
        if self.lblFCliente.get_text() != "Seleccionar cliente" and self.lblFMesa.get_text() != "Seleccionar mesa":
            camarero = self.lblFCamarero.get_text()
            cliente = self.lblFCliente.get_text()
            mesa = self.lblFMesa.get_text()
            fecha = self.lblFFecha.get_text()
            fila = (cliente, camarero, mesa, fecha)
            database.altaFactura(fila)
            self.vencomanda.show()
        else:
            self.lblAviso.set_markup("<span color='gray'>Debe seleccionar un cliente y una mesa</span>")

    def cerrarCliente(self, widget):
        self.limpiarCli(widget)
        self.vencliente.hide()

    def aceptarConfirma(self, widget):
        panel = self.Pestanas.get_current_page()
        if panel == 1:
            self.bajaCamarero(widget)
        if panel == 2:
            self.bajaProducto(widget)
        self.venconfirma.hide()

    def login(self, widget, data = None):
        user = self.loginUser.get_text()
        password = self.loginPwd.get_text()
        if len(user) > 0 and  len(password):
            fila = database.login(user, password)
            if str(fila[0]) != 'None' and str(fila[1]) != 'None':
                self.venlogin.hide()
                self.venprincipal.show()
                print("Iniciando sesión")
                self.lblFCamarero.set_text(user)
            else:
                self.lblError.set_text("Usuario o contraseña no encontrado")
                self.abrirError(widget)
                print("Error en el inicio de sesión")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def logout(self, widget):
        self.loginUser.set_text("")
        self.loginPwd.set_text("")
        print("Cerrando sesión")
        self.venprincipal.hide()
        self.venlogin.show()

    def maximizarVentana(self, widget):
        self.venprincipal.maximize()

    def salir(self, widget, data=None):
        print("Finalizando el programa")
        Gtk.main_quit()

if __name__ == '__main__':
    main = Main()
    Gtk.main()