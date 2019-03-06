import datetime

import gi
from gi.overrides import Gdk

from cafeteria import impresionPDF, colorInterfaz, validaciones, gestionCamareros, gestionProductos, gestionFacturas, \
    copiaSeguridad

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
        self.ComandasHeader = b.get_object("ComandasHeader")
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
        self.lblPagina = b.get_object("lblPagina")
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
               'on_btnCopiaSeguridad_activate':self.creaCopia,
               'on_btnMenuDia_activate':self.imprimirMenu,
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
               'on_addLinea_clicked':self.gestionComandas,
               'on_deleteLinea_clicked':self.eliminarComandas,
               'on_cancelComanda_clicked':self.cancelarComanda,
               'on_cleanFactura_clicked': self.limpiarFact,
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
#        database.generarMenuDia()
        self.cargarComunidades()
        self.cargaMesas()
        self.inicializarCalendario()

        # Colorea la aplicacion
        colorInterfaz.color(self)


    # Cerrar ventanas:
        self.venprincipal.connect('delete-event', lambda w, e: w.hide() or True)
        self.venacerca.connect('delete-event', lambda w, e: w.hide() or True)
        self.venerror.connect('delete-event', lambda w, e: w.hide() or True)
        self.venconfirma.connect('delete-event', lambda w, e: w.hide() or True)
        self.venlogin.connect('delete-event', lambda w, e: w.hide() or True)
        self.venjornada.connect('delete-event', lambda w, e: w.hide() or True)

    # METODOS DE SELECCION PARA LOS TREEVIEW
    def seleccionaCamarero(self, widget):
        '''Rellena los campos en la pestana de Camareros cuando se selecciona el TreeView correspondiente'''
        model, iter = self.treeCamareros.get_selection().get_selected()
        if iter != None:
            self.lblCamarero.set_text(str(model.get_value(iter, 0)))
            self.inputNombre.set_text(model.get_value(iter, 1))
            self.password = database.buscaPWD(self.lblCamarero.get_text())
            self.inputPassword.set_text("**********")

    def seleccionaProducto(self, widget):
        '''Rellena los campos de la pestana Productos cuando se selecciona el elemento en el TreeView'''
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
        '''Recoge los datos del elemento seleccionado en el TreeView de la pestana Facturas'''
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
            self.clienteDNI.set_text(str(model.get_value(iter,0)))
            self.clienteNombre.set_text(str(model.get_value(iter,1)))
            self.clienteApellido.set_text(str(model.get_value(iter,2)))

    # METODOS RELACIONADOS CON LA GESTION DE CAMAREROS
    def altaCamarero(self, widget):
        gestionCamareros.altaCamareros(self, widget)

    def modificaCamarero(self, widget):
        gestionCamareros.modificaCamarero(self,widget)

    def bajaCamarero(self, widget):
        gestionCamareros.bajaCamarero(self, widget)


    # METODOS RELACIONADOS CON LA GESTION DE PRODUCTOS
    def altaProducto(self, widget):
        gestionProductos.altaProducto(self, widget)

    def modificaProducto(self, widget):
        gestionProductos.modificaProducto(self,widget)

    def bajaProducto(self, widget):
        gestionProductos.bajaProducto(self, widget)

    # METODOS RELACIONADOS CON LA GESTION DE FACTURAS + LINEASFACTURAS
    def altaCliente(self, widget):
        gestionFacturas.altaCliente(self, widget)

    def bajaCliente(self, widget):
        gestionFacturas.bajaCliente(self, widget)

    def ocuparMesa(self, widget):
        gestionFacturas.ocuparMesa(self, widget)

    def gestionComandas(self, widget):
        gestionFacturas.gestionComandas(self, widget)

    def eliminarComandas(self, widget):
        gestionFacturas.eliminarComandas(self, widget)

    def cancelarComanda(self, widget):
        gestionFacturas.cancelarComanda(self,widget)

    def imprimeFactura(self, widget):
        '''Imprimir factura
            Comprueba que hay una factura seleccionada y que no pertenece al cliente anonimo,
            llama al metodo para cambiar el estado de la mesa a Disponible,
            llama al metodo encargado de generar el pdf con la factura,
            llama al metodo encargado de cambiar el estado de la factura a pagado'''
        if self.idFactura != "":
            if self.clienteFactura != "00000000T":
                database.ocuparMesa("Disponible", self.idMesa)
                self.cargaMesas()
                impresionPDF.imprimirFactura(self.idFactura, self.fechaFactura, self.clienteFactura)
                database.cobraFactura(self.idFactura, self.facturas)
                #Limpiar campos:
                self.idFactura = ""
                self.lblAviso.set_text("")
            else:
                self.lblError.set_text("No se puede generar una factura para un cliente anonimo")
                self.abrirError(widget)
                self.lblAviso.set_text("")
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna factura</span>")

    def imprimeRecibo(self, widget):
        '''Imprimir recibo
            Comprueba que hay una factura o mesa ocupada seleccionada,
            llama al metodo para cambiar el estado de la mesa a Disponible,
            llama al metodo encargado de generar el pdf con el recibo,
            llama al metodo encargado de cambiar el estado de la factura a pagado'''
        if self.idFactura != "" or self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
            if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
                self.idFactura = self.lblCFactura.get_text()
                self.idMesa = self.lblCMesa.get_text()
            database.ocuparMesa("Disponible", self.idMesa)
            self.cargaMesas()
            impresionPDF.imprimirRecibo(self.idFactura)
            database.cobraFactura(self.idFactura, self.facturas)
            #Limpiar campos:
            self.idFactura = ""
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.lblAviso.set_text("")
            self.comandas.clear()
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")

    # METODOS AUXILIARES:
    def mayus(self, widget, date = None):
        ''' Pone las iniciales y la letra del DNI en mayusculas '''
        self.inputNombre.set_text(self.inputNombre.get_text().title())
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        self.lblNombre.set_text(self.lblNombre.get_text().title())
        self.clienteDNI.set_text(self.clienteDNI.get_text().upper())
        self.clienteNombre.set_text(self.clienteNombre.get_text().title())
        self.clienteApellido.set_text(self.clienteApellido.get_text().title())

    def limpiarCam(self, widget):
        ''' Resetea todos los atributos de la pestana Camareros '''
        self.lblCamarero.set_text("Seleccionar camarero")
        self.inputNombre.set_text("")
        self.inputPassword.set_text("")
        self.lblAviso.set_text("")

    def limpiarProd(self, widget):
        ''' Resetea todos los atributos de la pestana Productos '''
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
        ''' Resetea todos los atributos y variables recurso de la pestana Facturas '''
        self. lblFMesa.set_text("Seleccionar mesa")
        database.cargarFactura(self.facturas, 0) #Recarga el treeView para que muestre todas las facturas registradas
        self.mesa = ""
        self.servicio = ""
        self.comunidad = ""
        self.provincia = ""
        self.ciudad = ""
        self.inputFCliente.set_text("")
        self.lblAviso.set_text("")

    def inicializarCalendario(self):
        '''Inicializar el calendario
            Pone la fecha actual en la pestana de Home para que el resto de la aplicacion
            pueda utilizarla en las gestiones necesarias'''
        dia = datetime.datetime.now().strftime("%d")
        mes = datetime.datetime.now().strftime("%m")
        ano = datetime.datetime.now().strftime("%Y")
        mes = int(mes) - 1
        self.fecha = "%s/" % dia + "%s/" % (mes + 1) + "%s" % ano
        self.lblHFecha.set_text(self.fecha)

    def cargarComunidades(self):
        '''Carga la lista de comunidades'''
        lista = database.cargaComunidad()
        for name in lista:
            self.clienteComu.append_text(name[0])

    def actualizarProvincias(self, widget):
        '''Actualiza la lista de provincias
            Recoge el evento de seleccion en la lista de comunidades y llama al metodo de cargar la combo'''
        self.comunidad = str(self.clienteComu.get_active_text())
        self.cargarProvincias(widget)

    def cargarProvincias(self, widget):
        '''Carga la lista de provincias'''
        self.clienteProv.remove_all()
        lista = database.cargaProvincias(self.comunidad)
        for name in lista:
            self.clienteProv.append_text(name[0])

    def actualizarMunicipios(self, widget):
        '''Actualiza la lista de municipios
            Recoge el evento de seleccion en la lista de provincias y llama al metodo de cargar la combo'''
        self.provincia = str(self.clienteProv.get_active_text())
        self.cargarMunicipios(widget)

    def cargarMunicipios(self, widget):
        '''Carga la lista de municipios o ciudades'''
        self.clienteCiu.remove_all()
        lista = database.cargaMunicipios(self.provincia)
        for name in lista:
            self.clienteCiu.append_text(name[0])

    def seleccionarCategoria(self, widget):
        '''Seleccionar categoria de productos
            Recoge el evento de los radiobutton relacionados con las categorias de los productos en la
            pestana Gestion de Productos y guarda en una variable la opcion seleccionada por el usuario'''
        if self.categoria1.get_active():
            self.categoria = 'Entrante'
        if self.categoria2.get_active():
            self.categoria = 'Plato'
        if self.categoria3.get_active():
            self.categoria = 'Postre'
        if self.categoria4.get_active():
            self.categoria = 'Otro'

    def terminarJornada(self, widget):
        '''Finalizar la jornada
            Comprueba si la contrasena introducida corresponde al camarero que ha iniciado sesion,
            recorre la lista de mesas que hay cambiando el estado de cada una de ellas a Disponible,
            por ultimo recarga el panel lateral de las mesas y cierra la ventana generada'''
        user = self.lblHCamarero.get_text()
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
                print('Mesas liberadas con exito')
                self.cerrarJornada(widget)
            else:
                self.lblError.set_text("Password no valida")
                self.abrirError(widget)
        else:
            self.lblError.set_text("Debe introducir su password")
            self.abrirError(widget)

    def buscaFactura(self, widget):
        '''Buscar factura
            Comprueba la longitud del dni introducido por el usuario,
            lo busca en la base de datos y si lo encuentra carga las facturas asociadas a ese dni'''
        dni = self.inputFCliente.get_text()
        if len(dni) == 9:
            encontrado = database.cargarFactura2(self.facturas, dni)
            if encontrado == False:
                self.lblError.set_text("No se ha encontrado ningun cliente con ese DNI")
                self.abrirError(widget)
                database.cargarFactura(self.facturas, 0)
        else:
            self.lblError.set_text("La longitud del DNI debe ser de 9 caracteres")
            self.abrirError(widget)


    # METODOS RELACIONADOS CON LA GESTION DEL PANEL MESAS:
    def cargaMesas(self):
        '''Cargar el panel lateral de las mesas
            Obtiene un listado con los datos de las mesas de la base de datos,
            cambia el estado a Disponible/No disponible de las etiquetas de cada mesa'''
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa1.get_text()
        database.cargarFactura(self.facturas, 1)
        self.lblCMesa.set_text(str(1))
        self.lblFMesa.set_text(str(1))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
            factura = database.buscaFactura(str(self.lblCMesa.get_text()))
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 1
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def mesa2(self, widget):
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestaNa,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa2.get_text()
        database.cargarFactura(self.facturas, 2)
        self.lblCMesa.set_text(str(2))
        self.lblFMesa.set_text(str(2))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestaNa,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa3.get_text()
        database.cargarFactura(self.facturas, 3)
        self.lblCMesa.set_text(str(3))
        self.lblFMesa.set_text(str(3))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestaNa,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa4.get_text()
        database.cargarFactura(self.facturas, 4)
        self.lblCMesa.set_text(str(4))
        self.lblFMesa.set_text(str(4))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa5.get_text()
        database.cargarFactura(self.facturas, 5)
        self.lblCMesa.set_text(str(5))
        self.lblFMesa.set_text(str(5))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa6.get_text()
        database.cargarFactura(self.facturas, 6)
        self.lblCMesa.set_text(str(6))
        self.lblFMesa.set_text(str(6))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa7.get_text()
        database.cargarFactura(self.facturas, 7)
        self.lblCMesa.set_text(str(7))
        self.lblFMesa.set_text(str(7))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.estado = self.lblmesa8.get_text()
        database.cargarFactura(self.facturas, 8)
        self.lblCMesa.set_text(str(8))
        self.lblFMesa.set_text(str(8))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
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
        '''Seleccion de la mesa
            Recoge el estado de la mesa y llama al metodo encargado de cambiar de pestana,
            carga las facturas asociadas con esa mesa,
            si la mesa esta disponible limpia el treeview de comandas y avisa de que la mesa no esta ocupada,
            si la mesa esta ocupada carga las lineas de ventas en el treeview de comandas'''
        self.mesa = 9
        self.estado = self.lblmesa9.get_text()
        database.cargarFactura(self.facturas, 9)
        self.lblCMesa.set_text(str(9))
        self.lblFMesa.set_text(str(9))
        self.seleccionarPanel()
        if self.estado == "No disponible":
            self.mesa = 0
            factura = database.buscaFactura(self.lblCMesa.get_text())
            self.lblCFactura.set_text(str(factura))
            database.cargarComanda(self.lblCFactura.get_text(), self.comandas)
        else:
            self.mesa = 9
            self.lblFMesa.set_text(str(self.mesa))
            self.lblAviso.set_text("")
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.comandas.clear()

    def seleccionarPanel(self):
        '''Cambiar de pestana al clickar una mesa
            Comprueba que la pestana actual no sea la pestana Gestion de Facturas,
            si la mesa esta disponible cambia a la pestana para sentar al cliente,
            si la mesa esta ocupada cambia a la pestana Gestion de comandas'''
        panel = self.Pestanas.get_current_page()
        if panel != 5:
            if self.estado == "No disponible":
                self.Pestanas.set_current_page(4)
            else:
                self.Pestanas.set_current_page(3)

    # METODOS RELACIONADOS CON LA GESTION DE LAS VENTANAS:
    def abrirAbout(self, widget):
        self.venacerca.show()

    def cerrarAbout(self, widget):
        self.venacerca.hide()

    def abrirError(self, widget):
        self.venerror.show();

    def cerrarError(self, widget):
        self.venerror.hide()
        self.lblError.set_text("")

    def abrirConfirma(self,widget):
        '''Abrir ventana confirmaciones
            Comprueba el panel actual y segun el resultado obtenido muestra un mensaje de error distinto
            o abre la ventana'''
        panel = self.Pestanas.get_current_page()
        if panel == 1:
            if self.lblCamarero.get_text() == "Seleccionar camarero":
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningun camarero</span>")
            else:
                self.venconfirma.show()
        if panel == 2:
            if self.lblProducto.get_text() == "Seleccionar producto":
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningun producto</span>")
            else:
                self.venconfirma.show()
        if panel == 3:
            if self.idcliente == "":
                self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningun cliente</span>")
            else:
                self.venconfirma.show()

    def cerrarConfirma(self, widget):
        self.venconfirma.hide()

    def abrirJornada(self, widget):
        self.venjornada.show()

    def cerrarJornada(self, widget):
        self.venjornada.hide()

    def aceptarConfirma(self, widget):
        '''Confirmar borrado
            Segun el panel actual de la aplicacion llama a un metodo de borrado o a otro'''
        panel = self.Pestanas.get_current_page()
        if panel == 1:
            self.bajaCamarero(widget)
        if panel == 2:
            self.bajaProducto(widget)
        if panel == 3:
            self.bajaCliente(widget)
        self.venconfirma.hide()

    def login(self, widget, data = None):
        '''Inicio de sesion
            Recoge los datos introducidos por el usuario y llama al metodo necesario
            para buscar en la base de datos, si el resultado de la busqueda es
            distinto a None inicia sesion abriendo la aplicaicon'''
        user = self.loginUser.get_text()
        password = self.loginPwd.get_text()
        if len(user) > 0 and  len(password):
            fila = database.login(user, password)
            if str(fila[0]) != 'None' and str(fila[1]) != 'None':
                self.venlogin.hide()
                self.venprincipal.show()
                print("Iniciando sesion")
                self.lblHCamarero.set_text(user)
            else:
                self.lblError.set_text("Usuario o password no encontrado")
                self.abrirError(widget)
                print("Error en el inicio de sesion")
        else:
            self.lblError.set_text("Debe cubrir todos los campos")
            self.abrirError(widget)

    def logout(self, widget):
        '''Cerrar sesion
            Limpia las variables, cierra la ventana principal y abre la ventana de login'''
        self.loginUser.set_text("")
        self.loginPwd.set_text("")
        print("Cerrando sesion")
        self.venprincipal.hide()
        self.venlogin.show()

    def imprimirMenu(self, widget):
        impresionPDF.imprimirMenu()

    def maximizarVentana(self, widget):
        color2 = Gdk.RGBA()
        color2.parse('#4E4C45')
        color2.to_string()
        self.venprincipal.override_background_color(Gtk.StateFlags.NORMAL, color2)
        self.venprincipal.maximize()

    def creaCopia(self, widget):
        copiaSeguridad.creaCopia(self)

    def salir(self, widget, data=None):
        print("Finalizando el programa")
        Gtk.main_quit()

if __name__ == '__main__':
    main = Main()
    Gtk.main()