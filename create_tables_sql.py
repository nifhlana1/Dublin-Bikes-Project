import sqlalchemy as sqla
from sqlalchemy import create_engine
import traceback
import glob
import os
from pprint import pprint
import time
import requests
import json


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

#CREATE ENGINE
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)

#CREATE TABLES
sql = """CREATE DATABASE IF NOT EXISTS dbbikes;"""
engine.execute(sql)

# Create 'station' table
sql = """
CREATE TABLE IF NOT EXISTS station (
address VARCHAR(256),
banking INTEGER,
bike_stands INTEGER,
bonus INTEGER,
contract_name VARCHAR(256),
name VARCHAR(256),
number INTEGER,
position_lat REAL,
position_lng REAL,
status VARCHAR(256)
)
"""

try:
    res = engine.execute("DROP TABLE IF EXISTS station")
    res = engine.execute(sql)
    print(res.fethcall())
except Exception as e:
    print(e)


# Create 'availability' table

sql = """CREATE TABLE IF NOT EXISTS availability (
number INTEGER,
available_bikes INTEGER,
available_bike_Stands INTEGER,
last_update INTEGER
)"""

try:
    res=engine.execute(sql)
    print(res.fetchall())
except Exception as e:
    print(e)









