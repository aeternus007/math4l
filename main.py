from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from datetime import datetime
import json

from utils import Alert, Coords, sort_by_time


app = FastAPI()

origins = [
    "http://math4l-1.aeternus007.repl.co",
    "https://math4l-1.aeternus007.repl.co",
    "http://lifesafer.netlify.app/view",
    "https://lifesafer.netlify.app/view",
    "http://lifesafer.netlify.app/create",
    "https://lifesafer.netlify.app/create",
    "http://0.0.0.0:80",
    "https://0.0.0.0:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create")
def create(alert : Alert):
    with open("alerts.json", "r") as f:
        alerts = json.load(f)

    descr = alert.descr
    lat = alert.lat
    lon = alert.lon
    time_created = str(datetime.now()).split(".")[0]

    alerts.append({"descr" : descr, "lat" : lat, "lon" : lon, "time_created" : time_created})
    
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)
        
    return {"success" : True}


@app.get("/view") # /{lon}/{lat}
def view(): # lon : float, lat : float
    with open("alerts.json", "r") as f:
        alerts = json.load(f)

    return sorted(alerts, key=sort_by_time, reverse=True) # was lambda x: pythagoras_sort({"lon" : lon, "lat" : lat}, x)


uvicorn.run(app, host="0.0.0.0", port="80")