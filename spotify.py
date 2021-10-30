import requests
from requests.structures import CaseInsensitiveDict

from lib import auth # set enviroment variables in ./lib/secrets.py

token = auth.getToken()

limit = 10
offset = 100

url = f"https://api.spotify.com/v1/artists/2oBG74gAocPMFv6Ij9ykdo/albums?limit={limit}&offset={offset}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer " + token

resp = requests.get(url, headers=headers)
print(resp.text)

# PSEUDO FOR AUTOMATION OF GENERATING TRACKLIST

#def artist():
#    offset = fetchFromDatabase()
#    if(artist not in database):
#        offset = 0
#    response = sendRequest(offset)
#    if(len(response.items) == 0):
#        moveToNextArtist()
#    updateOffset(newoffset = oldoffset+len(response.items))
#    for track in items:
#        parseTrackData()
#        addDatatoArtistCSV()

