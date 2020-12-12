import time

class Sensor(object):
    def __init__(self,queue):
        self.auto_restart = True
        self.device_sleep = 10
        self.queue = queue

    def poll(self):
        while True:
            self.queue.put(self.read())
            time.sleep(self.device_sleep)
