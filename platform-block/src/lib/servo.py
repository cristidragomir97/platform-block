

class Servo():
    def __init___(self, name, pin): 
        self.name = name 
        self.pin = pin

    def angle_to_pwm(self, angle):
        return (angle/18.0) + 2.5
        
