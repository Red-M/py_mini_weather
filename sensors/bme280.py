from . import base_sensor

class bme280(base_sensor.BME2680Sensor):
    def __init__(self, queue):
        super().__init__(queue)
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
        self.bme280.seaLevelhPa = 1014.5

    def wakeup(self):
        self.set_power_state(True)

    def sleep(self):
        self.set_power_state(False)

    def read(self):
        out = {
            'Temperature':self.bme280.temperature,
            'Humidity':self.bme280.humidity,
            'Pressure':self.bme280.pressure,
            'Altitude':self.bme280.altitude
        }
        return(out)

