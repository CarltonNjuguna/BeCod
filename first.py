import requests

url = "https://country-leaders.herokuapp.com"
status_url = url + "/status"
req = requests.get(status_url)
print(req.text) if req.ok else print(req)

country_url = url + "/countries"
req = requests.get(country_url)
countries = requests.get(country_url).json()
print(req.text) if req.ok else print(req)
print(countries)

cookies_url = url + "/cookie"
req = requests.get(cookies_url)
print(req.text) if req.ok else print(req)
cookie = req.cookies
print(cookie)
req = requests.get(country_url, cookies=cookie)
print(req.text)
print(req.json())

req = requests.get(url + "/leaders")
print(req,req.text,req.json())
param = 'fr'
req = requests.get(url + "/leaders", cookies=cookie, params=param)
print(req,req.text,req.json())



