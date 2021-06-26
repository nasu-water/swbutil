from datetime import datetime
from bluepy.btle import Scanner, DefaultDelegate

class SwitchBotMeter:
    def __init__(self, mac_addr):
        self.mac_addr = mac_addr.lower()
        self.scanner = Scanner().withDelegate(MeterDelegate(self.mac_addr))
        self.scanned_data = None

        
    def scan(self, scan_time_sec=3.0, max_retry_count=3):
        is_error = True
        retry_count = 0
        scanned_data = None

        # Repeat till scanned data is from meter or till retry count is below max retry count
        while is_error and retry_count < max_retry_count:
                retry_count += 1
                try:
                    self.scanner.scan(scan_time_sec)
                    
                    for device in self.scanner.getDevices():
                        if self.mac_addr in device.addr:
                            self.scanned_data = self.scanner.delegate.get_sensor_value()
                            is_error = False
                except:
                    pass


    def get_scan_data(self):
        return self.scanned_data
        

class MeterDelegate(DefaultDelegate):
    def __init__(self, mac_addr):
        DefaultDelegate.__init__(self)
        self.mac_addr = mac_addr
        self.sensor_value = None


    # Return latest sensor value
    # Rturns None when scan is not executed or scan failed 
    def get_sensor_value(self):
        return self.sensor_value

    
    def _decode_sensor_data(self, sensor_value_str):
        # Read sensor data from string and convert to binary data
        sensor_value_binary = bytes.fromhex(sensor_value_str[4:])
        
        # Battery
        battery_value = sensor_value_binary[2] & 0b01111111

        # Temperature above or below 0.
        is_temp_negative = sensor_value_binary[4] & 0b10000000

        # Temperature
        temp_value = ( sensor_value_binary[3] & 0b00001111 ) / 10 + ( sensor_value_binary[4] & 0b01111111 )

        # When temperature is below 0, make temp_value as negative value
        if not is_temp_negative:
            temp_value = -temp_value

        # Humidity
        humid_value = sensor_value_binary[5] & 0b01111111

        # Store in dictionary
        self.sensor_value = {
            'macaddr': self.mac_addr,
            'temperature': temp_value,
            'humidity': humid_value,
            'battery': battery_value,
            'datetime': datetime.now()
        }

        
    # Device handler
    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        # Scan entry devices macaddress
        if scanEntry.addr == self.mac_addr:
            # Retrieve advertisement data 
            for (adtype, description, value) in scanEntry.getScanData():
                # When description is environment sensor data
                if description == '16b Service Data':
                    # Decode sensor data
                    self._decode_sensor_data(value)
