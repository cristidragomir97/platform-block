class SR04:
    import Jetson.GPIO as GPIO
    

    def read():
        GPIO.output(GPIO_TRIGGER, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
 
        # start timers 
        StartTime = time.time()
        StopTime = time.time()
 
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
 
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because we got the 
        distance = (TimeElapsed * 34300) / 2
 
        return distance