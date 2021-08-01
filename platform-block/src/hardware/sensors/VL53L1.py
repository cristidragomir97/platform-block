class VL53L1(Sensor):
    import VL53L1X

    def __init__(name, angle, bus=1, address=0x29)
        super().__init__(name, kind="ranging", radiation="ir")
        self.tof = VL53L1X.VL53L1X(i2c_bus=bus, i2c_address=address)

    def set_range(self, rng):
        if rng < 4 and rng >= 0:
            self.tof.set_range()
        else:
            raise Exception("Invalid range: 1 - short, 2 - med,  3 - long")

    def set_fov(self, mode):

        if mode == "wide": 
            roi = VL53L1X.VL53L1xUserRoi(0, 15, 15, 0)

        else if mode == "center":
            roi = VL53L1X.VL53L1xUserRoi(6, 9, 9, 6)

        else if mode == "top":
            roi = VL53L1X.VL53L1xUserRoi(6, 15, 9, 12)

        else if mode == "bottom":
            roi = VL53L1X.VL53L1xUserRoi(6, 3, 9, 0)

        else if mode == "left":
            roi = VL53L1X.VL53L1xUserRoi(0, 9, 3, 6)

        else if mode == "right":
            roi = VL53L1X.VL53L1xUserRoi(12, 9, 15, 6)
            
        else:
            roi = VL53L1X.VL53L1xUserRoi(0, 15, 15, 0)

        self.tof.set_user_roi(roi)

    def read(self):
        return self.tof.get_distance()