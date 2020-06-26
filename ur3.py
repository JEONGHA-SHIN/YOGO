import urx
import time

init_j = (-0.7967985312091272, -1.6069005171405237, -1.516601864491598, -1.5728910605060022, 1.6002588272094727, -3.5587941304981996e-05)
mid_l = (-0.294,-0.258,0.24502,1.1064,-2.9611,0.0060)
destination_l = (-0.374,0.08723,0.25458,1.0025,2.9890,0.1350)

class ur3:

    def connect(self, bind_ip = '192.168.0.34'):
        self.init_joint = mid_l
        self.rob = urx.Robot(bind_ip)
        self.rob.movel(self.init_joint, 1, 0.5, wait=False)

    def __del__(self):
        self.rob.close()

    def auto_callibration(self):
        print("will be late")

    def go_2_bin(self, bin_global_location=(0.23, -0.4, 0.3, 2.85, 1.3, 0)):

        self.rob.movel(bin_global_location, 1, 0.2, wait=False)

    def go_down(self, z=0.05):
        self.rob.movel((0, 0, -z, 0, 0, 0), 0.5, 0.2, relative=True, wait=False)

    def go_destination(self):
        self.rob.movel(mid_l, 0.5, 0.2, wait=False)
        while True :
            time.sleep(0.5)
            if not self.rob.is_program_running():
                break
        self.rob.movel(destination_l, 0.5, 0.2, wait=False)

    def close(self):
        self.rob.close()