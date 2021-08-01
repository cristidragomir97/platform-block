import json, sys
from lib.driver import Driver
from lib.robot import Robot
from hardware.driver.Sparkfun import SparkfunDriver
from lib.encoder import QuadratureEncoder

def create_driver(drivetrain):
    wheels = drivetrain["wheels"]["no"]
    wheel_radius = drivetrain["wheels"]["radius"]
    wheel_sep = drivetrain["wheels"]["sep"]
    driver_type = drivetrain["driver"]["type"]
    driver_flip = drivetrain["driver"]["flip"]

    if driver_type == "sparkfun":
            driver = SparkfunDriver(wheels = wheels,
                                    radius =  wheel_radius,
                                    sep = wheel_sep,
                                    flip = driver_flip)
    if driver == "arduino":
        driver = None 
    
    return driver

def create_encoders(drivetrain):
    encs = []
    encoders = drivetrain["encoders"]

    for encoder in encoders:
        encoder_type = encoder["type"]
        if encoder_type == "quadrature":
            position = encoder["position"]
            A = encoder["A"]
            B = encoder["B"]

            enc = QuadratureEncoder(A, B)
            encs.append(enc)

    return encs

def create_servos(servos):
    servo = GPIOServo(name = "camera_servo", pin = SERVO)

def create_sensors(sensors):
     obstacle_sensor = VL53L1(name = "center_ir", angle=0)                

def parse_file(file = "config.json"):
    with open(file) as f:
        config = json.load(f)
        config = config[0]
        print(config)

        # drivetrain (motors and encoders)
        drivetrain = config["drivetrain"]
        motor_driver = create_driver(drivetrain)
        encoders = create_encoders(drivetrain)

        # servos 
        servos = config["servos"]

        #sensors
        sensors = config["sensors"]

        return motor_driver, encoders, servos, sensors

if __name__ == "__main__":
    driver, encoders, servos, sensors = parse_file()

    #bot = Robot()
    #bot.set_drive(driver, encoders)
    
    '''
    for servo in servos:
        bot.add_servo(servo)
    
    for sensor in sensors:
        bot.add_sensor(sensor)
    ''' 

    #bot.run()