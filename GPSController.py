#!/usr/bin/env python

from gps import *
import time
import threading
import math
import csv
import cgi
import cgitb
cgitb.enable()


class GpsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #starting the stream of info
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stopController(self):
        self.running = False

    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

def main():
    # create the controller
    gpsc = GpsController()
    try:
        # start controller
        gpsc.start()
        # wait a second for stream to start
        time.sleep(1)
        # print html header
        print "Content-type: text/html\n"
        
        i = 0
        while i < 1:
            print "<p>latitude : %s </p>" % gpsc.fix.latitude
            print "<p>longitude : %s </p>" % gpsc.fix.longitude
            print "<p>time utc : %s </p>" % gpsc.utc
            print "<p>altitude (m) : %s </p>" % gpsc.fix.altitude
            print "<p>speed (m/s) : %s </p>" % gpsc.fix.speed
            #time.sleep(2)
            i = i + 1
            with open('route/test_data.csv', 'a') as route:
                gpswriter = csv.writer(route, delimiter=',')
                gpswriter.writerow([gpsc.fix.latitude, gpsc.fix.longitude])

            route.close()
            with open('altitude/test_data.csv', 'a') as alt:
                gpswriter = csv.writer(alt)
                gpswriter.writerow([gpsc.fix.altitude])

            alt.close()
            with open('speed/test_data.csv', 'a') as speed:
                gpswriter = csv.writer(speed)
                gpswriter.writerow([gpsc.fix.speed])

            speed.close()
            with open('time/test_data.csv', 'a') as t:
                gpswriter = csv.writer(t)
                gpswriter.writerow([gpsc.utc])

            t.close()
        

    #Error
    except():
        print("Unexpected error:", sys.exc_info()[0])
        raise

    except KeyboardInterrupt:
        print "User Cancelled"

    finally:
        gpsc.stopController()
        #wait for the tread to finish
        gpsc.join()

if __name__ == '__main__':
    main()
