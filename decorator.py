#!/usr/bin/env python

import sys

def execute(fn):
    def wrapper(*args, **kwargs):
        if len(sys.argv) > 1:
            method, params = sys.argv[1], sys.argv[2:]
            module_name = sys.modules[fn.__module__]
            methods = dir(module_name)
            nos_arg = getattr(module_name, methods[methods.index(method)]).__code__.co_argcount
            if method in methods:
                if nos_arg == 0:
                    getattr(module_name, methods[methods.index(method)])()
                elif nos_arg and len(params) > 0:
                    getattr(module_name, methods[methods.index(method)])(params)
                else:
                    print("Paramater miss-match")
            return fn()
    return wrapper