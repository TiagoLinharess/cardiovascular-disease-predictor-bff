from sklearn.neighbors import KNeighborsClassifier
import joblib

class Model:

    def charge_model(self):
        return joblib.load('./MachineLearning/ML/cardiovascular_disease_predictor.pkl')

    def charge_scaler(self):
        return joblib.load('./MachineLearning/Scaler/scaler.pkl')

    def trainModel(self, X_train, y_train):
        knn = KNeighborsClassifier()
        knn.fit(X_train, y_train)
        return knn
