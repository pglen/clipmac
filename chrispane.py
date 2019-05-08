#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function

import signal, os, time, sys, subprocess, platform
import warnings

import gi
#from six.moves import range
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GLib

import config, chrisdlg, chrissql

keystate = 0
shiftstate = 0
altstate = 0

# These can be arbitrary texts ... fill in sensible defaults

barr = [
                "text here 0_1",
                "text here 0_2",
                "text here 0_3",
                "text here 0_4",
                ]

barr2 = [
                "text here 0_5",
                "text here 0_6",
                "text here 0_7",
                "text here 0_8",
                ]
barr3 = [
                "text here 21",
                "text here 22",
                "text here 23",
                "text here 24",
                ]
barr4 = [
                "text here 31",
                "text here 32",
                "text here 33",
                "text here 34",
                ]
barr5 = [
                "text here 41",
                "text here 42",
                "text here 43",
                "text here 44",
                ]
barr6 = [
                "text here 51",
                "text here 52",
                "text here 53",
                "text here 54",
                ]
barr7 = [
                "text here 51",
                "text here 52",
                "text here 53",
                "text here 54",
                ]
barr8 = [
                "text here 61",
                "text here 62",
                "text here 63",
                "text here 64",
                ]
barr9 = [
                "text here 71",
                "text here 72",
                "text here 73",
                "text here 74",
                ]

# -----------------------------------------------------------------------
# Create document

class edPane(Gtk.VPaned):

    def __init__(self, bname = "No Name", focus = False):

        pos = config.conf.sql.get_int("vpaned")
        if pos == 0: pos = 120

        Gtk.VPaned.__init__(self)
        self.set_border_width(3)
        self.set_position(pos)
        self.vbox = buttwin(bname);
        self.add2(self.vbox)
        self.bname = bname
        #self.vbox2 = buttwin(buff, True)
        #self.add1(self.vbox2)

        self.set_size_request(100, 100)

        # Shortcuts to access the editor windows
        self.area  = self.vbox.area
        #self.area2 = self.vbox2.area

    def close_button(self, butt):
        print("Close pressed, deactivated function")
        pass

# -----------------------------------------------------------------------
# Create main document widget with scroll bars

class buttwin(Gtk.VBox):

    def __init__(self, bname, readonly = False):

        global notebook, mained, keystate, shiftstate

        Gtk.VBox.__init__(self)
        self.bname = bname

        # Make it acessable:
        #self.area  = peddoc.pedDoc(buff, mained, readonly)
        self.area = Gtk.Window()
        self.set_spacing(10)

        #print "created", self.area, mained

        # Give access to notebook and main editor window
        #self.area.notebook = notebook
        #self.area.mained = mained
        self.area.fname = ""

        vtext = Gtk.Label(" ")
        self.pack_start(vtext, 0 ,0 , 0)

        bgarr = [
                barr, barr2, barr3, barr4,barr5, barr6, barr7,
                barr8, barr9
                ]

        for bb in bgarr:
            hbox = Gtk.HBox()
            txtb = Gtk.Label("  ")
            hbox.pack_start(txtb, 1 , 0 , 0)

            for aa in bb:
                cc = "    " + self.bname + "  " + aa + "    "
                ccc = config.conf.sql.get(cc);
                if ccc != None:
                    ddd = ccc[0]
                else:
                    ddd = cc
                butt = Gtk.Button.new_with_mnemonic(ddd)
                butt.org  = cc
                butt.connect("clicked", self.butt_press, cc)
                hbox.pack_start(butt, 0 ,0 , 0)
                txt = Gtk.Label("  ")
                hbox.pack_start(txt, 0 ,0 , 0)

            txtc = Gtk.Label("  ")
            hbox.pack_start(txtc, 1 ,0 , 0)

            self.pack_start(hbox, 0 ,0 , 0)


    def butt_press(self, butt, par):

        global keystate,  shiftstate, altstate

        mylab = butt.get_label()
        #print("Butt pressed", mylab, par, "shift",  shiftstate)
        ccc = config.conf.sql.get(par);
        #print ("ccc from database:", ccc)
        if ccc == None:
            ccc = []
            ccc.append("Not configured"); ccc.append("")
            config.conf.pedwin.update_statusbar3("Not configured yet.")
            config.conf.pedwin.update_statusbar(ccc[0])

        if shiftstate:
            bbb, eee = chrisdlg.config_dlg(mylab, ccc[1]);
            if eee != None:
                butt.set_label(bbb)
                config.conf.sql.put(par, bbb, eee);
            shiftstate = False
        else:
            disp2 = Gdk.Display()
            disp = disp2.get_default()
            clip = Gtk.Clipboard.get_default(disp)
            clip.set_text(ccc[1], len(ccc[1]))
            config.conf.pedwin.update_statusbar3("Last Button: '" + mylab + "'")
            ppp = str.split(str(ccc[1]), "\n")
            config.conf.pedwin.update_statusbar("Copied: '" + ppp[0] + "'")

        #, "alt", altstate)

        pass

# EOF
