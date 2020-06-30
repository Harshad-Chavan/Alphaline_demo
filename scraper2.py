import http.client
import mimetypes
import json
import re
from bs4 import BeautifulSoup
import time


names_list = []

def get_securities(company_name):
    securities = {}
    #NSE connection settings
    conn_nse = http.client.HTTPSConnection("www.nseindia.com")
    payload_nse = ''
    headers_nse = {
            'Cookie': ''
            }

    #BSE connection settings
    conn_bse = http.client.HTTPSConnection("api.bseindia.com")
    payload_bse = ''
    headers_bse = {}


    #Fetching all securities with name containing the given string

    #fetching from bse
    bse_list = []
    conn_bse.request("GET", f"/Msource/1D/getQouteSearch.aspx?Type=EQ&text={company_name}&flag=nw", payload_bse, headers_bse)
    res = conn_bse.getresponse()
    data = res.read()
    parsed_html = BeautifulSoup(data,'html.parser')
    l = parsed_html.find_all('span',attrs = {'class' : ''})
    for sym in l:
        ns = (str(sym).replace("<span>","").replace("</span>","").replace("<strong>","").replace("</strong>",""))
        symbols = re.search('^([A-Z-0-9]*)',ns).group(1)
        scripcodes = re.search('([A-Z-0-9]*)$',ns).group(1)
        bse_list.append((symbols,scripcodes))
        securities[symbols] = scripcodes
    print(bse_list)

    #fetching from nse 
    conn_nse.request("GET", f"/api/search/autocomplete?q={company_name}", payload_nse, headers_nse)
    res = conn_nse.getresponse()
    data = res.read()
    symbols_json = json.loads(data.decode("utf-8"))
    for element in symbols_json["symbols"]:
        if element['symbol'] in list(securities.keys()):
            print("present")
        else:
            print("not present")

    #returning only the common securities on both the exchanges
    return securities


def compute_difference(temp,selected_symbol):
    #fetching nse price
    nse_price = float(get_nse_price(selected_symbol))
    #fetching bse price
    bse_price = float(get_bse_price(temp[selected_symbol]))
    maxm = max(nse_price,bse_price)
    minm = min(nse_price,bse_price)
    print(f"difference in price == : { maxm - minm }")
    

def get_nse_price(company_name):
    conn = http.client.HTTPSConnection("www.nseindia.com")
    payload = ''
    headers = {
            'Cookie': ''
            }
    conn.request("GET", f"/api/quote-equity?symbol={company_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    print(jdict["priceInfo"]["close"])
    return jdict["priceInfo"]["close"]

def get_bse_price(scripcode):
    conn = http.client.HTTPSConnection("api.bseindia.com")
    payload = ''
    headers = {}

    conn.request("GET", f"/BseIndiaAPI/api/StockReachGraph/w?scripcode={scripcode}&flag=0&fromdate=&todate=&seriesid=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jdict = json.loads(data.decode("utf-8"))
    print(jdict["CurrVal"])
    return jdict["CurrVal"]


company_name = input("enter company name::")
securities = get_securities(company_name.lower())
symbol_name = input("select a symbol from above list::")

i = 1
while i < 10:
    time.sleep(1)
    compute_difference(securities,symbol_name)
    i += 1


