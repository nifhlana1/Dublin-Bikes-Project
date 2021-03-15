from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import requests
import json


#DATABASE DETAILS
URI="dbbikes.cqj4rrrshnza.us-east-1.rds.amazonaws.com"
PORT="3306"
DB = "dbbikes"
USER="dbbikes1"
PASSWORD="dbbikes1"

#WEATHER API

weather_url = "https://prodapi.metweb.ie/observations/phoenix-park/today"
res = requests.get(weather_url).json()

#ENGINE
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
meta=MetaData()


##DYNAMIC SCRAPER

#Create table using ORM
weather_today = Table(
    'weather_today', meta,
    Column('name', String),
    Column('temperature', Integer),
    Column('carinalWindDirection', Integer),
    Column('humidity', Integer),
    Column('rainfall', Integer),
    Column('pressure', Integer),
    Column('dayName', String),
    Column('reportTime', DateTime)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

#Create table using ORM
weather_live_hist = Table(
    'weather_live_hist', meta,
    Column('name', String),
    Column('temperature', Integer),
    Column('carinalWindDirection', Integer),
    Column('humidity', Integer),
    Column('rainfall', Integer),
    Column('pressure', Integer),
    Column('dayName', String),
    Column('reportTime', DateTime)
)

#Create table. Create_all is conditional by default. Won't recreate a table already preent
meta.create_all(engine)

##Connection object to represent connection resource.
conn = engine.connect()

 def write_weather_to_db(text):
    weather = json.loads(text)
    print(type(weather), len(weather))
    for w in weather:
        print(station)
        vals = (station.get('number'), int(station.get('banking')),
                station.get('available_bikes'), int(station.get('bonus')),
                station.get('available_bikes_Stands'), station.get('name'),
                station.get('last_update'), station.get('position').get('lat'),
                )
        engine.execute("insert into availability values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
    return