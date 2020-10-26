import pytest
import json
import requests

def presidents():
    query = "Presidents of the United States"
    ddg_api_url = 'http://api.duckduckgo.com/?q='+query+'&format=json'
    response = requests.get(ddg_api_url)
    r2 = response.json()
    r3 = r2["RelatedTopics"]
    po = r3[0]
    presLyst= ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison",
           "Tyler", "Polk", "Taylor", "Filmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
           "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
           "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Reagan", "Bush", "Clinton", "Obama", "Trump"]
    c1 = 0
    c2 = 0
    for i in presLyst:
        for k in presLyst:
            if (i in po["Result"]):
                print(presLyst[c1])
                print("True")
                c1 = c1 + 1
        po = r3[c2]
        c2 = c2 + 1
presidents()

def test_duck():
    query = "Presidents of the United States"
    ddg_api_url = 'http://api.duckduckgo.com/?q='+query+'&format=json'
    response = requests.get(ddg_api_url)
    r2 = response.json()
    r3 = r2["RelatedTopics"]
    presLyst= ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison",
           "Tyler", "Polk", "Taylor", "Filmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
           "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
           "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Reagan", "Bush", "Clinton", "Obama", "Trump"]
    po = r3[0]
    c1 = 0
    c2 = 0
    for i in presLyst:
        for k in presLyst:
            if (i in po["Result"]):
                assert i in po["Result"]
                c1 = c1 + 1
        po = r3[c2]
        c2 = c2 + 1



