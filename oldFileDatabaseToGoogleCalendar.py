#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Functions.eventsFunctions as ef

birthdays = [""]

for cumple in birthdays:
    ef.birthdayAddFunction(args=cumple.split(":")[1], summary=(cumple.split(":")[0]+'|'+str(cumple.split(":")[2])))

print("Done")
