import requests

def get_leaders():
    leaders_dict = {}
    url = "https://country-leaders.herokuapp.com"
    countries = url + "/countries"
    cookies_u = url + "/cookie"
    leaders = url + "/leaders" 
    cookie = requests.get(cookies_u).cookies
    countries = requests.get(countries, cookies=cookie).json()
    for country in countries :
        param_country = "country=" + country
        leaders = requests.get(leaders, cookies=cookie, params=param_country).json()
        for leader in leaders:
            leaders_dict.setdefault(country, []).append(leader)
    return leaders_dict

get_leaders()
