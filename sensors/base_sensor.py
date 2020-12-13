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
            self.wakeup()
            self.queue.put(self.read())
            self.sleep()
            time.sleep(self.device_sleep)
