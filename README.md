# SpotifyPredictML

## Overview
In this project, I used the Spotify Web API to extract the audio features of the songs I listened to most in 2017 (and did the same for a friend). I then used machine learning to try and get a computer to predict whether a song is from my playlist or his! 

## Tools Used
* Python
* Spotify Web API
* Spotipy
* Scikit-learn
* Seaborn and matplotlib

## What's in this Repository?
* `GenerateDataset.py` : Used to generate training set
* `GenerateTestSet.py` : Used to generate test set
* `SpotifyPredictML.py` : Jupyter notebook containing data visualization and machine learning
* `MeanAudioFeatures.png` : Graph of mean audio features by owner
* `DistributionPlot1.png` : Distribution plot of danceability, energy, mode, and speechiness
* `DistributionPlot2.png` : Distribution plot of acousticness, instrumentalness, liveness, and valence
* `CorrelationHeatmap.png` : Correlation heatmap of audio features
