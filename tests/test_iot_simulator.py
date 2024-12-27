import unittest
from src.iot_simulator import IoTDevice, simulate_iot_network

class TestIoTSimulator(unittest.TestCase):
    def test_iot_device_data_generation(self):
        device = IoTDevice("test_device", "pump")
        data = device.generate_data()
        self.assertIn("device_id", data)
        self.assertIn("device_type", data)
        self.assertIn("timestamp", data)
        self.assertIn("temperature", data)
        self.assertIn("vibration", data)
        self.assertIn("pressure", data)

    def test_simulate_iot_network(self):
        generator = simulate_iot_network(num_devices=3)
        data = next(generator)
        self.assertIsInstance(data, dict)
        self.assertIn("device_id", data)
