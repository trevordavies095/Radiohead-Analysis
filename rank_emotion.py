import json
import operator

with open("emotion-data.json") as f:
	data = json.load(f)

d = {}

for song in data:
	d[song] = data[song]["sadness"]

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

for i in sorted_d:
	print(i)