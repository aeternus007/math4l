from fastapi import FastAPI, Form
import uvicorn

from datetime import datetime
import json

from utils import Alert, Coords, sort_by_time


app = FastAPI()

@app.post("/create")
def create(alert : Alert):
    with open("alerts.json", "r") as f:
        alerts = json.load(f)

    descr = alert.description
    lat = alert.lat
    lon = alert.lon
    time_created = str(datetime.now()).split(".")[0]

    alerts.append({"descr" : descr, "lat" : lat, "lon" : lon, "time_created" : time_created})
    
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)
        
    return {"success" : True}


@app.get("/view/{lon}/{lat}")
def view(lon : float, lat : float):
    with open("alerts.json", "r") as f:
        alerts = json.load(f)

    return sorted(alerts, key=sort_by_time, reverse=True) # was lambda x: pythagoras_sort({"lon" : lon, "lat" : lat}, x)


uvicorn.run(app,host="0.0.0.0",port="8080")