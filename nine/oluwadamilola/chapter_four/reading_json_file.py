import json
from this import d
json_data = open('/home/catalyst/Downloads/user_data.json', "r+")
data = json.load(json_data)

for i in data:
    print(i)
    print()
    print()

