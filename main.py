#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel


#FastAPI 
from fastapi import FastAPI
from fastapi import Query
from fastapi import Path
from fastapi.param_functions import Body


app = FastAPI()

# Models 

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello":"World"}



@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
#...  obligatorio


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


# Validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
	person_id: int = Path(...,ge=0)
    ):
	return {person_id: "It exist!"}

#validaciones: Request Body

@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        ge=1,
        title='Person id',
        description='Id of the person you want to update'
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = dict(person)
    result.update(dict(location)) #uniendo diccioanrio

    return result