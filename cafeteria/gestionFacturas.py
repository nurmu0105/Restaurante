from cafeteria import database, validaciones


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
        validaciones.validaDNI(self, widget)
        if self.eDni == False:
            fila = (dni, apellido, nombre, comunidad, provincia, ciudad)
            database.altaCliente(fila, self.clientes)
            self.limpiarCli(widget)
            self.lblAviso.set_markup("<span color='white'>Alta de cliente completada con éxito</span>")
    else:
        self.lblError.set_text("Debe cubrir todos los campos")
        self.abrirError(widget)


def bajaCliente(self, widget):
    '''Baja de clientes
        Se envia el dni del cliente seleccionado al método de gestión de la base de datos encargado del
        borrado de clientes y se limpian los campos necesarios'''
    dni = self.idcliente
    database.bajaCliente(dni, self.clientes)
    self.limpiarCli(widget)
    self.lblAviso.set_markup("<span color='white'>Baja de cliente completada con éxito</span>")


def ocuparMesa(self, widget):
    '''OCupar mesas
        En primer lugar se comprueba si se ha seleccionado un cliente y una mesa disponible, se llama al método
        para cambiar el estado de la mesa a No Disponible y se recarga el panel para mostrar el nuevo estado.
        Se da de alta la factura en la base de datos, se limpian los campos utilizados y se setean los datos
        en el panel Gestión de comandas para dejarlo preparado para el alta de lineas de venta'''
    if self.idcliente != '' and self.mesa != 0:
        #Cambiar el estado de la mesa
        database.ocuparMesa("No disponible", self.lblFMesa.get_text())
        self.cargaMesas()
        #Alta de factura
        fila = (self.idcliente, self.lblHCamarero.get_text(), self.mesa, self.lblHFecha.get_text(), "NO")
        database.altaFactura(fila)
        #Limpiar los campos:
        self.lblCMesa.set_text(str(self.mesa))
        self.idcliente = ""
        self.mesa = 0
        #Cargar datos en el panel comandas:
        factura = database.buscaFactura(str(self.lblCMesa.get_text()))
        database.cargarFactura(self.facturas, 0)
        self.lblCFactura.set_text(str(factura))
        self.Pestanas.set_current_page(4)
    else:
        self.lblError.set_text("Debe seleccionar un cliente y una mesa disponible del panel lateral")
        self.abrirError(widget)


def gestionComandas(self, widget):
    '''Añadir líneas de venta a una factura
        Comprueba si hay una factura seleccionada, en caso afirmativo añade lineas de venta a la factura siempre
        que se haya seleccionado un producto'''
    if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
        if self.servicio != "":
            database.altaLinea(self.lblCFactura.get_text(), self.comandas, self.servicio)
            self.servicio = ""
        else:
            self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ningún producto</span>")
    else:
        self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")


def eliminarComandas(self, widget):
    '''Eliminar línea de ventas de una factura
        Comprueba si hay una factura seleccionada y en caso afirmativo elimina la línea de venta'''
    if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
        database.bajaLinea(self.lblCFactura.get_text(), self.comandas, self.servicio)
    else:
        self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")


def cancelarComanda(self, widget):
    '''Cancelar comanda: Baja de factura
        Comprueba si hay una mesa ocupada seleccionada, llama al método encargado de comprobar si hay líneas de venta
        asociadas a la mesa seleccionada. En caso negativo, elimina la factura'''
    if self.lblCFactura.get_text() != "Seleccione una mesa ocupada":
        vacio = database.bajaFactura(self.lblCFactura.get_text(), self.facturas)
        if (vacio == True):
            database.ocuparMesa("Disponible", self.lblCMesa.get_text())
            self.cargaMesas()
            self.lblCFactura.set_text("Seleccione una mesa ocupada")
            self.lblAviso.set_markup("<span color='white'>Factura cancelada con éxito</span>")
            self.Pestanas.set_current_page(0)
        else:
            self.lblError.set_text("No se puede borrar una factura con productos asociados")
            self.abrirError(widget)
            self.lblAviso.set_text("")
    else:
        self.lblAviso.set_markup("<span color='white'>No se ha seleccionado ninguna mesa ocupada</span>")


#def aceptarComanda(self, widget):
 #   '''Aceptar comanda
  #      Llama al método encargado de resetear la TreeView de vencomandas
   #     Llama al método de actualizar el estado de la mesa para que aparezca como no disponible
    #    Llama al método de cargar el TreeView de facturas de la ventana principal
     #   Llama al método de cargar los labels del panel de gestión de las mesas'''
#    database.limpiarComandas(self.comandas)
 #   database.ocuparMesa("No disponible", self.lblFMesa.get_text())
  #  database.cargarFactura(self.facturas, self.lblFMesa.get_text())
   # self.cargaMesas()
    #self.lblFCliente.set_text("Seleccionar cliente")
    #self.lblFMesa.set_text("Seleccionar mesa")
    #self.inicializarCalendario()
    #self.lblAviso.set_markup("<span color='white'>Alta de factura completada con éxito</span>")