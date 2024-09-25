import joblib

class Pipeline:

    def charge_model(self):
        return joblib.load('./MachineLearning/pipelines/cardiovascular_disease_predictor.pkl')

    def charge_scaler(self):
        return joblib.load('./MachineLearning/scalers/scaler.pkl')