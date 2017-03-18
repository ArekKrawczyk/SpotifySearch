from flask import Flask, render_template
import datetime
import spotipy
sp = spotipy.Spotify()
import requests
from flask import request

app = Flask(__name__)



import requests
req = 'https://api.spotify.com/v1/search?query=%s&type=%s&limit=20' % ("Foxes", "album")
print req
response = requests.get(req)
for i in response.json()["albums"]["items"]:
    print i["name"]
    print i["images"][-1]
