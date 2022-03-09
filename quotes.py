import requests
import json
import time

def quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+ " - "+json_data[0]['a']
  return(quote)


while True:
    a = input("Click Enter")
    q = quote()
    print(q)
    time.sleep(1)
