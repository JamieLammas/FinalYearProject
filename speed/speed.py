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
    speed = pylab.loadtxt('speed.csv')
    
    pylab.title("Speed Graph")
    pylab.plot(speed, 'o-')
    pylab.ylabel("Speed")

    print "Content-type:image/png\n"
    pylab.savefig(sys.stdout, format='png')

make_fig()
