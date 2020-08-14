import json
with open("test_scripts/config.json",'r') as f:
    data=json.loads(f.read())
    print(data['db'])