import requests
import urllib.parse
from urllib.request import Request, urlopen
import json

def pocket_articles():
    # Contact API
    consumer_ID = "91475-35c85f4e35ae67ce6c3b3e63"
    request_token = "050ef980-d5be-feaa-4ea4-afb32c"
    access_token ="70f96a8f-1ed4-1026-21db-92fe07"

    parameters = {"consumer_key":"91475-35c85f4e35ae67ce6c3b3e63","access_token":"70f96a8f-1ed4-1026-21db-92fe07", "favorite":1, "detailType":"simple"}

    response = requests.get("https://getpocket.com/v3/get",params=parameters)
    ##print(response.json())

    decoded = response.json()

    favorite_articles = {}

    j=0
    for i in decoded["list"].values():
        favorite_articles[j]= {'title': i["resolved_title"], 'url': i["resolved_url"]}
        j=j+1

    return favorite_articles

    ##for i in favorite_articles:
        ##print(favorite_articles[i]['title'], "\t", favorite_articles[i]['url'])
