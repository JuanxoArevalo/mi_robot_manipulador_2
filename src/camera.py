#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pickle
import os

cap = cv2.VideoCapture(2)
print(cap.isOpened())
bridge = CvBridge()

# Load filters
directory = os.path.dirname(__file__)
path = os.path.join(directory, 'color_filters/filters.pickle')
with open(path, 'rb') as handle:
    filters = pickle.load(handle)

def talker():

    pub = rospy.Publisher('/vision', Image, queue_size=1)
    rospy.init_node('camera', anonymous=False)
    rate = rospy.Rate(10)
    colors_to_test = ['red', 'yellow']
    radius = 10

    while not rospy.is_shutdown():
        _, frame = cap.read()
        frame_to_show = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for k in colors_to_test:
            mask = cv2.inRange(frame, filters[k][0], filters[k][1])
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if(len(cnts) == 2):
                ((x1, y1), r1) = cv2.minEnclosingCircle(cnts[0])
                ((x2, y2), r2) = cv2.minEnclosingCircle(cnts[1])
                x, y = (x1 + x2)/2.0, (y1 + y2)/2.0
                cv2.circle(frame_to_show, (int(x), int(y)), radius, (0, 255, 0), 2)
                print('x = ', int(x*8/40), 'y = ', int(y*8/40))

        cv2.imshow('Camera', frame_to_show)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

        msg = bridge.cv2_to_imgmsg(frame_to_show, "bgr8")
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
