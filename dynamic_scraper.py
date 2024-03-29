#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, DateTime
import requests
import json
from datetime import datetime


#DATABASE DETAILS
#URI="dbbikes.cgz9bu4plq6e.us-east-1.rds.amazonaws.com"
URI="dbbikes.cqj4rrrshnza.us-east-1.rds.amazonaws.com"
PORT="3306"
DB = "dbbikes"
#USER = "aine"
#PASSWORD = "ainedbbikes"
USER="dbbikes1"
PASSWORD="dbbikes1"

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
    Column('last_update', BigInteger),
    Column('current_time', Integer),
    Column('day', Integer),
    Column('date', DateTime)
)

#Create table using ORM
live_historic_avail = Table(
    'live_historic_avail', meta,
    Column('number', Integer),
    Column('available_bikes', Integer),
    Column('available_bike_stands', Integer),
    Column('last_update', BigInteger),
    Column('current_time', Integer),
    Column('day', Integer),
    Column('date',DateTime)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

##Connection object to represent connection resource.
conn = engine.connect()

##If the table already has rows, delete them all
trans = conn.begin()
conn.execute("truncate table availability")
trans.commit()

#Insert into the availability table using sql alchemy object relational mapping
now = datetime.now()
current_time = now.strftime("%H%M") #time as a 3-4 sequence of numbers
day = datetime.today().weekday() #produces an int value for day of the week
date = now.strftime("%Y-%m-%d") #probably not going to be used computationally, just for our benefit

def write_avail_to_db(text):
    stations = json.loads(text)
    print(type(stations), len(stations))
    for station in stations:
        #print(station)
        print({key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}})
        station = {key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}}
        print(type(station))
        ins = availability.insert().values(station,current_time=current_time, day=day, date=date)
        conn.execute(ins)
        print(ins)


    return

write_avail_to_db(res.text)



##--------LIVE_HISTORIC AVAILABILITY TABLE----



#Create table. Create_all is conditional by default. Won't recreate a table already preent
# meta.create_all(engine)
#
# ##Connection object to represent connection resource.
# conn = engine.connect()




#Insert into the live_historic_avail table

def write_avail_to_histdb(text):
    stations = json.loads(text)
    print(type(stations), len(stations))
    for station in stations:
        #print(station)
        print({key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}})
        station = {key:station[key] for key in station.keys() & {'number','available_bikes','available_bike_stands','last_update'}}
        print(type(station))
        ins = live_historic_avail.insert().values(station,current_time=current_time, day=day, date=date)
        #print(ins)
        conn.execute(ins)

    return

write_avail_to_histdb(res.text)

