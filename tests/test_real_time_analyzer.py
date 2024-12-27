import unittest
import pandas as pd
from src.real_time_analyzer import RealTimeAnalyzer
from src.ml_model import PredictiveModel

class MockModel:
    def predict(self, X):
        return [0.8]  # Always predict above threshold for testing

class TestRealTimeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.mock_model = MockModel()
        self.analyzer = RealTimeAnalyzer(self.mock_model, threshold=0.7)

    def test_add_data(self):
        data = pd.DataFrame({'temperature': [25], 'vibration': [5], 'pressure': [100]})
        self.analyzer.add_data(data)
        self.assertEqual(self.analyzer.data_queue.qsize(), 1)

    def test_get_alerts(self):
        data = pd.DataFrame({'temperature': [25], 'vibration': [5], 'pressure': [100]})
        self.analyzer.add_data(data)
        self.analyzer.start_analysis()
        
        # Give some time for the analysis thread to process
        import time
        time.sleep(0.1)
        
        alerts = self.analyzer.get_alerts()
        self.assertEqual(len(alerts), 1)
        self.assertTrue(isinstance(alerts[0], pd.DataFrame))

    def test_threshold(self):
        low_threshold_analyzer = RealTimeAnalyzer(self.mock_model, threshold=0.9)
        data = pd.DataFrame({'temperature': [25], 'vibration': [5], 'pressure': [100]})
        low_threshold_analyzer.add_data(data)
        low_threshold_analyzer.start_analysis()
        
        import time
        time.sleep(0.1)
        
        alerts = low_threshold_analyzer.get_alerts()
        self.assertEqual(len(alerts), 0)

if __name__ == '__main__':
    unittest.main()
