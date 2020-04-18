#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import django
django.setup()
import sys, os, csv
from athletes.models import *

with open('fenixmasters.csv', newline='', encoding="ISO-8859-1") as csvfile:
    myfile = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in myfile:
        print(row[0])
        athlete = Athlete()
        athlete.first_name = row[0]
        athlete.last_name = row[1]
        athlete.birthday = '2010-01-01' #row[2]
        athlete.enrollment_year = 0
        athlete.enrollment_month = 0
        athlete.created_user = 'rafaelmersant@yahoo.com'
        athlete.save()

