# py_mini_weather

Mini weather station using a raspberry pi (any of them will work, I prefer the 0w for the low power and the wifi), cherrypy and not much else.

# Supported Hardware

- PMS5003 particle sensor (pm1, pm2.5, pm10)
- SDS011 accurate particle sensor (pm2.5, pm10)
- BME280 (air pressure, humidity, temperature)
- BME680 (air pressure, humidity, temperature, VOC/Gas)

# Dependencies

Install the dependencies via the `install_dependencies.sh` script.

# Home Assistant setup
Home Assistant needs config in its sensors section similar to this:
```- platform: rest
  name: environ_sensor_api_stats
  value_template: '{{ value_json }}'
  resource: http://<IP_or_hostname>:8080/get_stats
  json_attributes:
    - PM1
    - PM2.5
    - PM10
    - Temperature
    - Humidity
    - Pressure
    - Gas
    - Altitude

- platform: template
  sensors:
    airmon_pm1:
      friendly_name: 'PM1 particles'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'PM1') }}"
      unit_of_measurement: "μg/m³"
      entity_id: sensor.environ_sensor_api_stats
    airmon_pm2_5:
      friendly_name: 'PM2.5 particles'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'PM2.5') }}"
      unit_of_measurement: "μg/m³"
      entity_id: sensor.environ_sensor_api_stats
    airmon_pm10:
      friendly_name: 'PM10 particles'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'PM10') }}"
      unit_of_measurement: "μg/m³"
      entity_id: sensor.environ_sensor_api_stats
    airmon_temp:
      friendly_name: 'Temperature'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'Temperature') }}"
      unit_of_measurement: "°C"
      entity_id: sensor.environ_sensor_api_stats
    airmon_pressure:
      friendly_name: 'Pressure'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'Pressure') }}"
      unit_of_measurement: "hPa"
      entity_id: sensor.environ_sensor_api_stats
    airmon_humidity:
      friendly_name: 'Humidity'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'Humidity') }}"
      unit_of_measurement: "%"
      entity_id: sensor.environ_sensor_api_stats
    airmon_gas:
      friendly_name: 'Air VOC/Gas'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'Gas') }}"
      unit_of_measurement: "ohm"
      entity_id: sensor.environ_sensor_api_stats
    airmon_altitude:
      friendly_name: 'Altitude'
      value_template: "{{ state_attr('sensor.environ_sensor_api_stats', 'Altitude') }}"
      unit_of_measurement: "m"
      entity_id: sensor.environ_sensor_api_stats
```

# TO DO
- Nicer README.
- Wiring diagram.
- Some form of tests.
- API documentation, not that there is much to document.

