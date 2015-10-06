#!/usr/bin/env python
# encoding: utf-8

import getopt
import inspect
import os
import sys

module_dir = os.path.dirname( os.path.abspath( __file__ ) ) + "/../modules"
sys.path.append(module_dir)

from module import Module


class Usage(Exception):

    def __init__(self):
        self.value = "main.py -m module_name"

    def __str__(self):
        return self.value


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hm:", ["help", "module="])
    except getopt.error, msg:
        raise Usage()

    module = None
    for option, value in opts:
        if option in ('-h', '--help'):
            raise Usage(msg)
        elif option in ('-m', '--module'):
            module = value
        else:
            raise Usage()

    if module is None: raise Usage()
    module = __import__(module)
    for attr in dir(module):
        attr = getattr(module, attr)
        if inspect.isclass(attr) and issubclass(attr, Module) and attr.__name__ != 'Module':
            obj = attr()
            obj.before()
            obj.execute()
            obj.after()


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception as e:
        print str(e)
