import gi
from gi.overrides import Gdk
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

def color(self):
    # Declaración de los colores:
    colorVerde = Gdk.RGBA()
    colorVerde.parse('#1f451a')
    colorVerde.to_string()
    colorResize = Gdk.RGBA()
    colorResize.parse('#3E3D39')
    colorResize.to_string()
    colorMesas = Gdk.RGBA()
    colorMesas.parse('#F2F1F0')
    colorMesas.to_string()

    # Setea los colores:
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
    self.ComandasHeader.override_background_color(Gtk.StateFlags.NORMAL, colorVerde)