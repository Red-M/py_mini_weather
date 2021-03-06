from . import base_sensor

class bme680(base_sensor.Sensor):
    def __init__(self, queue,config):
        super().__init__(queue,config)
        import board
        import busio
        import adafruit_bme680
        self.board = board
        self.busio = busio
        self.adafruit_bme680 = adafruit_bme680
        self.i2c = self.busio.I2C(self.board.SCL, self.board.SDA)
        self.bme680 = self.adafruit_bme680.Adafruit_BME680_I2C(self.i2c,debug=False)
        self.bme = self.bme680
        self._REG_CTRL_MEAS = self.adafruit_bme680._BME680_REG_CTRL_MEAS
        self.bme.seaLevelhPa = 1014.5
        self.temperature_offset = self.config.get('temp_offset',-5)
        self.read()

    def set_power_state(self,state):
        if isinstance(state,type(False))==True:
            temp = int.from_bytes(self.bme._read(self._REG_CTRL_MEAS, 1), byteorder='big', signed=False)
            temp &= ~0x03
            temp |= state << 0
            self.bme._write(self._REG_CTRL_MEAS, [temp])

    def wakeup(self):
        self.set_power_state(True)

    def sleep(self):
        self.set_power_state(False)

    def read(self):
        out = {
            'Gas':self.bme.gas,
            'Temperature':self.bme.temperature+self.temperature_offset,
            'Humidity':self.bme.humidity,
            'Pressure':self.bme.pressure,
            'Altitude':self.bme.altitude
        }
        return(out)

