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
                self.lblError.set_text("El DNI introducido debe ser un DNI valido")
                self.abrirError(widget)
        else:
            self.eDni = True
            self.lblError.set_text("La longitud del DNI debe ser de 9 caracteres")
            self.abrirError(widget)
    except:
        self.eDni = True
        self.lblError.set_text("El DNI introducido debe ser un DNI valido")
        self.abrirError(widget)

def validaPrecio(self, widget):
    precio = self.lblPrecio.get_text()
    try:
        int(precio)
        self.ePrecio = False
    except:
        self.ePrecio = True
        self.lblError.set_text("El precio no es valido")
        self.abrirError(widget)