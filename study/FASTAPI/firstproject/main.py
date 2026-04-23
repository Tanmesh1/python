from fastapi import FastAPI ,Path , HTTPException ,Query
import json
import os

app = FastAPI()

def load_data():
    try:
        print("in the load data")
        file_path = os.path.join(os.path.dirname(__file__), "patients.json")

        with open(file_path, 'r') as f:
            data = json.load(f)

        return data

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def hello():
    return {'message': 'Hello World'}

@app.get("/view")
def view():
    print("in the view")
    data = load_data()
    print(data)

    return data


@app.get("/patient/{patient_id}")
def view_patients(patient_id: str = Path(..., description='ID of the patient in the DB',example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return  HTTPException(status_code=404, detail = 'patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description= 'Sort on the basis of height , weight or bmi'), order : str = Query('asc', description='sort in asc or desc order')):


    valid_fields = ['height', 'weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select  from {valid_fields}')
    

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order selected between asc and desc')\
        

    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
