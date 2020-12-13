#!/usr/bin/env python3
import os
import sys
import time
import yaml
import threading
import multiprocessing
import cherrypy
import sensors


class SensorServ:
    def __init__(self):
        self.sensor_data = {}
        self.load_config()
        self.queue = multiprocessing.Queue()
        self.collector_queue = multiprocessing.Queue()
        self.lock = multiprocessing.Lock()
        self.start_collector()

    def load_config(self):
        f = open(os.path.join(os.path.dirname(__file__), 'config.yml'), 'r')
        self.config = yaml.load(f,Loader=yaml.FullLoader)
        f.close()

    def start_collector(self):
        self.collector_thread = threading.Thread(target=self.collector)
        not_sensors = ['modules','os', 'glob']
        self.active_sensors = []
        sensors_list = dir(sensors)
        sensors_list.reverse()
        for sensor in sensors_list:
            if not (sensor.startswith('_') or sensor in not_sensors):
                if sensor in self.config['devices']:
                    self.active_sensors.append(sensor)
        self.collector_thread.start()

    def collector(self):
        collector_data = {}
        threads = {}
        while True:
            for sensor in self.active_sensors:
                if not sensor in threads:
                    sensor_module = getattr(sensors,sensor)
                    threads[sensor] = {}
                    threads[sensor]['class'] = getattr(sensor_module,sensor)(self.queue)
                    threads[sensor]['thread'] = threading.Thread(target=threads[sensor]['class'].poll)
                    threads[sensor]['thread'].start()
                else:
                    if threads[sensor]['thread'].is_alive()==False and threads[sensor]['class'].auto_restart==True:
                        threads[sensor]['thread'].join(1)
                        del threads[sensor]
            ret = self.queue.get()
            collector_data.update(ret)
            if self.collector_queue.qsize()>=1:
                self.collector_queue.get_nowait()
            self.collector_queue.put(collector_data)
            time.sleep(self.config['collector_poll_time'])

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_stats(self):
        if self.collector_queue.qsize()==1:
            self.sensor_data = self.collector_queue.get_nowait()
        return(self.sensor_data)



if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(SensorServ())
