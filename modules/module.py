#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod


class Module(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def before(self): pass

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def after(self): pass
