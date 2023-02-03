import requests
import logging

try:
    response = requests.get("https://swapi.dev/api/people/1/", timeout = 0.5)
    # print(response.content)
except requests.ReadTimeout as e:
    # logging.basicConfig(level=logging.INFO)
    logging.error(e, exc_info=True)
    
    
    # r = requests.request('GET', "https://swapi.dev/api/people/1/")
# print(r.content)

# response = requests.get("https://swapi.dev/api/people/1/")
# print(response.content)


# r = requests.post("https://swapi.dev/api/people/1/", data = {'name': 'programmer'})
# print(r.status_code)