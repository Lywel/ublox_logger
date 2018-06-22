#!/usr/bin/env python2

log = None

import rospy
import time
import json

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus

def logNavSatFix(data):
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
    global log

    s = " ".join([
        str(time.time()),
        str(data.latitude),
        str(data.longitude),
        str(data.status.status)
    ])


    log.write(s + "\n")
    log.flush()

if __name__=='__main__':
    log = open('ros.log', 'w')
    rospy.init_node('ublox_logger')
    rospy.Subscriber('ublox_gps_rover/fix', NavSatFix, logNavSatFix)
    rospy.spin()
