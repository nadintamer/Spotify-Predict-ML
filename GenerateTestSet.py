#Author: Nadin Tamer (Hisar School)
import sys
import spotipy
import spotipy.util as util
import re
import pandas as pd

sp = spotipy.Spotify()
scope = 'user-library-read'
username = 'nadintamer'

token = util.prompt_for_user_token(username,scope,client_id='CLIENT-ID',client_secret='CLIENT-SECRET',redirect_uri='REDIRECT-URI')

df = pd.DataFrame(columns=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature'])

uris = ['LIST-OF-SONG-URIS']

if token:
    sp= spotipy.Spotify(auth=token)
    for uri in uris:
        response = str(sp.audio_features(uri)[0])
        response = response[1:-1]
        response = response.split(",")
        response.pop(11)
        response.pop(11)
        response.pop(11)
        response.pop(11)
        response.pop(11)
        features = []
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
        df.loc[df.shape[0]] =  [features[0],features[1],features[2],features[3],features[4],features[5],features[6],features[7],features[8],features[9],features[10],features[11],features[12]]
       
else:
    print("Can't get token for", username)

df.to_csv('testdf.csv',index=False)
print('Success!')



    
