#!/usr/bin/env python

import os, sys
import cgi
import cgitb
cgitb.enable()
import csv
import matplotlib
matplotlib.use('Agg')
import pylab

def make_fig():
    altitude = pylab.loadtxt('altitude.csv')
    #time = pylab.loadtxt('../altitude/altitude.csv')
    
    pylab.title("Altitude Graph")
    pylab.plot(altitude)
    pylab.ylabel("Altitude (M)")

    print "Content-type:image/png\n"
    pylab.savefig(sys.stdout, format='png')

make_fig()
