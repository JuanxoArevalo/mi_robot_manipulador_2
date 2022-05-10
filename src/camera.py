#!/usr/bin/env python3

from configparser import Interpolation
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0)
print(cap.isOpened())
bridge = CvBridge()

def talker():
    pub = rospy.Publisher('/vision', Image, queue_size=1)
    rospy.init_node('camera', anonymous=False)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        frame_small = cv2.resize(frame, (480,480), fx=0,fy=0,interpolation=cv2.INTER_CUBIC())
        if not ret:
            break
        msg = bridge.cv2_to_imgmsg(frame_small, "bgr8")
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if rospy.is_shutdown():
            cap.release()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
