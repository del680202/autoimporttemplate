#!/usr/bin/env python
# encoding: utf-8

from module import Module

class Dummy(Module):

    def before(self):
        print "prepare something..."

    def execute(self):
        print "Hello world"

    def after(self):
        print "clean something..."
