import http.client
import mimetypes
import json


names_list = []

def get_securities(company_name,conn,payload,headers):
    conn.request("GET", f"/api/search/autocomplete?q={company_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    symbols_json = json.loads(data.decode("utf-8"))
    return [element["symbol"] for element in symbols_json["symbols"]]



def get_nse_price(company_name):
    conn = http.client.HTTPSConnection("www.nseindia.com")
    payload = ''
    headers = {
            'Cookie': ''
            }
    name_list = get_securities(company_name,conn,payload,headers)
    print(name_list)
    conn.request("GET", f"/api/quote-equity?symbol={name_list[0]}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    print(jdict["priceInfo"]["close"])
    return jdict["priceInfo"]["close"]

def get_bse_price(company_name):
    conn = http.client.HTTPSConnection("api.bseindia.com")
    payload = ''
    headers = {}
    conn.request("GET", "/BseIndiaAPI/api/StockReachGraph/w?scripcode=500209&flag=0&fromdate=&todate=&seriesid=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    print(jdict["CurrVal"])
    return jdict["CurrVal"]


company_name = input("enter company name::")
i = 1
while i < 10:
   result =  float(get_nse_price(company_name)) - float(get_bse_price("INFY"))
   print(result)
   i += 1