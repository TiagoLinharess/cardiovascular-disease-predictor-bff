from pydantic import BaseModel

class PatientSchema(BaseModel):
    age: float = 63
    sex: int = 1
    cp: int = 2
    trestbps: float = 145.0
    chol: float = 204
    fbs: int = 1
    restecg: int = 2
    thalach: float = 108
    exang: int = 1
    oldpeak: float = 2.6
    slope: float = 2
    ca: float = 3
    thal: int = 7