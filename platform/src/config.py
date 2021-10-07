
import json
from colorama import Fore, Back

def has_key(object, key):
    try: 
        object["{}".format(key)]
        return True
    except ValueError:
        return False

def parse_actuators(actuators):
    print("[config] {} ranging sensor(s) :".format(len(actuators)))
    for actuator in actuators:
        print("[config]\t * type: {}, topic: {}".format(actuator["type"], actuator["topic"]))


def parse_sensors(sensors):
        # camera
        if has_key(sensors, "camera"):
           
            cameras = sensors["camera"]  
            print("\n[config] {} camera(s):".format(len(cameras))) 

            for camera in cameras: 
                print("[config]\t ---> type: {}, model: {}".format(camera["type"], camera["model"]))

        # LIDAR
        if has_key(sensors, "LIDAR"):
            lidar = sensors["LIDAR"]
            print("\n* LIDAR: ")  

            print("[config]\t ---> type: {}, model: {}".format(lidar["type"], lidar["model"]))

         # range sensors
        if has_key(sensors, "ranging"):
            print("\n[config] {} ranging sensor(s) :".format(len(sensors["ranging"])))

            ranging = sensors["ranging"]
            for sensor in ranging:
                print("[config] \t ---> type: {}, topic: {}".format(sensor["type"], sensor["topic"]))
        
        if has_key(sensors, "IMU"):
            print("\n[config]  IMU available")
            topic = sensors["IMU"]["topic"]
            kind = sensors["IMU"]["type"]
            print("[config] \t ---> type:{}, topic: {}".format(kind, topic))

"""
ta
"""
class ConfigParser():

    def __init__(self, file="src/config.json"):
        print("Configuration loaded: \n")
        with open(file) as f:
            config = json.load(f)
            config = config[0]

            # general stuff
            self.name = config["name"]
            self.desc = config["desc"]
    
            # driver
            self.driver = config["driver"]

            # actuators
            if has_key(config, "actuators"):
                actuators = config["actuators"]
                parse_actuators(actuators)

            # sensors
            if has_key(config, "sensors"):
                sensors = config["sensors"]
                parse_sensors(sensors)

    def get_driver(self):
        pid, radius, kind, address, flip = list(self.driver.values())
        return pid, radius, kind, address, flip




