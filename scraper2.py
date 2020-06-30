import http.client
import mimetypes
import json
import threading

def get_nse_price(company_name):
    cookie_nse = 'ak_bmsc=47F99B9504B73A055C1376BF5B8F265517D4FEECC35E0000A835FB5EA945DB40~pl0X4AcPh7ZTvtT5sMZAP2uyLExRqCbIlA3qf28SDRvVP1iKULxVAC64s097/J1o1mwJQ+hfwobE41vo+ZPeI/GJu7qbAa+knKdGvmQtU6NvFvq3QLbLxZgsE3c9HvHbtyf1rfu6fSzbzgCfsBXliGeT4QylqzzZp6NHAuUv9O1J+si5UpNECoIw2i6gOzOcHUJprFdMDZCvYpdT6VH9DrMKt8e85UOQBgayZZi6rt1Ac='
    conn = http.client.HTTPSConnection("www.nseindia.com")
    payload = ''
    headers = {
            'Cookie': cookie_nse
            }
    conn.request("GET", f"/api/quote-equity?symbol={company_name}", payload, headers)
    res = conn.getresponse()
    
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    return jdict["priceInfo"]["close"]

def get_bse_price(company_name):
    conn = http.client.HTTPSConnection("api.bseindia.com")
    payload = ''
    headers = {}
    conn.request("GET", "/BseIndiaAPI/api/StockReachGraph/w?scripcode=500209&flag=0&fromdate=&todate=&seriesid=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    return jdict["CurrVal"]

i = 1
while i < 10:
   result =  float(get_nse_price("INFY")) - float(get_bse_price("INFY"))
   print(result)
   i += 1