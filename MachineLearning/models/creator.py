import joblib

class Creator:

    def create(model):
        joblib.dump(model, 'MachineLearning/pipelines/cardiovascular_disease_predictor.pkl')