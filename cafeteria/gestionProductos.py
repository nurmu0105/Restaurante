from cafeteria import database


def altaProducto(self, widget):
    '''Alta de productos
        Primero pone en mayúsculas las iniciales y recoge los valores en unas variables,
        se comprueba la longitud de las mismas para ver si están vacías o no y se mandan
        los datos al método de registro en la base de datos.
        Por último se resetean los datos.
    '''
    self.lblNombre.set_text(self.lblNombre.get_text().title())
    nombre = self.lblNombre.get_text()
    precio = self.lblPrecio.get_text() + " €"
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
    precio = self.lblPrecio.get_text() + " €"
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