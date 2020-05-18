#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import csv
import os
import sys

import django
django.setup()
from administration.models import User


def uploadData():
    with open('fenixusers.csv', newline='', encoding="ISO-8859-1") as csvfile:
        myfile = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in myfile:
            print(row[0])
            _user = User()
            _user.email = row[0]
            _user.athlete_id = row[1]
            _user.name = row[2]
            _user.user_hash = "hash"
            _user.user_role = "Level2"
            _user.password = "12345678"
            _user.created_user = "rafaelmersant@yahoo.com"
            _user.save()


if __name__ == "__main__":
    uploadData()
