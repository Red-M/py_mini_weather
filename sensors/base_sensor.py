import time

class Sensor(object):
    def __init__(self,queue):
        self.auto_restart = True
        self.device_sleep = 10
        self.queue = queue

    def wakeup(self):
        pass

    def sleep(self):
        pass

    def poll(self):
        while True:
            # print('Start Poll: '+str(self))
            self.wakeup()
            self.queue.put(self.read())
            self.sleep()
            # print('End Poll: '+str(self))
            time.sleep(self.device_sleep)

class BME2680Sensor(Sensor):

    def set_power_state(self, state):
        if isinstance(state,type(False))==True:
            temp = int.from_bytes(self.bme._read(self._REG_CTRL_MEAS, 1), byteorder='big', signed=False)
            temp &= ~0x03
            temp |= state << 0
            self.bme680._write(self._REG_CTRL_MEAS, [temp])
