#Author: Nadin Tamer (Hisar School)
import sys
import spotipy
import spotipy.util as util
import re
import pandas as pd

sp = spotipy.Spotify()
scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
   print("Usage: %s username" % (sys.argv[0],))
   sys.exit()

token = util.prompt_for_user_token(username,scope,client_id='CLIENT-ID',client_secret='CLIENT-SECRET',redirect_uri='REDIRECT-URI')

df = pd.DataFrame(columns=['id', 'name', 'artists', 'danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature'])

def music(uri, name, artists):
    global df
    global top2017
    response = str(sp.audio_features(uri)[0])
    response = response[1:-1]
    response = response.split(",")
    response.pop(11)
    response.pop(11)
    response.pop(11)
    response.pop(11)
    response.pop(11)
    features = [uri, name, artists]
    for x in response:
        m = re.search("\d",x)
        if m:
            if "," in x:
                x = x[:-1]
            if x[m.start()-1] == "-":
                feature = x[m.start()-1:]
            else:
                feature = x[m.start():]
            try:
                feature = float(feature)
            except ValueError:
                feature = feature
            features.append(feature)
    df.loc[df.shape[0]] =  [features[0][:-1],features[1],features[2],features[3],features[4],features[5],features[6],features[7],features[8],features[9],features[10],features[11],features[12],features[13],features[14],features[15]]

def track_info(tracks):
    idlist = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        idlist.append([track['id'],track['name'],track['artists'][0]['name']])
        #print(" %d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))
    return idlist

uri = 'PLAYLIST-LINK'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

if token:
    sp= spotipy.Spotify(auth=token)
    results = sp.user_playlist(username,playlist_id,fields='tracks,next')
    tracks = results['tracks']
    playlist = track_info(tracks)
    
    for x in playlist:
        music(x[0],x[1],x[2])
    
else:
    print("Can't get token for", username)

df.to_csv('nadindf.csv',index=False)

#######################

nadindf = pd.read_csv("nadindf.csv")
candf = pd.read_csv("candf.csv")

df = pd.DataFrame(columns=['owner','id', 'name', 'artists', 'danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature'])

for index, row in nadindf.iterrows():
    df.loc[df.shape[0]] =  ['Nadin',row['id'],row['name'],row['artists'],row['danceability'],row['energy'],row['key'],row['loudness'],row['mode'],row['speechiness'],row['acousticness'],row['instrumentalness'],row['liveness'],row['valence'],row['tempo'],row['duration_ms'],row['time_signature']]

for index, row in candf.iterrows():
    df.loc[df.shape[0]] =  ['Can',row['id'],row['name'],row['artists'],row['danceability'],row['energy'],row['key'],row['loudness'],row['mode'],row['speechiness'],row['acousticness'],row['instrumentalness'],row['liveness'],row['valence'],row['tempo'],row['duration_ms'],row['time_signature']]

df.to_csv("nadincandf.csv",index=False)
print("Success!")
