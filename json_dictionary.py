import json


text = '{"name":"farook", "salary":50000}'

data = json.loads(text)

print(data["name"])

