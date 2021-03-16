import mysql.connector
import requests
import json
from datetime import datetime


print("trying to connect")
mydb = mysql.connector.connect(
    host="dublinbikes.chj6z1a17hdc.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Aws72gene!",
    database='DublinBikes',
    charset='utf8mb4',
 )

mycursor = mydb.cursor(dictionary=False)

print("Connected")

#Select all day records
sql_select_day = "SELECT DISTINCT DayOfWeek from DublinBikes.LiveHistoricalData"
cursor = mydb.cursor()
cursor.execute(sql_select_day)
# get all records
day_records = cursor.fetchall()
day_records = [(0,),]
print(day_records)

#Select all of the time records
sql_select_times = "SELECT DISTINCT TIME from DublinBikes.LiveHistoricalData"
cursor = mydb.cursor()
cursor.execute(sql_select_times)
# get all records
time_records = cursor.fetchall()

#Select all stations
sql_select_stations = "SELECT DISTINCT StationName from DublinBikes.LiveHistoricalData"
cursor = mydb.cursor()
cursor.execute(sql_select_stations)
# get all records
station_records = cursor.fetchall()
station_records = station_records[0]




"""The below prints out the average bike availability every day 
(at intervals of 5 minutes according to information in live_historic_availability)
, at every station."""

data = {}
for station in station_records:
    data[station] = {}
    print(data)
    station_var=str(station)
    for day in day_records:
        data[station][day[0]] = {}
        print(data)
        day_var = str(day[0])
        #Select query: average for every day and every time for station
        for i in time_records:
            #print(i[0])
            time_i = str(i[0])
            #print(time_i)
            cursor = mydb.cursor()
            sql_select_Query = "SELECT AVG(AvailableBikes) as AverageBikes FROM DublinBikes.LiveHistoricalData WHERE DayOfWeek=0 AND StationName='"+str(station_var)+"' AND Time = "+str(time_i)
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            data[station][day[0]][time_i] = str(records[0][0])



print(data)


#Convert the string with all of the averages into a json file and save
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


