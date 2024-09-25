from sklearn.neighbors import KNeighborsClassifier

class Model:

    def trainModel(self, X_train, y_train):
        knn = KNeighborsClassifier()
        knn.fit(X_train, y_train)
        return knn
