import http.client
import mimetypes
from bs4 import BeautifulSoup
import re

names_list = []
conn = http.client.HTTPSConnection("api.bseindia.com")
payload = ''
headers = {}
conn.request("GET", "/Msource/1D/getQouteSearch.aspx?Type=EQ&text=infosys&flag=nw", payload, headers)
res = conn.getresponse()
data = res.read()
parsed_html = BeautifulSoup(data,'html.parser')
l = parsed_html.find_all('span',attrs = {'class' : ''})
regex = "<span>([A-z,0-9,-]*)"
for x in l:
    m = re.search(regex,str(x))
    names_list.append(m.group(1))
    
    
print(names_list)



# print(data.decode("utf-8"))