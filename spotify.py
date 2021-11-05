import json
import time
import requests
from requests.structures import CaseInsensitiveDict

from lib import auth # set enviroment variables in ./lib/secrets.py
from lib import db
from lib import fileHandler

token = auth.getToken()

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer " + token

def parseAlbum(albums):
    # if album['album_group'] == 'appears_on' then it is a feature album
    for album in albums:
        print(album['album_type'],album['name'])

# takes input from csv file (artist,spotify_id)
def artist(artistData):
    print(artistData)
    metadata =  db.fetchMetaData(artistData['name'])
    offset = 0
    print(type(metadata))
    if (metadata is None) or (len(metadata) == 0):
        db.insertArtist(artistData)
    else:
        offset = offset = int(metadata['count'])
    spotify_id = artistData['spotify_id']
    limit = 7
    url = f"https://api.spotify.com/v1/artists/{spotify_id}/albums?limit={limit}&offset={offset}"
    resp = json.loads(requests.get(url, headers=headers).text)
    print(resp['total'])
    #fileHandler.writeFile(resp.text, 'data.json')
    # update artist data at the end of loop
    while (offset != resp['total']): # if no new tracks added then skip
        print('offset',offset)
        # process items
        parseAlbum(resp['items'])
        offset += len(resp['items'])
        url = resp['next']
        if url is None:
            print('offset',offset)
            return
        resp = json.loads(requests.get(url,headers=headers).text)
        time.sleep(3)

if __name__ == '__main__':
    artist({
        'name' : 'seedhe maut',
        'spotify_id' : '2oBG74gAocPMFv6Ij9ykdo'
    })
