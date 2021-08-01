import rospy
import Jetson.GPIO as GPIO

class L298NDriver(Driver):
    def __init__(self, wheels, radius, sep, flip, pins):
        super().__init__(wheels, radius, sep, flip)

        try:
            pwm_right = pins["PWM_RIGHT"]
            pwm_left = pins["PWM_LEFT"]
            right_a = pins["RIGHT_A"]
            right_b = pins["RIGHT_B"]
            left_a = pins["LEFT_A"]
            left_b = pins["LEFT_B"]
        except NameError, ValueError:
            print("Pin configuration incorrect")
        
        try:
            GPIO.setmode(GPIO.BOARD) 
            GPIO.setup(pwm_right, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(pwm_left, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(right_a, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(right_b, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(left_a, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(left_b, GPIO.OUT, initial=GPIO.LOW)
        
            self.pwm_right = GPIO.PWM(pwm_right, 50)
            self.pwm_right.start(0)

            self.pwm_left = GPIO.PWM(pwm_right, 50)
            self.pwm_left.start(0)
            
        except Exception as e:
            print("Error setting pins up")
    
    def update(self, angular, linear):
        right_pwm, left_pwm = super().compute_pwm(angular, linear, self.radius, self.sep)
        self.pwm_right.ChangeDutyCycle(right_pwm)
        self.pwm_left.ChangeDutyCycle(left_pwm)

        ## add code for forward, back, alea alea 


