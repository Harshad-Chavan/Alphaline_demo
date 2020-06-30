import http.client
import mimetypes
import json
import threading

company_name = input("enter company name::")

def get_securities(company_name,cookie,conn,payload,headers):
    conn.request("GET", f"/api/search/autocomplete?q={company_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    symbols_json = json.loads(data.decode("utf-8"))
    return [element["symbol"] for element in symbols_json["symbols"]]



def get_nse_price(company_name):
    cookie_nse = 'ak_bmsc=47F99B9504B73A055C1376BF5B8F265517D4FEECC35E0000A835FB5EA945DB40~pl0X4AcPh7ZTvtT5sMZAP2uyLExRqCbIlA3qf28SDRvVP1iKULxVAC64s097/J1o1mwJQ+hfwobE41vo+ZPeI/GJu7qbAa+knKdGvmQtU6NvFvq3QLbLxZgsE3c9HvHbtyf1rfu6fSzbzgCfsBXliGeT4QylqzzZp6NHAuUv9O1J+si5UpNECoIw2i6gOzOcHUJprFdMDZCvYpdT6VH9DrMKt8e85UOQBgayZZi6rt1Ac='
    conn = http.client.HTTPSConnection("www.nseindia.com")
    payload = ''
    headers = {
            'Cookie': cookie_nse
            }
    name_list = get_securities(company_name,cookie_nse,conn,payload,headers)
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


i = 1
while i < 10:
   result =  float(get_nse_price(company_name)) - float(get_bse_price("INFY"))
   print(result)
   i += 1