#!/usr/bin/env python

from gps import *
import time
import threading
import math
import csv
import cgi
import cgitb
cgitb.enable()

def write(altitude):
    with open('altitude/altitude.csv', 'a') as alt:
        gpswriter = csv.writer(alt)
        gpswriter.writerow([gpsc.fix.altitude])
