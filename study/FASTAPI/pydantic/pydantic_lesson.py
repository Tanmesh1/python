from pydantic import BaseModel
from typing import List , Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact: Dict[str,str]


def insert_patient_data(name, age):

    print(name)

def update_patients_data(patient: Patient):
    print(patient.name)


patient_info = {'name' : 'mokesh', 'age': '30', 'weight': 75.2 , 'married': True,'allergies': ['pollen','dust'], 'contact': {'email': 'abc@gmail.com','phone':'12332423454'}}

patient1 = Patient(**patient_info)

update_patients_data(patient1)