from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from models import Pipeline
from schemas import PatientSchema, SuccessResponse, ErrorResponse, success_json, error_json

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
@app.post('/predict', tags=[post_register_tag], responses={"201": SuccessResponse, "400": ErrorResponse})
def predict(form: PatientSchema):
    try:
        model = Pipeline().charge_model()
        scaler = Pipeline().charge_scaler()

        new_data = [[form.age, form.sex, form.cp, form.trestbps, form.chol, form.fbs, form.restecg, form.thalach, form.exang, form.oldpeak, form.slope, form.ca, form.thal]]

        column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

        new_data_df = pd.DataFrame(new_data, columns=column_names)

        new_data_scaled = scaler.transform(new_data_df)

        predict = model.predict(new_data_scaled)

        return success_json(int(predict))
    except Exception as e:
        return error_json(str(e))