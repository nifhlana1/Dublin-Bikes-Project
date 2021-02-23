#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import requests
import json


#DATABASE DETAILS
URI="dbbikes.cgz9bu4plq6e.us-east-1.rds.amazonaws.com"
PORT="3306"
DB = "dbbikes"
USER = "aine"
PASSWORD = "ainedbbikes"

#DUBLIN BIKES API CONNECTION
APIKEY = "c003ff338508fcee56ace550c4cd05659b717e61"
NAME = "dublin"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"

res = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})

#ENGINE
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
meta=MetaData()


##DYNAMIC SCRAPER

#Create table using ORM
availability = Table(
    'availability', meta,
    Column('number', Integer, primary_key=True),
    Column('available_bikes', Integer),
    Column('available_bike_stands', Integer),
    Column('last_update', Integer)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

##Connection object to represent connection resource.
conn = engine.connect()

#Insert into the availability table using sql alchemy object relational mapping

def write_avail_to_db(text):
    stations = json.loads(text)
    print(type(stations), len(stations))
    for station in stations:
        #print(station)
        print({key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}})
        station = {key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}}
        print(type(station))
        ins = availability.insert().values(station)
        print(ins)
        conn.execute(ins)

    return

write_avail_to_db(res.text)