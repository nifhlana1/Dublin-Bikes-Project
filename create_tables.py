import sqlalchemy as sqla
from sqlalchemy import create_engine
import traceback
import glob
import os
from pprint import pprint
import simplejson as json
import requests
import time
from IPython.display import display


URI = "dbbikes.cqj4rrrshnza.us-east-1.rds.amazonaws.com"
PORT="3306"
DB="dublin_bikes"
USER="dbbikes1"
PASSWORD=""


# engine=create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)
engine=create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)



sql = """CREATE DATABASE IF NOT EXISTS dbbikes;"""
engine.execute(sql)

for res in engine.execute("SHOW VARIABLES;"):
    print(res)