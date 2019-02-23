from cafeteria import database


def altaCamareros(self, widget):
    '''Alta de camareros
        Primero pone en mayúsculas las iniciales y recoge los valores en unas variables,
        se comprueba la longitud de las mismas para ver si están vacías o no y se mandan
        los datos al método de registro en la base de datos.
        Por último se resetean los datos.'''
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
        Por último se resetean los datos.'''
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