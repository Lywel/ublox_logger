#!/usr/bin/env python2

import rospy

from sensor_msgs.msg import NavSatFix

def gpslogger(data):
  global init
  rospy.loginfo("lat %s", data.latitude)
  rospy.loginfo("lon %s", data.longitude)

if __name__=='__main__':
  rospy.init_node('ublox_plot')
  rospy.Subscriber('ublox_gps_rover/fix', NavSatFix, gpslogger)
  rospy.spin()
