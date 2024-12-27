import random
import time
from datetime import datetime

class IoTDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

    def generate_data(self):
        timestamp = datetime.now().isoformat()
        temperature = random.uniform(20, 80)
        vibration = random.uniform(0, 10)
        pressure = random.uniform(90, 110)
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "timestamp": timestamp,
            "temperature": temperature,
            "vibration": vibration,
            "pressure": pressure
        }

def simulate_iot_network(num_devices=5):
    devices = [IoTDevice(f"device_{i}", random.choice(["pump", "motor", "valve"])) 
               for i in range(num_devices)]
    while True:
        for device in devices:
            yield device.generate_data()
        time.sleep(1)
