import http.client
import mimetypes
import json
import re
from bs4 import BeautifulSoup


names_list = []

def get_securities(company_name):

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

    #fetching from nse 
    conn_nse.request("GET", f"/api/search/autocomplete?q={company_name}", payload_nse, headers_nse)
    res = conn_nse.getresponse()
    data = res.read()
    symbols_json = json.loads(data.decode("utf-8"))
    nse_list = [element["symbol"] for element in symbols_json["symbols"]]
    print(nse_list)

    #fetching from bse
    bse_list = []
    conn_bse.request("GET", f"/Msource/1D/getQouteSearch.aspx?Type=EQ&text={company_name}&flag=nw", payload_bse, headers_bse)
    res = conn_bse.getresponse()
    data = res.read()
    parsed_html = BeautifulSoup(data,'html.parser')
    l = parsed_html.find_all('span',attrs = {'class' : ''})
    for sym in l:
        ns = (str(sym).replace("<span>","").replace("</span>","").replace("<strong>","").replace("</strong>",""))
        ls = re.search('(\w*)',ns).group(1)
        bse_list.append(ls)

    #returning only the common securities on both the exchanges
    return (set(nse_list) & set(bse_list))








# def get_nse_price(company_name):
#     conn = http.client.HTTPSConnection("www.nseindia.com")
#     payload = ''
#     headers = {
#             'Cookie': ''
#             }
#     name_list = get_securities(company_name,conn,payload,headers)
#     print(name_list)
#     conn.request("GET", f"/api/quote-equity?symbol={name_list[0]}", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     jdict = json.loads(data.decode("utf-8"))
#     print(jdict["priceInfo"]["close"])
#     return jdict["priceInfo"]["close"]

# def get_bse_price(company_name):
#     conn = http.client.HTTPSConnection("api.bseindia.com")
#     payload = ''
#     headers = {}

#     conn.request("GET", "/BseIndiaAPI/api/StockReachGraph/w?scripcode=500209&flag=0&fromdate=&todate=&seriesid=", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     jdict = json.loads(data.decode("utf-8"))
#     print(jdict["CurrVal"])
#     return jdict["CurrVal"]


company_name = input("enter company name::")
print(get_securities(company_name.lower()))


# i = 1
# while i < 10:
#    result =  float(get_nse_price(company_name)) - float(get_bse_price("INFY"))
#    print(result)
#    i += 1