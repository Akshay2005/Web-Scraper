import requests
import json

get_url = "https://api.nvite.com/events/sjsu/guests"
get_response = requests.get(get_url)
json_response = json.loads(get_response.content)

names = ""
for data in json_response['guests']:
    names += data['profile']['name'] + "\n"
    print data['profile']['name']

#To remove the last character i.e. "\n" in this case
names = names[:-1]

outfile = open('output.txt', 'w')
outfile.write(names)
outfile.close()
