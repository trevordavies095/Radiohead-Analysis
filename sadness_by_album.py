import indicoio
import json
import re
from pprint import pprint

indicoio.config.api_key = ''

emotion_data = {}

with open("Lyrics_Radiohead.json") as f:
	data = json.load(f)

with open("sadness-by-album-data.csv", "w") as f:
	f.write("title,album,sadness\n")
	for song in data['songs']:
		title = song['title']
		print(title)
		album = song['album']
		title = song['title']
		song = song['lyrics']
		song = song.replace("[", "<")
		song = song.replace("]", ">")
		song = re.sub('<[^>]+>', '', song)
		song = song.replace("\n\n\n", "/ ")
		song = song.replace("\n", "/ ")

		f.write(title + "," + album + "," + str(indicoio.emotion(song)["sadness"]) + "\n")