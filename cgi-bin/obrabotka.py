#!/usr/bin/env python3

import cgi
import random

our_form = cgi.FieldStorage()

frstnmbr = int(our_form.getfirst("frstnmbr","0"))
scndnmbr = int(our_form.getfirst("scndnmbr","0"))

a = random.randint(frstnmbr, scndnmbr)

print("Content-type: text/html")
print()
print(a)
