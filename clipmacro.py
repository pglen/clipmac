#!/usr/bin/env python

#pylint: disable=C0103
#pylint: disable=C0209
#pylint: disable=C0321
#pylint: disable=C0116
#pylint: disable=W0301
#pylint: disable=C0410
#pylint: disable=C0411
# pylint: disable=C0413

'''
 This is open source macro feeder. Written in python. The motivation for
 this project was to create macro shortcuts for pasting pre made
 text onto the clipboard.

 The clipmac program functions near identical on
    Linux / Windows / Mac / Raspberry PI

 Redirecting stdout to a fork to real stdout and log. This way
 messages can be seen even if clipmac is started without a
 terminal (from the GUI)

'''

import os, sys, getopt, signal
from clipmac import cliputils
basedir = os.path.dirname(cliputils.__file__)
#print(basedir)
sys.path.append(basedir)

import clipconf
clipconf.basedir = basedir

from clipmac import chrissql
from clipmac import chriswin

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

VERSION = "1.0.0"

# ------------------------------------------------------------------------

def main(strarr):

    if clipconf.conf.verbose:
        print("clipmac running on", "'" + os.name + "'", \
            "GTK", Gtk._version, "PyGtk", \
               "%d.%d.%d" % (Gtk.get_major_version(), \
                    Gtk.get_minor_version(), \
                        Gtk.get_micro_version()))

    signal.signal(signal.SIGTERM, terminate)

    # Initialize sqlite to load / save preferences & other info
    clipconf.conf.sql = chrissql.Pedsql(clipconf.conf.sql_data)

    mainwin =  chriswin.ChrisMainWin(None, None, strarr)
    clipconf.conf.pedwin = mainwin

    Gtk.main()

def helpx():

    #print()
    #print("clipmacro version: ", clipconf.conf.version)
    print("Usage: " + os.path.basename(sys.argv[0]) + " [options]")
    print("Options:  -d level  - Debug level 1-10. (Limited implementation)")
    print("          -v        - Verbose (to stdout and log)")
    print("          -c        - Dump Config")
    print("          -V        - Show version")
    print("          -x        - Clear (eXtinguish) config (will prompt)")
    print("          -h        - Help. (This screen)")
    #print()

def terminate(arg1, arg2):

    if clipconf.conf.verbose:
        print("Terminating clipmac.py, saving files to ~/clipmac")

    # Save all
    clipconf.conf.pedwin.activate_quit(None)
    #return signal.SIG_IGN

def mainfunc():

    opts = []; args = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h?fvxctVo")
    except getopt.GetoptError as err:
        print("Invalid option(s) on command line:", err)
        sys.exit(1)
    #print "opts", opts, "args", args
    clipconf.conf.version = VERSION
    for aa in opts:
        if aa[0] == "-d":
            try:
                clipconf.pgdebug = int(aa[1])
            except:
                clipconf.pgdebug = 0
        if aa[0] == "-h": helpx() ;  sys.exit(1)
        elif aa[0] == "-?": helpx() ;  sys.exit(1)
        elif aa[0] == "-V": print("Version", clipconf.conf.version); \
            sys.exit(1)
        elif aa[0] == "-f": clipconf.conf.full_screen = True
        elif aa[0] == "-v": clipconf.conf.verbose = True
        elif aa[0] == "-x": clipconf.conf.clear_config = True
        elif aa[0] == "-c": clipconf.conf.show_config = True
        elif aa[0] == "-o": clipconf.conf.use_stdout = True
        else:  pass
    try:
        if not os.path.isdir(clipconf.conf.config_dir):
            if clipconf.conf.verbose:
                print("making", clipconf.conf.config_dir)
            os.mkdir(clipconf.conf.config_dir)
    except: pass

    # Let the user know it needs fixin'
    if not os.path.isdir(clipconf.conf.config_dir):
        print("Cannot access config dir:", clipconf.conf.config_dir)
        sys.exit(1)

    if not os.path.isdir(clipconf.conf.data_dir):
        if clipconf.conf.verbose:
            print("making", clipconf.data_dir)
        os.mkdir(clipconf.conf.data_dir)
    if not os.path.isdir(clipconf.conf.log_dir):
        if clipconf.conf.verbose:
            print("making", clipconf.conf.log_dir)
        os.mkdir(clipconf.conf.log_dir)
    if not os.path.isdir(clipconf.conf.macro_dir):
        if clipconf.conf.verbose:
            print("making", clipconf.conf.macro_dir)
        os.mkdir(clipconf.conf.macro_dir)
    if not os.path.isdir(clipconf.conf.sess_data):
        if clipconf.conf.verbose:
            print("making", clipconf.conf.sess_data)
        os.mkdir(clipconf.conf.sess_data)
    #clipconf.conf.keyh = pyedlib.keyhand.KeyHand()
    clipconf.conf.mydir = os.path.abspath(__file__)

    # To clear all config vars
    if clipconf.conf.clear_config:
        print("Are you sure you want to clear config ? (y/n)")
        sys.stdout.flush()
        aa = sys.stdin.readline()
        if aa[0] == "y":
            print("Removing configuration ... ", end=' ')
            # Initialize sqlite to load / save preferences & other info
            clipconf.conf.sql = chrissql.Pedsql(clipconf.conf.sql_data)
            clipconf.conf.sql.rmall()
            print("OK")
        else:
            print("Not deleted.")
        sys.exit(0)

    # To check all config vars
    if clipconf.conf.show_config:
        print("Dumping configuration:")
        # Initialize sqlite to load / save preferences & other info
        clipconf.conf.sql = chrissql.Pedsql(clipconf.conf.sql_data)
        ss = clipconf.conf.sql.getall();
        for aa in ss:
            print(aa)
        sys.exit(0)

    #Uncomment this for silent stdout
    if clipconf.conf.use_stdout:
        #print("Using real stdout")
        sys.stdout = cliputils.Unbuffered(sys.stdout)
        sys.stderr = cliputils.Unbuffered(sys.stderr)
    else:
        pass
        #sys.stdout = pyedlib.log.fake_stdout()
        #sys.stderr = pyedlib.log.fake_stdout()

    # Uncomment this for buffered output
    if clipconf.conf.verbose:
        #print("Started clipmac")
        #pyedlib.log.print("Started clipmac")
        pass

    main(args[0:])

# Start of program:

if __name__ == '__main__':
    mainfunc()

# EOF
