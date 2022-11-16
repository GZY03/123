import requests

def BaiduQuery(address, city, currentkey):
  """
  :param address: address
  :param currentkey: AK
  """
  url = 'http://api.map.baidu.com/geocoding/v3/?'
  params = {
    "address": address,
    "city": city,
    "output": 'json',
    "ak": currentkey,
  }
  response = requests.get(url, params=params)
  answer = response.json()
  print(answer)


if __name__ == '__main__':
    BaiduQuery('陆家嘴','上海','mvmAhnmuDjilwgYRDRwWaGYqRTXnoMuY')