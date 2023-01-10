<<<<<<< HEAD:chrismac.py
#!/usr/bin/env python

# ------------------------------------------------------------------------
# This is open source macro feeder. Written in python. The motivation for
# this project was to create macro shortcuts for Chris
#
# This project was derived from pyedit.py
#
# chrismac functions near flawless on Linux / Windows / Mac / Raspberry PI

from __future__ import absolute_import
from __future__ import print_function

import os, sys, getopt, signal
import traceback
import config
import chrissql
import chriswin

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

mainwin = None
show_timing = 0
show_config = 0
clear_config = 0
use_stdout = 0

# ------------------------------------------------------------------------

def main(strarr):

    if(config.conf.verbose):
        print("chrismac running on", "'" + os.name + "'", \
            "GTK", Gtk._version, "PyGtk", \
               "%d.%d.%d" % (Gtk.get_major_version(), \
                    Gtk.get_minor_version(), \
                        Gtk.get_micro_version()))

    signal.signal(signal.SIGTERM, terminate)
    mainwin =  chriswin.ChrisMainWin(None, None, strarr)
    config.conf.pedwin = mainwin

    Gtk.main()

def help():

    print()
    print("chrismac version: ", config.conf.version)
    print("Usage: " + os.path.basename(sys.argv[0]) + " [options] [[filename] ... [filenameN]]")
    print("Options:")
    print("            -d level  - Debug level 1-10. (Limited implementation)")
    print("            -v        - Verbose (to stdout and log)")
    print("            -f        - Start Full screen")
    print("            -c        - Dump Config")
    print("            -o        - Use real stdout (for debug strings)")
    print("            -V        - Show version")
    print("            -x        - Clear (eXtinguish) config (will prompt)")
    print("            -h        - Help")
    print()

# ------------------------------------------------------------------------

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream

   def write(self, data):
       self.stream.write(data)
       self.stream.flush()

   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()

   def __getattr__(self, attr):
       return getattr(self.stream, attr)

def terminate(arg1, arg2):

    if(config.conf.verbose):
        print("Terminating chrismac.py, saving files to ~/chrismac")

    # Save all
    config.conf.pedwin.activate_quit(None)
    #return signal.SIG_IGN

# Start of program:

if __name__ == '__main__':

    # Redirect stdout to a fork to real stdout and log. This way messages can
    # be seen even if chrismac is started without a terminal (from the GUI)

    opts = []; args = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h?fvxctVo")
    except getopt.GetoptError as err:
        print("Invalid option(s) on command line:", err)
        sys.exit(1)

    #print "opts", opts, "args", args

    config.conf.version = 0.70

    for aa in opts:
        if aa[0] == "-d":
            try:
                pgdebug = int(aa[1])
            except:
                pgdebug = 0

        if aa[0] == "-h": help();  exit(1)
        if aa[0] == "-?": help();  exit(1)
        if aa[0] == "-V": print("Version", config.conf.version); \
            exit(1)
        if aa[0] == "-f": config.conf.full_screen = True
        if aa[0] == "-v": config.conf.verbose = True
        if aa[0] == "-x": clear_config = True
        if aa[0] == "-c": show_config = True
        if aa[0] == "-t": show_timing = True
        if aa[0] == "-o": use_stdout = True

    try:
        if not os.path.isdir(config.conf.config_dir):
            if(config.conf.verbose):
                print("making", config.con.config_dir)
            os.mkdir(config.conf.config_dir)
    except: pass

    # Let the user know it needs fixin'
    if not os.path.isdir(config.conf.config_dir):
        print("Cannot access config dir:", config.conf.config_dir)
        sys.exit(1)

    if not os.path.isdir(config.conf.data_dir):
        if(config.conf.verbose):
            print("making", config.con.data_dir)
        os.mkdir(config.conf.data_dir)

    if not os.path.isdir(config.conf.log_dir):
        if(config.conf.verbose):
            print("making", config.conf.log_dir)
        os.mkdir(config.conf.log_dir)

    if not os.path.isdir(config.conf.macro_dir):
        if(config.conf.verbose):
            print("making", config.conf.macro_dir)
        os.mkdir(config.conf.macro_dir)

    if not os.path.isdir(config.conf.sess_data):
        if(config.conf.verbose):
            print("making", config.conf.sess_data)
        os.mkdir(config.conf.sess_data)

    if(config.conf.verbose):
        print("Data stored in ", config.conf.config_dir)

    # Initialize sqlite to load / save preferences & other info
    sql = chrissql.pedsql(config.conf.sql_data)

    # Initialize pedconfig for use
    config.conf.sql = sql
    #config.conf.keyh = pyedlib.keyhand.KeyHand()
    config.conf.mydir = os.path.abspath(__file__)

    # To clear all config vars
    if clear_config:
        print("Are you sure you want to clear config ? (y/n)")
        sys.stdout.flush()
        aa = sys.stdin.readline()
        if aa[0] == "y":
            print("Removing configuration ... ", end=' ')
            sql.rmall()
            print("OK")
        sys.exit(0)

    # To check all config vars
    if show_config:
        print("Dumping configuration:")
        ss = sql.getall();
        for aa in ss:
            print(aa)
        sys.exit(0)

    #Uncomment this for silent stdout
    if use_stdout:
        #print("Using real stdout")
        sys.stdout = Unbuffered(sys.stdout)
        sys.stderr = Unbuffered(sys.stderr)
    else:
        pass
        #sys.stdout = pyedlib.log.fake_stdout()
        #sys.stderr = pyedlib.log.fake_stdout()

    # Uncomment this for buffered output
    if config.conf.verbose:
        print("Started chrismac")
        #pyedlib.log.print("Started chrismac")

    main(args[0:])

# EOF



=======
#!/usr/bin/env python3

# ------------------------------------------------------------------------
# This is open source macro feeder. Written in python. The motivation for
# this project was to create macro shortcuts for Chris
#
# This project was derived from pyedit.py
#
# chrismac functions near flawless on Linux / Windows / Mac / Raspberry PI

from __future__ import absolute_import
from __future__ import print_function

import os, sys, getopt, signal
import traceback
import config
import chrissql
import chriswin

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

mainwin = None
show_timing = 0
show_config = 0
clear_config = 0
use_stdout = 0

# ------------------------------------------------------------------------

def main(strarr):

    if(config.conf.verbose):
        print("chrismac running on", "'" + os.name + "'", \
            "GTK", Gtk._version, "PyGtk", \
               "%d.%d.%d" % (Gtk.get_major_version(), \
                    Gtk.get_minor_version(), \
                        Gtk.get_micro_version()))

    signal.signal(signal.SIGTERM, terminate)
    mainwin =  chriswin.ChrisMainWin(None, None, strarr)
    config.conf.pedwin = mainwin

    Gtk.main()

def help():

    print()
    print("chrismac version: ", config.conf.version)
    print("Usage: " + os.path.basename(sys.argv[0]) + " [options] [[filename] ... [filenameN]]")
    print("Options:")
    print("            -d level  - Debug level 1-10. (Limited implementation)")
    print("            -v        - Verbose (to stdout and log)")
    print("            -f        - Start Full screen")
    print("            -c        - Dump Config")
    print("            -o        - Use real stdout (for debug strings)")
    print("            -V        - Show version")
    print("            -x        - Clear (eXtinguish) config (will prompt)")
    print("            -h        - Help")
    print()

# ------------------------------------------------------------------------

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream

   def write(self, data):
       self.stream.write(data)
       self.stream.flush()

   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()

   def __getattr__(self, attr):
       return getattr(self.stream, attr)

def terminate(arg1, arg2):

    if(config.conf.verbose):
        print("Terminating chrismac.py, saving files to ~/chrismac")

    # Save all
    config.conf.pedwin.activate_quit(None)
    #return signal.SIG_IGN

# Start of program:

if __name__ == '__main__':

    # Redirect stdout to a fork to real stdout and log. This way messages can
    # be seen even if chrismac is started without a terminal (from the GUI)

    opts = []; args = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h?fvxctVo")
    except getopt.GetoptError as err:
        print("Invalid option(s) on command line:", err)
        sys.exit(1)

    #print "opts", opts, "args", args

    config.conf.version = 0.70

    for aa in opts:
        if aa[0] == "-d":
            try:
                pgdebug = int(aa[1])
            except:
                pgdebug = 0

        if aa[0] == "-h": help();  exit(1)
        if aa[0] == "-?": help();  exit(1)
        if aa[0] == "-V": print("Version", config.conf.version); \
            exit(1)
        if aa[0] == "-f": config.conf.full_screen = True
        if aa[0] == "-v": config.conf.verbose = True
        if aa[0] == "-x": clear_config = True
        if aa[0] == "-c": show_config = True
        if aa[0] == "-t": show_timing = True
        if aa[0] == "-o": use_stdout = True

    try:
        if not os.path.isdir(config.conf.config_dir):
            if(config.conf.verbose):
                print("making", config.con.config_dir)
            os.mkdir(config.conf.config_dir)
    except: pass

    # Let the user know it needs fixin'
    if not os.path.isdir(config.conf.config_dir):
        print("Cannot access config dir:", config.conf.config_dir)
        sys.exit(1)

    if not os.path.isdir(config.conf.data_dir):
        if(config.conf.verbose):
            print("making", config.con.data_dir)
        os.mkdir(config.conf.data_dir)

    if not os.path.isdir(config.conf.log_dir):
        if(config.conf.verbose):
            print("making", config.conf.log_dir)
        os.mkdir(config.conf.log_dir)

    if not os.path.isdir(config.conf.macro_dir):
        if(config.conf.verbose):
            print("making", config.conf.macro_dir)
        os.mkdir(config.conf.macro_dir)

    if not os.path.isdir(config.conf.sess_data):
        if(config.conf.verbose):
            print("making", config.conf.sess_data)
        os.mkdir(config.conf.sess_data)

    if(config.conf.verbose):
        print("Data stored in ", config.conf.config_dir)

    # Initialize sqlite to load / save preferences & other info
    sql = chrissql.pedsql(config.conf.sql_data)

    # Initialize pedconfig for use
    config.conf.sql = sql
    #config.conf.keyh = pyedlib.keyhand.KeyHand()
    config.conf.mydir = os.path.abspath(__file__)

    # To clear all config vars
    if clear_config:
        print("Are you sure you want to clear config ? (y/n)")
        sys.stdout.flush()
        aa = sys.stdin.readline()
        if aa[0] == "y":
            print("Removing configuration ... ", end=' ')
            sql.rmall()
            print("OK")
        sys.exit(0)

    # To check all config vars
    if show_config:
        print("Dumping configuration:")
        ss = sql.getall();
        for aa in ss:
            print(aa)
        sys.exit(0)

    #Uncomment this for silent stdout
    if use_stdout:
        #print("Using real stdout")
        sys.stdout = Unbuffered(sys.stdout)
        sys.stderr = Unbuffered(sys.stderr)
    else:
        pass
        #sys.stdout = pyedlib.log.fake_stdout()
        #sys.stderr = pyedlib.log.fake_stdout()

    # Uncomment this for buffered output
    if config.conf.verbose:
        print("Started chrismac")
        #pyedlib.log.print("Started chrismac")

    main(args[0:])

# EOF



>>>>>>> 4652a8ab8eb7ff8baf5955dd08b3a59e11fda41a:clipmac.py
