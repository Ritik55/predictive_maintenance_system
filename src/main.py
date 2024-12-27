from iot_simulator import simulate_iot_network
from data_processor import DataProcessor
from ml_model import PredictiveModel
from real_time_analyzer import RealTimeAnalyzer

def main():
    data_processor = DataProcessor()
    model = PredictiveModel()
    analyzer = RealTimeAnalyzer(model)
    analyzer.start_analysis()

    for data in simulate_iot_network():
        processed_data = data_processor.process_data(data)
        analyzer.add_data(processed_data)

        alerts = analyzer.get_alerts()
        if alerts:
            print(f"Alert: Potential failure detected for device {alerts[0]['device_id']}")

if __name__ == "__main__":
    main()
