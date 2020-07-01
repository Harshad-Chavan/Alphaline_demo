from datetime import datetime, timedelta
import time
nse = 1593594900000
temp = datetime.utcfromtimestamp(nse / 1000)
time_diff = 59
for x in range(1,10):
    nse_time = (temp + timedelta(seconds=time_diff)).strftime('%H:%M:%S') 


bse = "Wed Jul 01 2020 09:15:59" 
bse_time = (datetime.strptime(bse, "%a %b %d %Y %H:%M:%S")).time()

print(str(bse_time))
print(type(nse_time))

print(str(bse_time) == nse_time)