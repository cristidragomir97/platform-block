import json, sys, rospy, time

from geometry_msgs.msg import Twist
from time import sleep


from roscore import Roscore
from constants import *
from utils import scan_bus, detect_usb, tof_address_fix
from config import ConfigParser
from subscriber import Subscriber

from hardware.driver.Sparkfun import SparkfunDriver

parser = ConfigParser()

def handle_actuators():
    pass

def handle_sensors():
    pass

def handle_driver():
    pid, radius, kind, address, flip = parser.get_driver()

    # switch based on driver type
    if kind == "sparkfun":
        sparkfun = SparkfunDriver(radius=radius, flip=flip)

        # check for connection 
        if address in scan_bus():

            sub = Subscriber(
                name="{}".format("kind"),
                topic="cmd_vel", 
                message=Twist,
                callback=sparkfun.update)

            sub.start()

            

    if kind == "L298N":
        print("sorry, motor driver not implemented yet")
        pass

    if kind == "adafruit":
        print("sorry, motor driver not implemented yet")
        pass

if __name__ == "__main__":
    Roscore().run()
    time.sleep(5)

    bus = scan_bus()
    print(bus)
    
    try:

        if TOF1 and TOF2 and TOF3 in bus: 
            pass
        else:
            tof_address_fix()
            print(scan_bus())
    except Exception:
        print("shit happens")

    handle_driver()
    #handle_actuators()
    #handle_sensors()

 

    
