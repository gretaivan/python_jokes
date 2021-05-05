import requests
# from models import *
from models.joke import Joke 

def fetch_random_joke(): 
    URL = 'https://official-joke-api.appspot.com/random_joke'
    req = requests.get(URL)
    print(req.json())
    for data in req.json():
        Joke(data)
    return data

     
    # return Joke(req)
    
    # model: Joke(result)

# def get joke by type(type)
    #URL = f'njfkdbskjfs/{type}/aslnad


