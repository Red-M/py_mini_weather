from . import base_sensor

class bme280(base_sensor.Sensor):
    def __init__(self, queue,config):
        super().__init__(queue,config)
        import board
        import busio
        import adafruit_bme280
        self.board = board
        self.busio = busio
        self.adafruit_bme280 = adafruit_bme280
        self.i2c = self.busio.I2C(self.board.SCL, self.board.SDA)
        self.bme280 = self.adafruit_bme280.Adafruit_BME280_I2C(self.i2c)
        self.bme = self.bme280
        self._REG_CTRL_MEAS = self.adafruit_bme280._BME280_REGISTER_CTRL_MEAS
        self.read()
        self.bme.seaLevelhPa = 1014.5

    def set_power_state(self,state):
        if isinstance(state,type(False))==True:
            options = {
                True:self.adafruit_bme280.MODE_FORCE,
                False:self.adafruit_bme280.MODE_SLEEP
            }
            self.bme.mode = options[state]

    def wakeup(self):
        self.set_power_state(True)

    def sleep(self):
        self.set_power_state(False)

    def read(self):
        out = {
            'Temperature':self.bme.temperature,
            'Humidity':self.bme.humidity,
            'Pressure':self.bme.pressure,
            'Altitude':self.bme.altitude
        }
        return(out)

