import csv
import google_web_search as search
from time import sleep
import random
import json


def saveDataChance(data):
    if int(random.random()*10) == 5:
        saveData(data)

def saveData(data):
    print 'saving'
    with open(filename, 'wb') as outfile:
        stuff = json.dump(data, outfile, indent = 4)

def getJSONData(filename):
    try:
        with open(filename) as readfile:
            data = json.load(readfile)
        return data   
    except:
        return {}

filename = 'urls_no_wiki_google'
data = getJSONData(filename)
gws = search.GoogleWebSearch()


with open('city_state.csv', 'rU') as infile:
    reader = csv.reader(infile)
    for row in reader:
        try:
            city, state = row[0], row[1]
            key = city + ',' + state
            if key in data:
                continue
            print city, state

            query = city + ' ' + state +' government'
            gws.search(query, 1)
            url = gws.get_result_urls()[0]
            index = 0
            while 'wiki' in url or 'google' in url:
                index += 1;
                url = gws.get_result_urls()[index]

            if url == '' or url is None:
                print 'failed'
                time = random.random()*5;
                sleep(time)
                continue
            temp = {}
            temp['url'] = url
            temp['city'] = city
            temp['state'] = state
            data[key] = temp
            print 'result', url
            time = (random.random()+.5)*1.7;
            sleep(time)
            #saveDataChance(data)
            saveData(data)
        except:
            continue


