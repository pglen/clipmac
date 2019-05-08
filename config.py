#!/usr/bin/env python

# Global configuration for chrsmac. Also a place we share globals to the rest
# of the project like the main window, statusbar, keyhandler etc ...
# so the functionality is acessable from the key handler
# or the key handler is acessable from the main window ... etc
# The majority of dynamic vars are inited in chrismac.py

from __future__ import absolute_import
import signal, os, time, sys

config_reg = "/apps/chrismac"

class conf():

    IDLE_TIMEOUT = 15           # Time for a backup save
    SYNCIDLE_TIMEOUT = 2        # Time for syncing windows and spelling
    UNTITLED = "untitled.txt"   # New (empty) file name

    full_screen = False
    keyh = None
    pedwin = None

    # Count down variables
    idle = 0; syncidle = 0;   statuscount = 0

    # Where things are stored (backups, orgs, macros, logs)
    config_dir = os.path.expanduser("~/.chrismac")
    macro_dir = os.path.expanduser("~/.chrismac/macros")
    data_dir = os.path.expanduser("~/.chrismac/data")
    log_dir = os.path.expanduser("~/.chrismac/log")
    sql_data = os.path.expanduser("~/.chrismac/sql_data")
    sess_data = os.path.expanduser("~/.chrismac/sess")
    sql = None
    config_file = "defaults"

    # Where things are stored (UI x/y pane pos.)
    config_reg = "/apps/chrismac"
    verbose = False

    def __init__(self):
        pass












