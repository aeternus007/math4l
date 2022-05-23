from pydantic import BaseModel

from datetime import datetime
from math import sqrt

class Alert(BaseModel):
    descr : str
    lat : float
    lon : float


class Coords(BaseModel):
    lat : float
    lon : float


def pythagoras_sort(location, item):
    delta_x = (location["lon"] - item["lat"]) ** 2
    delta_y = (location["lon"] - item["lat"]) ** 2

    return sqrt((delta_x + delta_y))


def sort_by_time(item):
    return datetime.strptime(item["time_created"], '%Y-%m-%d %H:%M:%S')