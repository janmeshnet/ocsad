#!/usr/bin/env python

import sys
import os
try: 
	import gi
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk
	
except:
	print "Unable to import GTK3, sorry..."
	sys.exit(1)
import bencode
from os.path import expanduser

class Ocsad:
	def __init__(self):

		self.gladefile = "ocsad.glade"
		builder = Gtk.Builder()
		builder.add_from_file("ocsad.glade")
		builder.get_object("ocsad_main_window").show_all()
		
		g = Gateway();
		g.set_builder(builder);
		g.load_settings_from_disk();

		
		builder.connect_signals(Handler(builder, g))
		
		
		builder.get_object("ocsad_main_window").connect("destroy", Gtk.main_quit)
		
class Handler:
	b = None
	g = None
	def __init__(self, builder, gateway):
		global g
		global b
		b=builder
		g=gateway
	def onDestroy(self, *args):
		Gtk.main_quit()
	def onStartCrawler(self, *args): 
		
		if g.get_settings_ip6addr() == '': 
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Warning! ")
			
			
			dialog.format_secondary_text(
				"You must first go to Settings tab and set Your IPv6 Address to your cjdns interface's address before you can start a crawler thread. "
			)
			dialog.run()
			dialog.destroy()
		else:
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Warning! "
			)
			dialog.format_secondary_text(
				"Feature not implemented. "
			)
			dialog.run()
			dialog.destroy()
		

	def onStartSearch(self, *args): 
		
		if g.get_active_crawler_threads() == 0: 
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Warning! ")
			
			
			dialog.format_secondary_text(
				"You must first go to Crawler tab and start a crawler thread before you can make a search. "
			)
			dialog.run()
			dialog.destroy()
		else:
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Warning! "
			)
			dialog.format_secondary_text(
				"Feature not implemented. "
			)
			dialog.run()
			dialog.destroy()
			
	def onSettingsIp6addrSave(self, *args): 
		newIP=b.get_object("settings_ip6addr").get_text()
		
		home = expanduser("~")
		basedir=os.path.join(home, ".ocsad")
		
			
		with open(os.path.join(basedir,'settings_ip6addr.txt'), 'w') as myfile:
			myfile.write("%s" % newIP)
			
		g.load_settings_from_disk();
		
		if g.get_settings_ip6addr() == newIP: 
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Success! ")
			
			
			dialog.format_secondary_text(
				"Your ip address was saved. "
			)
			dialog.run()
			dialog.destroy()
		else:
			dialog = Gtk.MessageDialog(
				parent=b.get_object("ocsad_main_window") ,
				flags=Gtk.DialogFlags.MODAL,
				type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				message_format="Error! "
			)
			dialog.format_secondary_text(
				"Changes have not been saved. "
			)
			dialog.run()
			dialog.destroy()



class Gateway: 
	builder = ''
	settings_ip6addr = ''
	active_crawler_threads = 0;
		
	def set_builder(self, gtkbuilder):
		global builder	
		self.builder = gtkbuilder
	def get_builder(self):
		return self.builder

	def set_active_crawler_threads(self, value=0):
		global active_crawler_threads	
		self.active_crawler_threads = value
	def get_active_crawler_threads(self):
		return self.active_crawler_threads



		
	def get_settings_ip6addr(self): 
		return self.settings_ip6addr	
		
	def load_settings_from_disk(self):
		global settings_ip6addr
		home = expanduser("~")
		basedir=os.path.join(home, ".ocsad")
		
		if not os.path.isdir(basedir):
			os.makedirs(basedir)
			
			
			
			
			
		if os.path.exists(os.path.join(basedir, "settings_ip6addr.txt")): 
			#settings_ip6addr	
			with open(os.path.join(basedir,'settings_ip6addr.txt'), 'r') as myfile:
				self.settings_ip6addr=myfile.read()
				self.builder.get_object("settings_ip6addr").set_text(self.settings_ip6addr)









if __name__ == "__main__":
	o = Ocsad()
	Gtk.main()
