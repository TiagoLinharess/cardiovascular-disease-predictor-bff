from pydantic import BaseModel

class SuccessResponse(BaseModel):
    predict: int = 1

class ErrorResponse(BaseModel):
    error: str = "Message"

def success_json(value):
    return { "predict": value }

def error_json(e):
    return { "error": e }