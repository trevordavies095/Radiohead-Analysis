import indicoio
import json
import re
from pprint import pprint

indicoio.config.api_key = ''

emotion_data = {}

with open("Lyrics_Radiohead.json") as f:
	data = json.load(f)

for song in data['songs']:
	title = song['title']
	song = song['lyrics']
	song = song.replace("[", "<")
	song = song.replace("]", ">")
	song = re.sub('<[^>]+>', '', song)
	song = song.replace("\n\n\n", "/ ")
	song = song.replace("\n", "/ ")

	emotion_data[title] = indicoio.emotion(song)

	print(title + ": " + str(emotion_data[title]['sadness']))

with open("emotion-data.json", 'w') as f:
	json.dump(emotion_data, f)