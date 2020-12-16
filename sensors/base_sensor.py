import time

class Sensor(object):
    def __init__(self,queue,config):
        self.auto_restart = True
        self.device_sleep = 10
        self.queue = queue
        self.config = config

    @classmethod
    def name(self):
        return(self.__name__)

    def wakeup(self):
        pass

    def sleep(self):
        pass

    def poll(self):
        while True:
            # print('Start Poll: '+str(self.name()))
            self.wakeup()
            self.queue.put([self.name(),self.read()])
            self.sleep()
            # print('End Poll: '+str(self.name()))
            time.sleep(self.device_sleep)
