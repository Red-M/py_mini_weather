from . import base_sensor
import time

class sds011(base_sensor.Sensor):
    def __init__(self, queue,config):
        super().__init__(queue,config)
        import sds011 as sds011_module
        self.sds011 = sds011_module
        self.sensor = self.sds011.SDS011(self.config['port'], use_query_mode=True)
        self.device_sleep = 60

    def wakeup(self):
        self.sensor.sleep(sleep=False)
        time.sleep(self.device_sleep)

    def sleep(self):
        self.sensor.sleep(sleep=True)

    def read(self):
        pmdata = self.sensor.query()
        out = {
            'PM2.5':pmdata[0],
            'PM10':pmdata[1]
        }
        return(out)
