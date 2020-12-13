from . import base_sensor

class sds011(base_sensor.Sensor):
    def __init__(self, queue):
        super().__init__(queue)
        import sds011
        self.sds011 = sds011
        self.sensor = self.sds011.SDS011('/dev/ttyUSB0', use_query_mode=True)

    def wakeup(self):
        self.sensor.sleep(sleep=False)

    def sleep(self):
        self.sensor.sleep(sleep=True)

    def read(self):
        pmdata = self.sensor.query()
        out = {
            'PM2.5':pmdata[0],
            'PM10':pmdata[1]
        }
        return(out)
