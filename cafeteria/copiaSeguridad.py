import zipfile
import os
import getpass
import datetime



def creaCopia(self):
	'''Generar copia de seguridad
		Crea una copia de seguridad de la base de datos y guarda la carpeta backups
		dentro de la carpeta personal del usuario'''
	db = 'Restaurante'
	fecha = datetime.datetime.now()
	if not os.path.exists('/home/' + getpass.getuser() + '/backups'):
		os.mkdir('/home/' + getpass.getuser() + '/backups', mode=0o777, dir_fd=None)
	fichzip = zipfile.ZipFile('/home/' + getpass.getuser() + '/backups/' + str(fecha) + "_backup_" + db + "GreenSide.zip", 'w')
	dir = os.getcwd()
	fichzip.write(db, dir, zipfile.ZIP_DEFLATED)
	fichzip.close()
	print('Copia de seguridad realizada con éxito')
	self.lblAviso.set_markup("<span color='white'>Copia de seguridad realizada con éxito</span>")