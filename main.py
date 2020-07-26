import tweepy
from src.keys import api
from geniusAPI import lyrics_cleaning, lyrics_conversion, genius_song, converttostr
import time
import csv
import random
import json

def main():
    while True:
        with open('src/artists.csv') as f:
            csv_reader = csv.reader(f)
            artist_row = random.choice(list(csv_reader))
            
        seperator = ' '
        artist_str = converttostr(artist_row, seperator)
        print ("artist:%s \n"%(artist_str))
        
        new_song = genius_song(artist_str)
        print (new_song)
        
        #manipulate json file
        json_file = open('src/lyrics.json', 'r', encoding='utf-8')
        json_data=json.load(json_file)
        song_meta = json_data['full_title']
        lyrics_data = json_data['lyrics']

        converted_lyrics = lyrics_conversion(lyrics_data)
        lyrics_rd = lyrics_cleaning(converted_lyrics)
        lyrics_rd.encode(encoding='UTF-8')
        print (converted_lyrics)
        print (lyrics_rd)
        # send the tweet with lyrics
        api.update_status("%s \n (Song: %s)" %(lyrics_rd, song_meta))
        json_file.close()
        time.sleep(900)

if __name__ == "__main__":
    main()

# tweets from the timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)