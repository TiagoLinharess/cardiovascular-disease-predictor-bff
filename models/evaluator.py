from sklearn.metrics import accuracy_score

class Evaluator:

    def evaluate(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        return accuracy_score(y_test, predictions)