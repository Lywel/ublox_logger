#!/usr/bin/env python2

import rospy
import time

from sensor_msgs.msg import NavSatFix

def logNavSatStatus(status):
"""
Doc extract: sensor_msgs/NavSatStatus

# Navigation Satellite fix status for any Global Navigation Satellite System

# Whether to output an augmented fix is determined by both the fix
# type and the last time differential corrections were received.  A
# fix is valid when status >= STATUS_FIX.

int8 STATUS_NO_FIX =  -1        # unable to fix position
int8 STATUS_FIX =      0        # unaugmented fix
int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation
int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation

int8 status
"""
  rospy.loginfo("[STATUS] %s", time.time(),
    status.status)

def logNavSatFix(data):
"""
Doc extract: sensor_msgs/NavSatFix

# satellite fix status information
NavSatStatus status

# Latitude [degrees]. Positive is north of equator; negative is south.
float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is west.
float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid
# (quiet NaN if no altitude is available).
float64 altitude

"""
  rospy.loginfo("[FIX] %f %f %f %f", time.time(),
    data.latitude, data.longitude, data.altitude)

  logNavSatStatus(data.status)

if __name__=='__main__':
  rospy.init_node('ublox_plot')
  rospy.Subscriber('ublox_gps_rover/fix', NavSatFix, logNavSatFix)
  rospy.spin()
