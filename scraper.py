import requests

url = "https://www.nseindia.com/api/quote-equity?symbol=INFY"

payload = {}
headers = {
  'Cookie': 'ak_bmsc=47F99B9504B73A055C1376BF5B8F265517D4FEECC35E0000A835FB5EA945DB40~pl0X4AcPh7ZTvtT5sMZAP2uyLExRqCbIlA3qf28SDRvVP1iKULxVAC64s097/J1o1mwJQ+hfwobE41vo+ZPeI/GJu7qbAa+knKdGvmQtU6NvFvq3QLbLxZgsE3c9HvHbtyf1rfu6fSzbzgCfsBXliGeT4QylqzzZp6NHAuUv9O1J+si5UpNECoIw2i6gOzOcHUJprFdMDZCvYpdT6VH9DrMKt8e85UOQBgayZZi6rt1Ac='
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



