import time
import random
import lyricsgenius as lg
import csv
import random
import json
import os
GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")

genius = lg.Genius(GENIUS_TOKEN, skip_non_songs=True, remove_section_headers=True)

# random pick an artist from the csv
with open('artists.csv') as f:
    csv_reader = csv.reader(f)
    artist_row = random.choice(list(csv_reader))

# convert list to string
def converttostr(input_seq, seperator):
    final_str = seperator.join(input_seq)
    return final_str

seperator = ' '
artist_str = converttostr(artist_row, seperator)
print (artist_str)

# select the song and save the lyrics to a json file 
def genius_song(artist_str):  
    artist = genius.search_artist(artist_str, max_songs=25, sort="title")
    select_song = random.choice(artist.songs)
    lyrics = select_song.save_lyrics('lyrics.json', overwrite=True, extension='json')
    return print (select_song)

new_song = genius_song(artist_str)
print (new_song)

json_file = open('lyrics.json', 'r', encoding='utf-8')
json_data=json.load(json_file)
# metadata 
song_meta = json_data['full_title']
lyrics_data = json_data['lyrics']

def lyrics_conversion(lyrics_json):
    lyric_extraction = []
    lyrics_split = lyrics_json.splitlines()
    lyric_converted = lyric_extraction.extend(lyrics_split)
    return lyric_extraction

def lyrics_cleaning(converted_lyrics):
    list_tags = [(5,7),(10,12),(3,5),(6,8),(16,18),(2,4),(3,5),(7,9),(4,6),(6,10)]
    random_parts = random.choice(list_tags)
    print (random_parts)
    cleaned_lyrics = (converted_lyrics[random_parts[0]:random_parts[1]])
    cleaned_lyrics = (str(cleaned_lyrics).strip('['']'))
    return cleaned_lyrics

converted_lyrics = lyrics_conversion(lyrics_data)
lyrics_rd = lyrics_cleaning(converted_lyrics)
print (converted_lyrics)
print (lyrics_rd)

json_file.close()
