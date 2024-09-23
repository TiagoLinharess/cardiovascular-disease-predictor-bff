import joblib

class Creator:

    def create(model):
        joblib.dump(model, 'MachineLearning/ML/cardiovascular_disease_predictor.pkl')