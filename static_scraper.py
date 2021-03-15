import requests
import traceback
import datetime
import time
import sqlalchemy as sqla
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger
import traceback
import glob
import os
from pprint import pprint
import time
import requests
import json


#DATABASE DETAILS
#URI="dbbikes.cgz9bu4plq6e.us-east-1.rds.amazonaws.com"
URI="dbbikes.cqj4rrrshnza.us-east-1.rds.amazonaws.com"
PORT="3306"
DB = "dbbikes"
#USER = "aine"
USER="dbbikes1"

#PASSWORD = "ainedbbikes"
PASSWORD="dbbikes1"

#DUBLIN BIKES API CONNECTION
APIKEY = "c003ff338508fcee56ace550c4cd05659b717e61"
NAME = "dublin"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"

res = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})

#ENGINE
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
meta=MetaData()


#INSERT INTO STATIONS TABLE
#If the length of rows in station table  is zero, insert the rows FROM jcdECAUX
def stations_to_db(text):
    stations = json.loads(text)
    print(type(stations), len(stations))
    for station in stations:
        print(station)
        vals = (station.get('address'), int(station.get('banking')),
                station.get('bike_stands'), int(station.get('bonus')),
                station.get('contract_name'), station.get('name'),
                station.get('number'), station.get('position').get('lat'),
                station.get('position').get('lng'), station.get('status')
                )

        engine.execute("insert into station values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
    return

stations_to_db(res.text)


##DYNAMIC SCRAPER

#Creat availability table using ORM
availability = Table(
    'availability', meta,
    Column('number', Integer, primary_key=True),
    Column('available_bikes', Integer),
    Column('available_bike_stands', Integer),
    Column('last_update', Integer)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

#Creat live_historic_availability table using ORM
live_historic_avail = Table(
    'live_historic_avail', meta,
    #Note, number not a primary key here as will have repeated values
    Column('number', Integer),
    Column('available_bikes', Integer),
    Column('available_bike_stands', Integer),
    Column('last_update', BigInteger)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

##Connection object to represent connection resource.
conn = engine.connect()


#Insert into the availability table using sql alchemy object relational mapping

# def write_avail_to_db(text):
#     stations = json.loads(text)
#     print(type(stations), len(stations))
#     for station in stations:
#         #print(station)
#         print({key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}})
#         station = {key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}}
#         print(type(station))
#
#
#         ins = availability.insert().values(station)
#         print(ins)
#         conn.execute(ins)
#
#     return

#Execute the insert
#write_avail_to_db(res.text)




def write_to_file(text):
    with open("data/bikes_{}".format(now).replace(" ","_"),"w") as f:
        f.write(r.text)





##Unused insert into availability table using SQL
# def write_avail_to_db(text):
#     stations = json.loads(text)
#     print(type(stations), len(stations))
#     for station in stations:
#         print(station)
#         vals = (station.get('number'), int(station.get('banking')),
#                 station.get('available_bikes'), int(station.get('bonus')),
#                 station.get('available_bikes_Stands'), station.get('name'),
#                 station.get('last_update'), station.get('position').get('lat'),
#                 )
#         engine.execute("insert into availability values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
#     return
#





