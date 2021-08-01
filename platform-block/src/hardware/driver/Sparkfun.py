import rospy, qwiic_scmd
from lib.driver import Driver

class SparkfunDriver(Driver):
     
    def __init__(self, wheels, radius, sep, flip):
        super().__init__(wheels, radius, sep, flip)

        #try:
        self.sparkfun = qwiic_scmd.QwiicScmd()
        self.drivetrain = "differential"
            
        if self.sparkfun.connected == False:
            print('Motor Driver not connected. Check Connections')

        self.sparkfun.begin()
        self.sparkfun.set_drive(0, 0, 0)
        self.sparkfun.set_drive(1, 0, 0)
        self.sparkfun.enable()

        super().set_callback(update)
        super().start()

        print("* Motors	successfullly initialised")
        #except Exception as e:
            #print("\033[91m* Exception initialisitng Sparkfun Driver", e )

    def update(self, msg):
        angular = msg.angular.z
        linear = msg.linear.x
        right_pwm, left_pwm = super().compute_pwm(angular, linear, self.radius, self.sep)
        driver.set_drive(0, 0, right_pwm)
        driver.set_drive(1, 1, left_pwm)