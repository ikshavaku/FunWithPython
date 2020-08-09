#!/usr/bin/python3

import json
import requests

r= requests.get("https://jsonplaceholder.typicode.com/todos")
print(r)
todos=json.loads(out.txt)