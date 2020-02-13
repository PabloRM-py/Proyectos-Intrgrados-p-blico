#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
def hablador():
     pub=rospy.Publisher('chateador',String,queue_size=10)
     rospy.init_node('hablador',anonymous=True)
     rate=rospy.Rate(10)
     counter=0
     while not rospy.is_shutdown():
         hola_str='Yo te saludo {0} veces'.format(counter)
         counter=counter+1
         rospy.loginfo(hola_str)
         pub.publish(hola_str)
         rate.sleep() 
if __name__ == '__main__':
 try:
    hablador()
 except rospy.ROSInterruptException:
    pass 