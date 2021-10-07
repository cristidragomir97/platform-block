import VL53L1X
from lib.ranging import Ranging

class VL53L1(Ranging):

    def __init__(self, name, address="0x29"):
        
        super().__init__(name, 
                radiation="ir",
                min_range="0",
                max_range="400", 
                fov="27")

        super().set_callback(self.read)


        self.tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=address)

    def set_range(self, rng):
        if rng < 4 and rng >= 0:
            self.tof.set_range()
        else:
            raise Exception("Invalid range: 1 - short, 2 - med,  3 - long")

    def set_fov(self, mode):

        if mode == "wide": 
            roi = VL53L1X.VL53L1xUserRoi(0, 15, 15, 0)

        elif mode == "center":
            roi = VL53L1X.VL53L1xUserRoi(6, 9, 9, 6)

        elif mode == "top":
            roi = VL53L1X.VL53L1xUserRoi(6, 15, 9, 12)

        elif mode == "bottom":
            roi = VL53L1X.VL53L1xUserRoi(6, 3, 9, 0)

        elif mode == "left":
            roi = VL53L1X.VL53L1xUserRoi(0, 9, 3, 6)

        elif mode == "right":
            roi = VL53L1X.VL53L1xUserRoi(12, 9, 15, 6)
            
        else:
            roi = VL53L1X.VL53L1xUserRoi(0, 15, 15, 0)

        self.tof.set_user_roi(roi)

    def read(self):
        return self.tof.get_distance()