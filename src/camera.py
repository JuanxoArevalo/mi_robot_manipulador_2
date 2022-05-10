#!/usr/bin/env python3

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node('VideoPublisher', anonymous=True)
VideoRaw = rospy.Publisher('VideoRaw', Image, queue_size=10)
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while rospy.is_shutdown():      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    frame = cv2.flip(frame, 1)

    msg_frame = CvBridge().cv2_to_imgmsg(frame)

    VideoRaw.publish(msg_frame, "RGB8")