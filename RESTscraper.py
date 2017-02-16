import requests
import json

get_url = "https://api.nvite.com/events/sjsu/guests"
get_response = requests.get(get_url)
json_response = json.loads(get_response.content)

names = ""
for data in json_response['guests']:
    names += data['profile']['name'] + "\n"
    print "Name: " + data['profile']['name']
    print "Description: " + data['profile'].get('description', 'Null')
    print "Location: " + data['profile'].get('location', 'Null')
    if data['service'] == "email":
        print "Registerd via: Email"
    elif data['service'] == "facebook":
        print "Profile: " + "https://www.facebook.com/" + data['profile']['handles']['facebook']
    elif data['service'] == "linkedin":
        print "Profile: " + "https://www.linkedin.com/in/" + data['profile']['handles']['linkedin']
    elif data['service'] == "twitter":
        print "Profile: " + "https://twitter.com/" + data['profile']['handles']['twitter']

    print "\n"

# To remove the last character i.e. "\n" in this case
names = names[:-1]

outfile = open('output.txt', 'w')
outfile.write(names)
outfile.close()
