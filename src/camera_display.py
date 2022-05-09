#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image

def callback(data):
        # Display the resulting frame
    cv2.imshow('frame', data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('VideoRaw', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

