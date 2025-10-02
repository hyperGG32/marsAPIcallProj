import os
import requests
from dotenv import load_dotenv
load_dotenv("APIKEY.env")

api_key = os.getenv("API_KEY") # a fancy way of hiding API key from public
api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
"""query_mode = 'sol'
if query_mode == 'sol':
    query_sol = 0"""
api_params = {}
if len(api_params) > 0:
    api_url += '?'
    for i in api_params:
        api_url += i
        api_url += "&"

rovers_set = {"curiosity", "opportunity", "spirit"}
curiosity_cam_set = {"FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM"}
opportunity_cam_set = {"FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"}
spirit_cam_set = {"FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"}

def data():
    call_url = api_url
    if not len(api_params) > 0:
        call_url += '?api_key=' + api_key
    else:
        call_url += '&api_key=' + api_key

    d = requests.get(call_url)
    data = d.json()
    return data


for i in data():
    print(i,":", end="\n\t")
    for n in data()[i]:
        for p in n:
            if p == "cameras":
                print("cameras :\n\t\t\t", end="", sep='')
                for j in n[p]:
                    for b in j:
                        print(b, ": ", j[b], end="\n\t\t\t", sep='')
            else:
                print(p, ": ", n[p], end="\n\t\t", sep='')
        print(end="\n\t")
"""request.get(api_url + rover + '/photo&sol=' + str(sol) + '&camera=' + camera + '&api_key=' + api_key"""

