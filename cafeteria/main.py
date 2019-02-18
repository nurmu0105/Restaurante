import datetime

import gi
from gi.overrides import Gdk

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
        self.treeClientes = b.get_object("treeClientes")
        self.clientes = b.get_object("clientes")
        self.treeProductos = b.get_object("treeProductos")
        self.productos = b.get_object("productos")
        self.treeCamareros = b.get_object("treeCamareros")
        self.camareros = b.get_object("camareros")
        self.treeFacturas = b.get_object("treeFacturas")
        self.treeProductos2 = b.get_object("treeProductos2")
        self.treeComandas = b.get_object("treeComandas")
        self.comandas = b.get_object("comandas")
        self.facturas = b.get_object("facturas")
        self.Panel = b.get_object("Panel")
        self.Pestanas = b.get_object("Pestanas")
        self.Camareros = b.get_object("Camareros")
        self.Productos = b.get_object("Productos")
        self.Facturas = b.get_object("Facturas")
        self.Home = b.get_object("Home")
        self.Comandas = b.get_object("Comandas")
        self.Clientes = b.get_object("Clientes")
        self.Mesas = b.get_object("Mesas")
        self.LoginPie = b.get_object("LoginPie")
        self.LoginTexto1 = b.get_object("LoginTexto1")
        self.LoginTexto2 = b.get_object("LoginTexto2")
        self.LoginTexto3 = b.get_object("LoginTexto3")
        self.LoginSeparator = b.get_object("LoginSeparator")
        self.HomeHeader = b.get_object("HomeHeader")
        self.lblHCamarero = b.get_object("lblHCamarero")
        self.lblHFecha = b.get_object("lblHFecha")
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
        self.categoria1 = b.get_object("categoria1")
        self.categoria2 = b.get_object("categoria2")
        self.categoria3 = b.get_object("categoria3")
        self.categoria4 = b.get_object("categoria4")
        self.addProduct = b.get_object("addProduct")
        self.updateProduct = b.get_object("updateProduct")
        self.deleteProduct = b.get_object("deleteProduct")
        self.cleanProduct = b.get_object("cleanProduct")
        self.categoria = ''

    # Gestion:
        self.addFactura = b.get_object("addFactura")
        self.printFactura = b.get_object("printFactura")
        self.lblFMesa = b.get_object("lblFMesa")
        self.inputFCliente = b.get_object("inputFCliente")
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
        self.clienteFactura = ''
        self.idcliente = ''
        self.mesa = 0

    # Comandas:
        self.lblCFactura = b.get_object("lblCFactura")
        self.lblCMesa = b.get_object("lblCMesa")

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
               'on_categoria1_toggled':self.seleccionarCategoria,
               'on_categoria2_toggled':self.seleccionarCategoria,
               'on_categoria3_toggled':self.seleccionarCategoria,
               'on_categoria4_toggled':self.seleccionarCategoria,
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
               'on_treeClientes_cursor_changed':self.seleccionaCliente,
               'on_clienteComu_changed':self.actualizarProvincias,
               'on_clienteProv_changed':self.actualizarMunicipios,
               'on_btnLimpiarClientes_clicked':self.limpiarCli,
               'on_bajaCliente_clicked':self.abrirConfirma,
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
               'on_printTicket_clicked':self.imprimeRecibo,
               'on_aceptComanda_clicked':self.imprimeRecibo,
               'on_clienteOcupar_clicked':self.ocuparMesa,
               'on_btnBuscaFactura_clicked':self.buscaFactura,
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
        # Abre la ventana de log in
        self.venlogin.show()
        print("Iniciando el programa")
        # Carga las tablas, el panel de mesas y el calendario
        database.cargarCamarero(self.camareros)
        database.cargarProducto(self.productos)
        database.cargarFactura(self.facturas, 0)
        database.cargarCliente(self.clientes)
        #database.generarMenuDia()
        self.cargarComunidades()
        self.cargaMesas()
        self.inicializarCalendario()
        # Colorea la aplicación
        self.color()


    # Cerrar ventanas:
        self.venprincipal.connect('delete-event', lambda w, e: w.hide() or True)
        self.venacerca.connect('delete-event', lambda w, e: w.hide() or True)
        self.venerror.connect('delete-event', lambda w, e: w.hide() or True)
        self.venconfirma.connect('delete-event', lambda w, e: w.hide() or True)
        self.venlogin.connect('delete-event', lambda w, e: w.hide() or True)
        self.vencalendario.connect('delete-event', lambda w, e: w.hide() or True)
        self.venjornada.connect('delete-event', lambda w, e: w.hide() or True)

    # MÉTODOS DE SELECCIÓN PARA LOS TREEVIEW
    def seleccionaCamarero(self, widget):
        '''Rellena los campos en la pestaña de Camareros cuando se selecciona el TreeView correspondiente'''
        model, iter = self.treeCamareros.get_selection().get_selected()
        if iter != None:
            self.lblCamarero.set_text(str(model.get_value(iter, 0)))
            self.inputNombre.set_text(model.get_value(iter, 1))
            self.password = database.buscaPWD(self.lblCamarero.get_text())
            self.inputPassword.set_text("**********")

    def seleccionaProducto(self, widget):
        '''Rellena los campos de la pestaña Productos cuando se selecciona el elemento en el TreeView'''
        model, iter = self.treeProductos.get_selection().get_selected()
        if iter != None:
            self.lblProducto.set_text(str(model.get_value(iter, 0)))
            self.lblNombre.set_text(model.get_value(iter, 1))
            precio = str(model.get_value(iter, 2)).split()[0]
            self.lblPrecio.set_text(precio)
            categoria = str(model.get_value(iter,3))
            if categoria == 'Plato':
                self.categoria2.set_active(True)
            elif categoria == 'Entrante':
                self.categoria1.set_active(True)
            elif categoria == 'Postre':
                self.categoria3.set_active(True)
            else:
                self.categoria4.set_active(True)

    def seleccionaProducto2(self, widget):
        '''Recoge el dato seleccionado en el TreeView de la ventana comandas'''
        model, iter = self.treeProductos2.get_selection().get_selected()
        if iter != None:
            self.servicio = str(model.get_value(iter, 0))

    def seleccionaComanda(self, widget):
        '''Recoge el dato del elemento seleccionado en el TreeView de la ventana comandas'''
        model, iter = self.treeComandas.get_selection().get_selected()
        if iter != None:
            self.servicio = str(model.get_value(iter, 0))

    def seleccionaFactura(self, widget):
        '''Recoge los datos del elemento seleccionado en el TreeView de la pestaña Facturas'''
        model, iter = self.treeFacturas.get_selection().get_selected()
        if iter != None:
            self.idFactura = model.get_value(iter, 0)
            self.idMesa = model.get_value(iter, 3)
            self.fechaFactura = model.get_value(iter, 4)
            self.clienteFactura = model.get_value(iter,1)

    def seleccionaCliente(self, widget):
        model, iter = self.treeClientes.get_selection().get_selected()
        if iter != None:
            self.idcliente = str(model.get_value(iter,0))

    # MÉTODOS RELACIONADOS CON LA GESTIÓN DE CAMAREROS
    def altaCamarero(self, widget):
        '''Alta de camareros
            Primero pone en mayúsculas las iniciales y recoge los valores en unas variables,
            se comprueba la longitud de las mismas para ver si están vacías o no y se mandan
            los datos al método de registro en la base de datos.
            Por último se resetean los datos.
        '''
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        nombre = self.inputNombre.get_text()
        password = self.inputPassword.get_text()
        if len(nombre) > 0 and len(password) > 0:
            fila = (nombre, password)
            database.altaCamarero(fila, self.camareros)
            self.limpiarCam(widget)
            self.lblAviso.set_markup("<span color='white'>Alta de camarero completada con éxito</span>")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def modificaCamarero(self, widget):
        '''Modificaciones de camareros
            Se pone en mayúsculas la inicial y se recogen los datos en unas variables.
            Se comprueba si se ha seleccionado un camarero y en caso informativo comprueba la longitud
            de las variables para ver si han sido introducidas y se envían al método de gestión
            de la base de datos.
            Por último se resetean los datos.
        '''
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        nombre = self.inputNombre.get_text()
        password = self.inputPassword.get_text()
        if self.lblCamarero.get_text() == "Seleccionar camarero":
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún camarero</span>")
        else:
            if len(nombre) > 0 and len(password) > 0:
                if password == "**********":
                    password = self.password
                fila = (nombre, password)
                database.modificaCamarero(fila, self.lblCamarero.get_text(), self.camareros)
                self.limpiarCam(widget)
                self.lblAviso.set_markup("<span color='white'>Modificación de camarero completada con éxito</span>")
            else:
                self.lblError.set_text("Debe cubrir todos los campos")
                self.abrirError(widget)

    def bajaCamarero(self, widget):
        '''Baja de camareros
            Se coge el id del camarero del label y se envía al método correspondiente de gestión
            de la base de datos
            Por último se resetean los datos.
         '''
        id = self.lblCamarero.get_text()
        database.bajaCamarero(id,self.camareros)
        self.limpiarCam(widget)
        self.lblAviso.set_markup("<span color='white'>Baja de camarero completada con éxito</span>")

    # MÉTODOS RELACIONADOS CON LA GESTIÓN DE PRODUCTOS
    def altaProducto(self, widget):
        '''Alta de productos
            Primero pone en mayúsculas las iniciales y recoge los valores en unas variables,
            se comprueba la longitud de las mismas para ver si están vacías o no y se mandan
            los datos al método de registro en la base de datos.
            Por último se resetean los datos.
        '''
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        nombre = self.lblNombre.get_text()
        precio = self.lblPrecio.get_text()+" €"
        if len(nombre) > 0 and len(precio) > 0 and self.categoria != '':
            fila = (nombre, precio, self.categoria)
            database.altaProducto(fila, self.productos)
            self.limpiarProd(widget)
            self.lblAviso.set_markup("<span color='white'>Alta de producto completada con éxito</span>")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def modificaProducto(self, widget):
        '''Modificación de productos
            Se pone en mayúsculas las iniciales y se recogen los datos en una variable.
            Se comprueba si se ha seleccionado un producto, en caso afirmativo comprueba
            la longitud de los datos introducidos y los envía al método correspondiente
            de gestión de la base de datos.
            Se resetean los datos.
        '''
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        nombre = self.lblNombre.get_text()
        precio = self.lblPrecio.get_text()+" €"
        print(nombre, precio, self.categoria)
        if self.lblProducto.get_text() == "Seleccionar producto":
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún producto</span>")
        else:
            if len(nombre) > 0 and len(precio) > 2 and self.categoria != '':
                fila = (nombre, precio, self.categoria)
                database.modificaProducto(fila, self.lblProducto.get_text(), self.productos)
                self.limpiarProd(widget)
                self.lblAviso.set_markup("<span color='white'>Modificación de producto completada con éxito</span>")
            else:
                self.lblError.set_text("Debe cubrir todos los campos")
                self.abrirError(widget)

    def bajaProducto(self, widget):
        '''Baja de productos
            Se recoge el id del producto en una variables que se manda al método correspondiente de la BBDD
        '''
        id = self.lblProducto.get_text()
        database.bajaProducto(id, self.productos)
        self.limpiarProd(widget)
        self.lblAviso.set_markup("<span color='white'>Baja de producto completada con éxito</span>")

    # MÉTODOS RELACIONADOS CON LA GESTIÓN DE FACTURAS + LINEASFACTURAS
    def altaCliente(self, widget):
        '''Alta de clientes
            Se ponen en mayúsculas las iniciales y se recogen los datos en variables.
            Se comprueba que los datos han sido introducidos en los campos correspondientes, en caso
            afirmativo, se llama al método de validar el DNI y si no surge un error, se envían
            los datos al método de gestión de la BBDD
        '''
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
                database.altaCliente(fila, self.clientes)
                self.limpiarCli(widget)
                self.lblAviso.set_markup("<span color='white'>Alta de cliente completada con éxito</span>")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def bajaCliente(self, widget):
        dni = self.idcliente
        database.bajaCliente(dni, self.clientes)
        self.limpiarCli(widget)
        self.lblAviso.set_markup("<span color='white'>Baja de cliente completada con éxito</span>")

    def ocuparMesa(self, widget):
        if self.idcliente != '' and self.mesa != 0:
            database.ocuparMesa("No disponible", self.lblFMesa.get_text())
            self.cargaMesas()
            fila = (self.idcliente,self.lblHCamarero.get_text(),self.mesa,self.lblHFecha.get_text())
            database.altaFactura(fila)
            self.lblCMesa.set_text(str(self.mesa))
            self.idcliente = ""
            self.mesa = 0
            factura = database.buscaFactura(str(self.lblCMesa.get_text()))
            self.lblCFactura.set_text(str(factura))
        else:
            self.lblError.set_text("Debe seleccionar un cliente y una mesa disponible del panel lateral")
            self.abrirError(widget)

    def abrirComandas(self, widget):
        '''Abrir comandas
            Se comprueba si se ha dado de alta el cliente y se ha seleccionado mesa
            Se envían los datos al método de gestión de la base de datos y se abre la ventana vencomandas'''
        if self.lblFCliente.get_text() != "Seleccionar cliente" and self.lblFMesa.get_text() != "Seleccionar mesa":
            camarero = self.lblFCamarero.get_text()
            cliente = self.lblFCliente.get_text()
            mesa = self.lblFMesa.get_text()
            fecha = self.lblFFecha.get_text()
            fila = (cliente, camarero, mesa, fecha)
            database.altaFactura(fila)
            self.vencomanda.show()
        else:
            self.lblAviso.set_markup("<span color='white'>Debe seleccionar un cliente y una mesa</span>")

    def gestionComandas(self, widget):
        '''Añadir tuplas a la tabla lineasFactura
            El método se ejecuta cuando se pulsa el botón añadir en la ventana vencomandas'''
        if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
            if self.servicio != "":
                database.altaLinea(self.lblCFactura.get_text(), self.comandas, self.servicio)
                self.servicio = ""
            else:
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún producto</span>")
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")

    def eliminarComandas(self, widget):
        '''Eliminar comandas
            EL método se ejecuta cuando se pulsa el botón eliminar en la ventana vencomandas'''
        if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
            database.bajaLinea(self.lblCFactura.get_text(), self.comandas, self.servicio)
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")

    def cancelarComanda(self, widget):
        '''Cancelar comanda
            Llama al método encargado de realizar la baja de la factura creada'''
        if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
            vacio = database.bajaFactura(self.lblCFactura.get_text(), self.facturas)
            if(vacio == True):
                database.ocuparMesa("Disponible", self.lblCMesa.get_text())
                self.cargaMesas()
                self.lblCFactura.set_text("Seleccione una mesa ocupada")
                self.lblAviso.set_markup("<span color='white'>Factura cancelada con éxito</span>")
            else:
                self.lblError.set_text("No se puede borrar una factura con productos asociados")
                self.abrirError(widget)
                self.lblAviso.set_text("")
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")

    def aceptarComanda(self, widget):
        '''Aceptar comanda
            Llama al método encargado de resetear la TreeView de vencomandas
            Llama al método de actualizar el estado de la mesa para que aparezca como no disponible
            Llama al método de cargar el TreeView de facturas de la ventana principal
            Llama al método de cargar los labels del panel de gestión de las mesas
            Cierra la ventana vencomandas y resetea los datos'''
        database.limpiarComandas(self.comandas)
        database.ocuparMesa("No disponible", self.lblFMesa.get_text())
        database.cargarFactura(self.facturas, self.lblFMesa.get_text())
        self.cargaMesas()
        self.lblFCliente.set_text("Seleccionar cliente")
        self.lblFMesa.set_text("Seleccionar mesa")
        self.inicializarCalendario()
        self.lblAviso.set_markup("<span color='white'>Alta de factura completada con éxito</span>")

    # MÉTODOS AUXILIARES:
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
        self.categoria1.set_active(True)
        self.categoria2.set_active(False)
        self.categoria3.set_active(False)
        self.categoria = 'Entrante'

    def limpiarCli(self, widget):
        ''' Resetea todos los atributos de la ventana Clientes '''
        self.clienteDNI.set_text("")
        self.clienteNombre.set_text("")
        self.clienteApellido.set_text("")
        self.clienteComu.set_active(-1)
        self.clienteProv.set_active(-1)
        self.clienteCiu.set_active(-1)
        self.idcliente = ""
        self.lblAviso.set_text("")

    def limpiarFact(self, widget):
        ''' Resetea todos los atributos y variables recurso de la pestaña Facturas '''
        self. lblFMesa.set_text("Seleccionar mesa")
        database.cargarFactura(self.facturas, 0) #Recarga el treeView para que muestre todas las facturas registradas
        self.mesa = ""
        self.servicio = ""
        self.comunidad = ""
        self.provincia = ""
        self.ciudad = ""
        self.inputFCliente.set_text("")

    def inicializarCalendario(self):
        dia = datetime.datetime.now().strftime("%d")
        mes = datetime.datetime.now().strftime("%m")
        ano = datetime.datetime.now().strftime("%Y")
        mes = int(mes) - 1
        self.fecha = "%s/" % dia + "%s/" % (mes + 1) + "%s" % ano
        self.lblHFecha.set_text(self.fecha)

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

    def seleccionarCategoria(self, widget):
        if self.categoria1.get_active():
            self.categoria = 'Entrante'
        if self.categoria2.get_active():
            self.categoria = 'Plato'
        if self.categoria3.get_active():
            self.categoria = 'Postre'
        if self.categoria4.get_active():
            self.categoria = 'Otro'

    def imprimeFactura(self, widget):
        if self.idFactura != "":
            if self.clienteFactura != "00000000T":
                database.ocuparMesa("Disponible", self.idMesa)
                self.cargaMesas()
                database.imprimirFactura(self.idFactura, self.fechaFactura, self.clienteFactura)
                self.idFactura = ""
                self.lblAviso.set_text("")
            else:
                self.lblError.set_text("No se puede generar una factura para un cliente anónimo")
                self.abrirError(widget)
                self.lblAviso.set_text("")
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna factura</span>")

    def imprimeRecibo(self, widget):
        if self.idFactura != "" or self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
            if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
                self.idFactura = self.lblCFactura.get_text()
                self.idMesa = self.lblCMesa.get_text()
            print("MESA: "+str(self.idMesa))
            database.ocuparMesa("Disponible", self.idMesa)
            self.cargaMesas()
            database.imprimirRecibo(self.idFactura)
            self.idFactura = ""
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.lblAviso.set_text("")
            self.comandas.clear()
        else:
            self.lblAviso.set_markup("<span color='white'>Seleccione una mesa ocupada</span>")

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

    def buscaFactura(self, widget):
        dni = self.inputFCliente.get_text()
        if len(dni) == 9:
            encontrado = database.cargarFactura2(self.facturas, dni)
            if encontrado == False:
                self.lblError.set_text("No se ha encontrado ningún cliente con ese DNI")
                self.abrirError(widget)
                database.cargarFactura(self.facturas, 0)
        else:
            self.lblError.set_text("La longitud del DNI debe ser de 9 caracteres")
            self.abrirError(widget)


    # MÉTODOS RELACIONADOS CON LA GESTIÓN DEL PANEL MESAS:
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
        self.estado = self.lblmesa1.get_text()
        database.cargarFactura(self.facturas, 1)
        self.lblCMesa.set_text(str(1))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(str(self.lblCMesa.get_text()))
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 1
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa2(self, widget):
        self.estado = self.lblmesa2.get_text()
        database.cargarFactura(self.facturas, 2)
        self.lblCMesa.set_text(str(2))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 2
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa3(self, widget):
        self.estado = self.lblmesa3.get_text()
        database.cargarFactura(self.facturas, 3)
        self.lblCMesa.set_text(str(3))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 3
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa4(self, widget):
        self.estado = self.lblmesa4.get_text()
        database.cargarFactura(self.facturas, 4)
        self.lblCMesa.set_text(str(4))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 4
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa5(self, widget):
        self.estado = self.lblmesa5.get_text()
        database.cargarFactura(self.facturas, 5)
        self.lblCMesa.set_text(str(5))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 5
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa6(self, widget):
        self.estado = self.lblmesa6.get_text()
        database.cargarFactura(self.facturas, 6)
        self.lblCMesa.set_text(str(6))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 6
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa7(self, widget):
        self.estado = self.lblmesa7.get_text()
        database.cargarFactura(self.facturas, 7)
        self.lblCMesa.set_text(str(7))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 7
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa8(self, widget):
        self.estado = self.lblmesa8.get_text()
        database.cargarFactura(self.facturas, 8)
        self.lblCMesa.set_text(str(8))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 8
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa9(self, widget):
        self.mesa = 9
        self.estado = self.lblmesa9.get_text()
        database.cargarFactura(self.facturas, 9)
        self.lblCMesa.set_text(str(9))
        if self.estado == "No disponible":
            self.mesa = 0
            self.lblFMesa.set_text("Seleccionar mesa")
            self.lblAviso.set_markup("<span color='gray'>Mesa no disponible</span>")
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 9
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    # MÉTODOS RELACIONADOS CON LA GESTIÓN DE LAS VENTANAS:
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
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún camarero</span>")
            else:
                self.venconfirma.show()
        if panel == 2:
            if self.lblProducto.get_text() == "Seleccionar producto":
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún producto</span>")
            else:
                self.venconfirma.show()
        if panel == 3:
            if self.idcliente == "":
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún cliente</span>")
            else:
                self.venconfirma.show()

    def cerrarConfirma(self, widget):
        self.venconfirma.hide()

    def abrirJornada(self, widget):
        self.venjornada.show()

    def cerrarJornada(self, widget):
        self.venjornada.hide()

    def aceptarConfirma(self, widget):
        panel = self.Pestanas.get_current_page()
        if panel == 1:
            self.bajaCamarero(widget)
        if panel == 2:
            self.bajaProducto(widget)
        if panel == 3:
            self.bajaCliente(widget)
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
                self.lblHCamarero.set_text(user)
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
        color2 = Gdk.RGBA()
        color2.parse('#4E4C45')
        color2.to_string()
        self.venprincipal.override_background_color(Gtk.StateFlags.NORMAL, color2)
        self.venprincipal.maximize()

    def color(self):
        colorVerde = Gdk.RGBA()
        colorVerde.parse('#1f451a')
        colorVerde.to_string()
        colorResize = Gdk.RGBA()
        colorResize.parse('#3E3D39')
        colorResize.to_string()
        colorMesas = Gdk.RGBA()
        colorMesas.parse('#F2F1F0')
        colorMesas.to_string()
        self.venprincipal.override_background_color(Gtk.StateFlags.NORMAL, colorResize)
        self.Pestanas.override_background_color(Gtk.StateFlags.NORMAL, colorVerde)
        self.Panel.override_background_color(Gtk.StateFlags.NORMAL, colorMesas)
        self.Home.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        self.Camareros.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        self.Productos.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        self.Facturas.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        self.Mesas.override_background_color(Gtk.StateFlags.NORMAL, colorMesas)
        self.lblAviso.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 0))
        self.LoginTexto3.override_color(Gtk.StateFlags.NORMAL, colorVerde)
        self.LoginTexto1.override_color(Gtk.StateFlags.NORMAL, colorVerde)
        self.LoginTexto2.override_color(Gtk.StateFlags.NORMAL, colorVerde)
        self.HomeHeader.override_background_color(Gtk.StateFlags.NORMAL, colorVerde)
        self.Clientes.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        self.Comandas.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        #self.HomeHeader.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1))
        #self.treeProductos.override_background_color(Gtk.StateFlags.NORMAL, colorVerde)
        #self.scrollProductos.override_background_color(Gtk.StateFlags.NORMAL, colorVerde)


    def salir(self, widget, data=None):
        print("Finalizando el programa")
        Gtk.main_quit()

if __name__ == '__main__':
    main = Main()
    Gtk.main()