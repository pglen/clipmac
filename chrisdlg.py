#!/usr/bin/env python


# Action Handler for find

from __future__ import absolute_import
from __future__ import print_function

import re, string, warnings, sys

import gi
#from six.moves import range
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject

def find_keypress():
    pass


def  config_dlg(head, parent = None):

    dialog = Gtk.Dialog(head,
                   None,
                   Gtk.DialogFlags.MODAL | \
                   Gtk.DialogFlags.DESTROY_WITH_PARENT,
                   (Gtk.STOCK_CANCEL, Gtk.ResponseType.REJECT,
                    Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT))
    dialog.set_default_response(Gtk.ResponseType.ACCEPT)
    #dialog.set_transient_for(self2.mained.mywin)
    dialog.set_position(Gtk.WindowPosition.CENTER)
    try:
        dialog.set_icon_from_file(get_img_path("pyedpro_sub.png"))
    except:
        print("Cannot load find dialog icon", sys.exc_info())

    #self.dialog = dialog

    # Spacers
    label1 = Gtk.Label("   ");  label2 = Gtk.Label("   ")
    label3 = Gtk.Label("   ");  label4 = Gtk.Label("   ")
    label5 = Gtk.Label("   ");  label6 = Gtk.Label("   ")
    label7 = Gtk.Label("   ");  label8 = Gtk.Label("   ")

    entry = Gtk.Entry();
    myentry = entry

    entry.set_activates_default(True)

    dialog.vbox.pack_start(label4, 0, 0, 0)

    hbox2 = Gtk.HBox()
    hbox2.pack_start(label6, 0, 0, 0)
    hbox2.pack_start(entry, True, True, 0)
    hbox2.pack_start(label7, 0, 0, 0)

    dialog.vbox.pack_start(hbox2, 0, 0, 0)

    dialog.checkbox = Gtk.CheckButton.new_with_mnemonic("Use _regular expression")
    dialog.checkbox2 = Gtk.CheckButton.new_with_mnemonic("Case In_sensitive")

    #dialog.checkbox.set_active(pedconfig.conf.sql.get_int("regex"))
    #dialog.checkbox2.set_active(pedconfig.conf.sql.get_int("nocase"))

    dialog.vbox.pack_start(label5, 0, 0, 0)

    hbox = Gtk.HBox()
    hbox.pack_start(label1, 0, 0, 0)
    hbox.pack_start(dialog.checkbox, 0, 0, 0)
    hbox.pack_start(label2, 0, 0, 0)
    hbox.pack_start(dialog.checkbox2, 0, 0, 0)
    hbox.pack_start(label3, 0, 0, 0)
    dialog.vbox.pack_start(hbox, 0, 0, 0)
    dialog.vbox.pack_start(label8, 0, 0, 0)

    label30 = Gtk.Label("   ");  label31 = Gtk.Label("   ")
    label32 = Gtk.Label("   ");  label33 = Gtk.Label("   ")
    label34 = Gtk.Label("   ");  label35 = Gtk.Label("   ")

    dialog.checkbox3 = Gtk.CheckButton.new_with_mnemonic("Search _All Buffers")
    #dialog.checkbox4 = Gtk.CheckButton("Hello")
    hbox4 = Gtk.HBox()
    hbox4.pack_start(label30, 0, 0, 0);
    hbox4.pack_start(dialog.checkbox3, 0, 0, 0)
    #hbox4.pack_start(label31, 0, 0, 0);
    #hbox4.pack_start(dialog.checkbox4, 0, 0, 0)
    hbox4.pack_start(label32, 0, 0, 0);
    dialog.vbox.pack_start(hbox4, 0, 0, 0)
    dialog.vbox.pack_start(label33, 0, 0, 0)

    dialog.connect("key-press-event", find_keypress)

    dialog.show_all()
    response = dialog.run()


