import requests
params = {
    "ak": 'mvmAhnmuDjilwgYRDRwWaGYqRTXnoMuY',
}
r = requests.get('http://api.map.baidu.com/geocoding/v3/?a=深圳', params=params)
loc = r.json()
print(loc)