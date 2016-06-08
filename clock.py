#!/usr/bin/python
import os, time
from gps import *
from tzwhere import tzwhere
from Adafruit_LED_Backpack import SevenSegment

gpsd= gps(mode = WATCH_ENABLE)
print "Acquiring gps fix..."
while gpsd.fix.mode != MODE_3D:
    gpsd.next()
    time.sleep(1)

tz = tzwhere.tzwhere()
tzname = tz.tzNameAt(gpsd.fix.latitude, gpsd.fix.longitude)
print "Setting timezone to " + tzname

os.environ['TZ'] = tzname
time.tzset()

# Create display instance on default I2C address (0x70) and bus number.                                                                                                                                                                                                       
display = SevenSegment.SevenSegment(busnum=2)
display.begin()
while True:
    localtime = time.localtime(time.time())
    timestr = time.strftime('%I') + time.strftime('%M')
    display.clear()
    display.set_colon(localtime[5] % 2)
    display.print_number_str(timestr)
    display.write_display()
