import http.client
import mimetypes
import json
import time
from datetime import datetime, timedelta


security = {}
security_obj = { "nseprice" : 0 , "bseprice" : 0 , "diffprice": 0 }

def get_conn(site):
    #NSE connection settings
    if site == "nse":
        conn_nse = http.client.HTTPSConnection("www.nseindia.com")
        payload_nse = ''
        headers_nse = {
            'Cookie': ''
            }
        return conn_nse,payload_nse,headers_nse
    
    #BSE connection settings
    elif site == 'bse':
        conn_bse = http.client.HTTPSConnection("api.bseindia.com")
        payload_bse = ''
        headers_bse = {}
        return conn_bse,payload_bse,headers_bse


def get_nse_data():
    #fetching graph data from nse
    conn,payload,headers = get_conn('nse')
    conn.request("GET", "https://www.nseindia.com/api/chart-databyindex?index=TCSEQN", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    nse_data = jdict["grapthData"]
    return nse_data



def get_bse_data():
    #fetching graph data from bse
    conn,payload,headers = get_conn('bse')
    conn.request("GET", "/BseIndiaAPI/api/StockReachGraph/w?scripcode=532540&flag=0&fromdate=&todate=&seriesid=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    bse_data = json.loads(jdict["Data"])
    return bse_data
  

def getbserecord(bse_data):
    for data in bse_data:
        time_str = data['dttm']
        time_obj = time.strptime(time_str[:-3], "%a %b %d %Y %H:%M") 
        time_inepoch = time.mktime(time_obj)
        curr_time = (datetime.fromtimestamp(time_inepoch))
        yield curr_time,data["vale1"]


def compute_price(nse_data,bse_data):
    seq = getbserecord(bse_data)
    intial_bse,bse_price = next(seq)
    for x in nse_data :
       curr_time = (datetime.utcfromtimestamp(x[0] / 1000.0)).strftime('%Y-%m-%d %H:%M:%S')[:-3]
       curr_time = datetime.strptime(curr_time, "%Y-%m-%d %H:%M")
       if curr_time == intial_bse:
            security[curr_time.strftime('%H:%M:%S')] = { "nseprice" : x[1] , "bseprice" : float(bse_price) , "diffprice": x[1] - float(bse_price) } 
            intial_bse,bse_price = next(seq)
            
            
compute_price(get_nse_data(),get_bse_data())
for x in security.items():
    print(x)  

    
