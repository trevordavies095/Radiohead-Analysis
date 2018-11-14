import json
import operator

with open("emotion-data.json") as f:
	data = json.load(f)

d = {}

for song in data:
	sadness = data[song]["sadness"]
	joy = data[song]["joy"]
	d[song] = joy / sadness

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=False)

for i in sorted_d:
	print(i)