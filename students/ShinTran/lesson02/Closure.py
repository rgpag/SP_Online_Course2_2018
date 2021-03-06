'''
Shin Tran
Python 220
Lesson 2 Assignment
'''

#!/usr/bin/env python3

# Write a closure to capture high energy tracks
# we will define high energy tracks as anything over 0.8

import pandas as pd

music = pd.read_csv("featuresdf.csv")

def get_energy(table):
    return table[2]

def filter_list(energy = 0.8):
    music_list = zip(music.artists, music.name, music.energy)
    tracks = [y for y in music_list if y[2] >= energy]
    track_list = sorted(tracks, key = get_energy, reverse = True)
    def print_list():
        print("Artist               Song Name                                        Energy ")
        print("-----------------------------------------------------------------------------")
        for item in track_list:
            print('{:20} {:45} {:10,.5f}'.format(*item))
    return print_list


high_energy = filter_list(0.8)
high_energy()