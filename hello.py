from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H%M") #time as a 3-4 sequence of numbers
day = datetime.today().weekday() #produces an int value for day of the week
date = now.strftime("%Y-%m-%d") #probably not going to be used computationally, just for our benefit


print(date)