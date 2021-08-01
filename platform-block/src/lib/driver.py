
import rospy
import threading

class Driver(threading.Thread):
    def __init__(self, wheels, radius, sep, flip):
        self.radius = radius 
        self.wheels = wheels
        self.sep = sep
        self.flip = flip
        print("* initialising base driver with", radius, wheels, sep, flip)
    
    def compute_pwm(angular, linear, radius, sep):
        right_pwm = (linear / radius) + ((angular * sep) / (2.0 * radius)) * 10
        left_pwm = (linear / radius)  - ((angular * sep) / (2.0 * radius)) * 10
        return right_pwm, left_pwm

    def set_callback(self, fn):
        self.callback = fn

    def run(self):
        rospy.init_node('motor_driver', anonymous=False)
        rospy.Subscriber('cmd_vel', Twist, self.callback)
        rospy.spin()









