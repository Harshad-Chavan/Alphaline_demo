import http.client
import mimetypes
from bs4 import BeautifulSoup
conn = http.client.HTTPSConnection("api.bseindia.com")
payload = ''
headers = {}
conn.request("GET", "/Msource/1D/getQouteSearch.aspx?Type=EQ&text=infosys&flag=nw", payload, headers)
res = conn.getresponse()
data = res.read()
parsed_html = BeautifulSoup(data)
l = parsed_html.find_all('span',attrs = {'class' : ''})
for x in l:
    print(x)




# print(data.decode("utf-8"))