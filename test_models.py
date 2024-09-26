from models import Charger, Model, Evaluator, Pipeline
import pytest

# Initialize Classes
charger = Charger()
model = Model()
evaluator = Evaluator()
pipeline = Pipeline()

# Parameters
url = './MachineLearning/data/heart-disease-uci.csv'
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Charge data
data = charger.loadData(url)
array = data.values
X_test = array[:, :-1]
y_test = array[:, -1]

def test_model_lr():
    lr_path = './MachineLearning/models/cardiovascular_disease_predictor_lr.pkl'
    model = pipeline.charge(lr_path)

    accuracy = evaluator.evaluate(model, X_test, y_test)

    assert accuracy >= 0.6

def test_model_knn():
    lr_path = './MachineLearning/models/cardiovascular_disease_predictor_knn.pkl'
    model = pipeline.charge(lr_path)

    accuracy = evaluator.evaluate(model, X_test, y_test)

    assert accuracy >= 0.54

def test_model_rf():
    lr_path = './MachineLearning/pipelines/cardiovascular_disease_predictor.pkl'
    model = pipeline.charge(lr_path)

    accuracy = evaluator.evaluate(model, X_test, y_test)

    assert accuracy >= 0.92
