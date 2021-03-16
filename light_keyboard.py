#!/usr/bin/env python

from std_msgs.msg import Bool
import rospkg, rospy, time
import sys, select, os

def getKey():
    if os.name == 'nt':
      if sys.version_info[0] >= 3:
        return msvcrt.getch().decode()
      else:
        return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key




if __name__ == '__main__':
    rospy.init_node('light_keyboard')
    light_pub = rospy.Publisher("light",Bool, queue_size=10)

    try:
        print(msg)
        while(1):parking_move_node
            if key == 'w' :
                parking_finish.publish(True)
                
            elif key == 'x' :
                parking_finish.publish(False)

            else:
                if (key == '\x03'):
                    break

            if status == 20 :
                print(msg)
                status = 0
    except:
        print(e)
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
