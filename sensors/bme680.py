from . import base_sensor

class bme680(base_sensor.Sensor):
    def __init__(self, queue):
        super().__init__(queue)
        import board
        import busio
        import adafruit_bme680
        self.board = board
        self.busio = busio
        self.adafruit_bme680 = adafruit_bme680
        self.i2c = self.busio.I2C(self.board.SCL, self.board.SDA)
        self.bme680 = self.adafruit_bme680.Adafruit_BME680_I2C(self.i2c)
        self.bme680.seaLevelhPa = 1014.5

    def read(self):
        out = {
            'Gas':self.bme680.gas,
            'Temperature':self.bme680.temperature,
            'Humidity':self.bme680.humidity,
            'Pressure':self.bme680.pressure,
            'Altitude':self.bme680.altitude
        }
        return(out)

