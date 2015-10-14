#!/usr/local/bin/python3

import sys
import urllib.request
import json


mapsURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(sys.argv[1])
mapsResult = urllib.request.urlopen(mapsURL).read()
mapsJSON = json.loads(mapsResult.decode('utf-8'))

results = mapsJSON['results']
information = results[0]
geometry = information['geometry']
location = geometry['location']

latitude = location['lat']
longitude = location['lng']

instagramURL = "https://api.instagram.com/v1/media/search?lat="+str(latitude)+"&lng="+str(longitude)+"&client_id=d140e2b778d0406a9f6cc82f4410491b"
instagramResult = urllib.request.urlopen(instagramURL).read()
instagramJSON = json.loads(instagramResult.decode('utf-8'))

if len(instagramJSON.keys()) > 0:
    for image in instagramJSON['data']:
        pass
        '''
        Re add processing.
        '''
