#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import csv
import os
import sys

import django
django.setup()
from athletes.models import Athlete

def get_month_number(_month):

    if (_month != None):
        if _month.lower() == "enero":
            return "01"
        if _month.lower() == "febrero":
            return "02"
        if _month.lower() == "marzo":
            return "03"
        if _month.lower() == "abril":
            return "04"
        if _month.lower() == "mayo":
            return "05"
        if _month.lower() == "junio":
            return "06"
        if _month.lower() == "julio":
            return "07"
        if _month.lower() == "agosto":
            return "08"
        if _month.lower() == "septiembre":
            return "09"
        if _month.lower() == "octubre":
            return "10"
        if _month.lower() == "noviembre":
            return "11"
        if _month.lower() == "diciembre":
            return "12"

    return ""


def birthdate_formatted(year, month, day):
    if year != None and month != None and day != None:
        if len(year) == 4 and len(month) >= 1 and len(day) >= 1:
            return f'{year}-{month}-{day}'


def uploadData():
    with open('FenixFullClean.csv', newline='', encoding="ISO-8859-1") as csvfile:
        myfile = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in myfile:
            print(row[0])
            athlete = Athlete()
            athlete.category = row[0]
            athlete.enrollment_year = row[1] if len(row[1]) > 0 else 0
            athlete.enrollment_month = get_month_number(row[2]) if len(row[2]) > 0 else 0
            athlete.first_name = row[3]
            athlete.last_name = row[4]
            athlete.birthday = birthdate_formatted(row[6],row[7],row[8])
            athlete.email = row[9]
            athlete.phone_number = row[10]
            athlete.created_user = 'rafaelmersant@yahoo.com'
            athlete.save()


if __name__ == "__main__":
    uploadData()
