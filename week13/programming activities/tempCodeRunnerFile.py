import json
import requests
url = 'https://www.baidu.com'
req = requests.get(url)
print(req.text)