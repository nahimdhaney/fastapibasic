#Python
from typing import Optional
from fastapi.param_functions import Body

#Pydantic
from pydantic import BaseModel


#FastAPI 
from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

# Models 

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello":"World"}


@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=50
    ),

    # El ... para hacerlo obligatorio, no recomendado en un Query parameter
    age: int = Query(...)
):
    '''
    Funcion para probar la validacion en los query parameter.
    El Age esta obligatorio, no se recomienda hacer esto, si necesitas un
    parametro obligatorio se recomienda hacerlo en un path parameter
    '''
    return {name: age}
# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
#...  obligatorio