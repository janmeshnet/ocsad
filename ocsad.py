#!/usr/bin/env python

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#import gtk.glade
#except:
#sys.exit(1)


class Ocsad:
	def __init__(self):

#Set the Glade file
		self.gladefile = "ocsad.glade"
#builder = gtk.glade.XML(self.gladefile, "ocsad_main_window")
		builder = Gtk.Builder()
		builder.add_from_file("ocsad.glade")
		builder.get_object("ocsad_main_window").show_all()
        # builder.connect_signals()
		builder.connect_signals(Handler())

		
#	self.window = self.wTree.get_widget("MainWindow")
#	if (self.window):
#		self.window.connect("destroy", gtk.main_quit)


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

if __name__ == "__main__":
	o = Ocsad()
	Gtk.main()
