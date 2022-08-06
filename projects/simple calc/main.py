from prefect import flow, task
from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: float
    c: str

@task
def printer(obj):
    print(f"Received a {type(obj)} with value {obj}")

@flow(name='Simple Calc Flow')
def model_validator(model: Model):
    printer(model)
