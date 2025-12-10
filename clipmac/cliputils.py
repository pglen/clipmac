#!/usr/bin/env python

# Global configuration for macros. Also a place we share globals to
# the rest of the project like the main window, statusbar, keyhandler
# etc ... so the functionality is acessable from the key handler
# or the key handler is acessable from the main window ... etc
# The majority of dynamic vars are inited in clipmacro.py

import signal, os, time, sys

class Unbuffered(object):

    ''' Stdin / Stdout '''

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

