import unittest
import pandas as pd
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
        self.sample_data = {
            "device_id": "device_1",
            "device_type": "pump",
            "timestamp": "2023-01-01T00:00:00",
            "temperature": 45.2,
            "vibration": 3.7,
            "pressure": 102.3
        }

    def test_process_data(self):
        result = self.processor.process_data(self.sample_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 1)
        self.assertIn("temperature", result.columns)
        self.assertIn("vibration", result.columns)
        self.assertIn("pressure", result.columns)
