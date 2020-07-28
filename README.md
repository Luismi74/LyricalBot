

<h1 align="center">Lyrical-Bot</h1>
<h3 align="center"> 
Twitter Bot that tweets quotes from lyrics
</h3>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg?style=?style=for-the-badge)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/fo-real.svg)](https://forthebadge.com)

## Check it out: [Twitter Link](https://twitter.com/BotLyrical)

Dependencies
------------

  * Twitter API
  * Tweepy==3.9.0
  * Lyricsgenius==1.8.6

        pip install Tweepy
        pip install lyricsgenius

You will need to create an app account on https://dev.twitter.com/apps and modify the settings permissions to read and write then generate new Oauth Tokens. you'll need to also sign up for a (free) account that authorizes access to [the Genius API](http://genius.com/api-clients).

Usage
------------
    . 
    LyricalBot/
    │
    ├── src/
    │   ├── env_settings.py
    │   └── keys.py
    │   └── artists.csv
    │
    ├── lyrics.json
    ├── geniusAPI.py  
    ├── main.py
    └── requirements.txt

###### The Bot uses a list os artist located in the `src/artists.csv` file, if you want to add a new artist you can contribute with a pull request 🖖

The main file for the project is main.py and has some function calls to geniusAPI.py for structuring the lyrics format. To change how many songs you want to query for a specific artist, navigate to `geniusAPI.py` and change the value `max_songs`:

```python
artist = genius.search_artist(artist_str, max_songs=25, sort="title")
```

###### Lyrics are song metadata are stroed in the `lyrics.json` file extracted using the [Lyricgenius API](https://github.com/johnwmillr/lyricsgenius).

If you want to change the amount of time it takes to tweet, go to the main file `main.py` and change the time in seconds:

```python
time.sleep(900)
```

License
------------

You can fork 🍴 this repository on GitHub as long as it links back to this original repository. Have fun! 🤗

Contribute
------------

If you want to contribute to this project or just want to add your favorite artist hit me up or send a pull request ✅