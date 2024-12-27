import unittest
import numpy as np
from src.ml_model import PredictiveModel

class TestPredictiveModel(unittest.TestCase):
    def setUp(self):
        self.model = PredictiveModel()
        self.X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.y_train = np.array([0, 1, 1])

    def test_train(self):
        self.model.train(self.X_train, self.y_train)
        self.assertIsNotNone(self.model.model)

    def test_predict(self):
        self.model.train(self.X_train, self.y_train)
        X_test = np.array([[2, 3, 4]])
        prediction = self.model.predict(X_test)
        self.assertIsInstance(prediction, np.ndarray)
        self.assertEqual(prediction.shape, (1,))

    def test_save_and_load_model(self):
        self.model.train(self.X_train, self.y_train)
        self.model.save_model("test_model.joblib")
        
        new_model = PredictiveModel()
        new_model.load_model("test_model.joblib")
        
        X_test = np.array([[2, 3, 4]])
        original_prediction = self.model.predict(X_test)
        loaded_prediction = new_model.predict(X_test)
        
        np.testing.assert_array_equal(original_prediction, loaded_prediction)

if __name__ == '__main__':
    unittest.main()
