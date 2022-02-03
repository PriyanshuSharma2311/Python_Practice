import json
import urllib.request as url

response = url.urlopen('https://api.covid19india.org/states_daily.json')
data = json.load(response)

states = data['states_daily']

confirmed = []
recovered = []
deceased = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered.append(states[i])
    else:
        deceased.append(states[i])

