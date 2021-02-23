import requests
import json






##STATIC DATA - GET STATIONS IN DUBLIN
NAME="Dublin" # name of contract
STATIONS="https://api.jcdecaux.com/vls/v1/stations" # and the JCDecaux endpoint
APIKEY = "c003ff338508fcee56ace550c4cd05659b717e61"


r = requests.get(STATIONS, params={"apiKey": APIKEY,"contract": NAME})
#Print status code of the request
print(r.status_code)
#Print the data that was retrieved
print(r.json())



def jprint(obj):
 '''##Json.loads: takes a JSON string and
 converts (loads) it to a Python object'''
 text = json.dumps(obj, sort_keys=True, indent=4)
 print(text)

jprint(r.json())




#GET STATION LIST
# NAME="Dublin" # name of contract
# STATIONS="https://api.jcdecaux.com/vls/v1/stations" # and the JCDecaux endpoint
# STATION_NUM = 42
# STATION_NAME = "SMITHFIELD NORTH"
# APIKEY = "c003ff338508fcee56ace550c4cd05659b717e61"
#
#
# r_41 = requests.get(STATIONS, params={"apiKey": APIKEY, "contract_name": "dublin"})
# #Print status code of the request
# print(r_41.status_code)
# #Print the data that was retrieved
# print(r_41.json())






#REQUEST INFORMATION FOR STATION NUMBER X
# NAME="Dublin" # name of contract
# STATIONS="https://api.jcdecaux.com/vls/v1/stations/{station_number}?contract={contract_name}" # and the JCDecaux endpoint
# STATION_NUM = 42
# STATION_NAME = "SMITHFIELD NORTH"
# APIKEY = "c003ff338508fcee56ace550c4cd05659b717e61"
#
#
# r_42 = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME, "station_number": STATION_NUM})
# #Print status code of the request
# print(r_42.status_code)
# #Print the data that was retrieved
# print(r_42.json())









#CODE/FUNCTION FROM LECTURE SLIDES:

# def main():
#
#  with open()

 # run forever...
 # while True:
 #  try:
 #    r = requests.get(STATIONS,
 #     params={"apiKey": APIKEY, "contract": NAME})
 #
 #     store(json.loads(r.text))
 #
 #    # now sleep for 5 minutes
 #    time.sleep(5*60)
 #  except:
 #        # if there is any problem, print the traceback
 #     print traceback.format_exc()
 #  return