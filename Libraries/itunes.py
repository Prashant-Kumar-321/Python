import json 
import requests
import sys 

if len(sys.argv) != 2: 
    sys.exit()


singer = sys.argv[1]

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={singer}")

# print(response.status_code)
# if response.status_code == 200: 

data = response.json()
# data_str = json.dumps(data, indent=2)
# print(data_str)

for result in data["results"]: 
    print(result["trackName"])