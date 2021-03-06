#!/usr/bin/env python

"""Setup script for the 'decompyle' distribution."""

____revision__ = "$Id: setup.py,v 1.1.1.1 2004/12/14 12:29:31 dan Exp $"

from distutils.core import setup, Extension

setup (name = "decompyle",
       version = "2.3",
       description = "Python byte-code to source-code converter",
       author = "Hartmut Goebel",
       author_email = "hartmut@oberon.noris.de",
       url = "http://www.goebel-consult.de/decompyle/",
       packages=['decompyle'],
       scripts=['scripts/decompyle'],
       ext_modules = [Extension('decompyle/marshal_25',
                                ['decompyle/marshal_25.c'],
                                define_macros=[]),
                      ]
      )
