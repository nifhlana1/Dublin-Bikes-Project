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




"""The below prints out the average bike availability every day 
(at intervals of 5 minutes according to information in live_historic_availability)
, at every station."""

data = []
for station in station_records:
    print("'{")
    data.append("{")
    data.append(station[0])
    print(station[0])
    station_var=str(station[0])
    for day in day_records:
        print("{")
        data.append("{"+str(day[0])+"{")
        print(day[0])
        print("{")
        day_var = str(day[0])
        #Select query: average for every day and every time for station
        for i in time_records:
            #print(i[0])
            time_i = str(i[0])
            #print(time_i)
            cursor = mydb.cursor()
            sql_select_Query = "SELECT AVG(AvailableBikes) as AverageBikes FROM DublinBikes.LiveHistoricalData WHERE DayOfWeek="+day_var+" AND StationName='"+str(station_var)+"' AND Time = "+str(time_i)
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print(str(time_i)+":"+str(records[0][0]))
            data.append(str(time_i)+":"+str(records[0][0])+",")
        print("}}")
        data.append("}}")

    print("}")
    data.append("}")
print("}")
data.append("}'")



#Convert the string with all of the averages into a json file and save
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)















# sql_select_Query = "SELECT AVG(AvailableBikes) as AverageBikes FROM DublinBikes.LiveHistoricalData "\
#                    "WHERE DayOfWeek=4 " \
#                    "AND StationNumber=2 " \
#                    "AND Time = 1605"
# cursor = mydb.cursor()
# cursor.execute(sql_select_Query)
# # get all records
# records = cursor.fetchall()



#
# for row in records:
#     print("{")
#     print('StationNumber:',row[0])
#     print('StationName:',row[1])
#     print('BikeStands:',row[2])
#     print('AvailableBikeStands:',row[3])
#     print('AvailableBikes:',row[4])
#     print('Status:',"'"+row[5]+"'")
#     print('Time:',row[6])
#     print('DayOfWeek:', row[7])
#     print('Date:', row[8])
#     print("}")


