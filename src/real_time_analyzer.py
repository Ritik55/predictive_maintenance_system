import threading
from queue import Queue

class RealTimeAnalyzer:
    def __init__(self, model, threshold=0.7):
        self.model = model
        self.threshold = threshold
        self.data_queue = Queue()
        self.alert_queue = Queue()

    def analyze_data(self):
        while True:
            data = self.data_queue.get()
            prediction = self.model.predict(data)
            if prediction[0] > self.threshold:
                self.alert_queue.put(data)

    def start_analysis(self):
        threading.Thread(target=self.analyze_data, daemon=True).start()

    def add_data(self, data):
        self.data_queue.put(data)

    def get_alerts(self):
        alerts = []
        while not self.alert_queue.empty():
            alerts.append(self.alert_queue.get())
        return alerts
