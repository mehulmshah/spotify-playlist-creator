import requests
import base64
import sys
import json

CLIENT_ID = 'e91542f2d63248269efb73a7099d36bd'
SECRET_KEY = '02e7c7dd501941cf8ebc597ae306f3c3'

def getMood():
    mood = input('Pick a characteristic (danceability, energy, speechiness, valence): ')
    return mood

def getGenre():
    genre = input('Pick a genre (pop, r-n-b, industrial, spanish, etc): ')
    return genre

def getAuth():
    login_url = 'https://accounts.spotify.com/api/token'
    body = {'grant_type':'client_credentials'}
    encoded_auth = base64.b64encode(CLIENT_ID+':'+SECRET_KEY)
    headers = {'Authorization':'Basic %s' % encoded_auth}
    res = requests.post(login_url,data={'grant_type':'client_credentials'},headers=headers)
    if res.status_code != 200:
        print('There was an error getting the auth token')
        sys.exit(1)
    token_info = res.json()
    return token_info

def getSongs(mood, genre, token):
    endpoint = 'https://api.spotify.com/v1/recommendations?seed_genres='+genre+'&target_'+mood+'=1.0&limit=10'
    headers = {'Authorization': 'Bearer %s' % str(token['access_token'])}
    r = requests.get(endpoint, headers=headers)
    if r.status_code != 200:
        print('There was an error getting results')
        sys.exit(1)
    return r.json()

def outputList(results):
    for i in range(len(results['tracks'])):
        print('Artist: ' + results['tracks'][i]['artists'][0]['name'] + ' Title: ' + results['tracks'][i]['name'])
        print('Link: ' + results['tracks'][i]['external_urls']['spotify'] + '\n')

def main():
    token = getAuth()
    mood = getMood()
    genre = getGenre()
    result = getSongs(mood, genre, token)
    print(result)
    outputList(result)

if __name__ == '__main__':
    main()
