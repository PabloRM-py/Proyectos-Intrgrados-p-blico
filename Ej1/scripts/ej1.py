#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16  
def ej1():
     pub=rospy.Publisher('numerador',Int16,queue_size=10)
     rospy.init_node('numerados',anonymous=True)
     rate=rospy.Rate(10)
     i=0
     while not rospy.is_shutdown():
         try:
             while i !=5:
                num_int=int(input('Dasme ints: '))
                #print(num_int)
                rospy.loginfo(num_int)
                pub.publish(num_int)
                i=i+1
             if i==5:
                pass
         except IOError:
            exit('Error')
if __name__ == '__main__':
 try:
    ej1()
 except rospy.ROSInterruptException:
    pass