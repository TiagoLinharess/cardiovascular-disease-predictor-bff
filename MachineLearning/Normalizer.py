from sklearn.preprocessing import StandardScaler
import joblib

class Normalizer:

    def normalize(self, X_train):
        scaler = joblib.load('./MachineLearning/Scaler/scaler.pkl')
        X_train = scaler.transform(X_train)
        return X_train
