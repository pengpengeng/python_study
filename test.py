# -*- coding: UTF-8 -*-
import requests

url = "https://test.fameex.com/userapi/wallet/l2c/return"

payload = "{\"coinPair\":\"BNB/USDT\",\"coinType\":\"BNB\",\"recordId\":\"\",\"returnAmount\":\"1\"}"
headers = {
  'AuthorizationId': '0f5cdcfc-1bbd-4c86-82bc-2ea6a56c65b5',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOiIxNTk4NTc5OTUwMjI5NDQ5NDQ1IiwiaWF0IjoiMCIsInVzZXJJZCI6IjQzMTIwMzE1In0.6b7G2BCU1dXSgaIJAMehtFRi4atwVzPqkiIjcLmc3oM',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)
a=True
print(range(2,10,2))
    