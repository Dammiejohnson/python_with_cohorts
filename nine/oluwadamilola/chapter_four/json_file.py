import json
data = open("/home/catalyst/Downloads/user_data.json", "r+")
data= json.load(data)

print(data)

# hello_str = 'hello world';
# print(hello_str[3:-2])