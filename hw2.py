import requests
import re
import matplotlib.pyplot as plt
from apikey import *


def lyrics_word_count_easy(artist, song, phrase):
    url = "https://api.lyrics.ovh/v1/" + artist + "/" + song
    r = requests.get(url)
    if (r.status_code != requests.codes.ok):
        return -1
    json = r.json()
    words = json["lyrics"].split()
    word_count = 0
    for word in words:
        if word.lower() == phrase.lower():
            word_count += 1
    return word_count
    

def lyrics_word_count(artist, phrase):
    api_key = apikey['api_key']

    songs = []
    parameters = {'q_artist': artist, 'apikey': api_key}
    find_songs = requests.get("http://api.musixmatch.com/ws/1.1/track.search", params=parameters)
    json = find_songs.json()
    #print(json["message"]["body"]["track_list"])
    for i in range(len(json["message"]["body"]["track_list"])):
        #print(json["message"]["body"]["track_list"][i]["track"]["track_name"])
        songs.append(json["message"]["body"]["track_list"][i]["track"]["track_name"])
    #print(find_songs.url)
    #print(find_songs)
    count = 0
    print(songs)
    for song in songs:
        count += lyrics_word_count_easy(artist, song, phrase)
    return count
    

def visualize():
    import numpy as np
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    
    plt.subplot(2, 1, 1)
    plt.plot(x,y)
    plt.yticks([-20, 0, +20])
    plt.title("LineGraph")
    
    plt.subplot(2, 2, 3)
    plt.hist((x,y), histtype='bar')
    plt.title("Histogram")
    
    plt.subplot(2, 2, 4)
    plt.scatter(x,y)
    plt.title("Scatter")
    return plt.show()

#print(lyrics_word_count_easy("Rick Astley", "Never Gonna Give You Up", "never"))
print(lyrics_word_count("Rick Astley", "never"))
#visualize()
