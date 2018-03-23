import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getMoods():
    mood = input('Pick one or more characteristics separated by spaces (danceability, energy, speechiness, valence): ')
    mood_list = mood.split(' ')
    return ['target_' + mood for mood in mood_list]

def getGenres():
    genre = input('Pick one or more genres separated by spaces (pop, r-n-b, industrial, spanish, etc): ')
    genre_list = genre.split(' ')
    return genre_list

def outputList(results):
    for i in range(len(results['tracks'])):
        print('Artist: ' + results['tracks'][i]['artists'][0]['name'] + ' Title: ' + results['tracks'][i]['name'])
        print('Link: ' + results['tracks'][i]['external_urls']['spotify'] + '\n')

def main():
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    moods = getMoods()
    genres = getGenres()
    result = sp.recommendations(seed_genres=genres, limit=5,)
    outputList(result)

if __name__ == '__main__':
    main()
