from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from MachineLearning import Model

import pandas as pd

# Inicializa API
info = Info(title="Cardiovascular disease predictor", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# Rota Predição POST
post_register_tag = Tag(name="Predição", description="Efetua a predição de doença cardiovascular com base nos dados enviados")
@app.post('/predict', tags=[post_register_tag], responses={"201": {"result": True}, "400": {"error": "error"}})
def predict():
    model = Model().charge_model()
    scaler = Model().charge_scaler()

    new_data = [[63, 1, 3, 160, 285, 1, 2, 200, 1, 3.5, 3, 3, 7],
                [89, 0, 2, 130, 250, 1, 1, 187, 1, 3.5, 3, 3, 3],
                [41, 1, 1, 130, 204, 0, 0, 172, 0, 1.4, 2, 0, 2]]

    column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    new_data_df = pd.DataFrame(new_data, columns=column_names)

    new_data_scaled = scaler.transform(new_data_df)

    predictions = model.predict(new_data_scaled)

    return {"predict": int(predictions[1])}