import json
import requests

data = json.dumps({'name':'Aditya'})
res = requests.post('http://127.0.0.1:10001/api', data)
print(res.text)
