#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# reads utf8 on stdin, prints latex on stdout 

import os, os.path, sys, codecs
import latex

# register as a codec
latex.register()

# read encoding names from name of this file
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
from_enc, to_enc = scriptname.split("_to_")

for l in sys.stdin:
    print unicode(l, from_enc).encode(to_enc),
    
