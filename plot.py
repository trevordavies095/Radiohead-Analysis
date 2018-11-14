import json
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

with open("emotion-data.json") as f:
	data = json.load(f)

songs = []
joy = []
sadness = []

for song in data:
	songs.append(song)
	sadness.append(data[song]["sadness"] * 100)
	joy.append(data[song]["joy"] * 100)


for i in range(len(songs)):
	print(songs[i] + ": (" + str(joy[i]) + ", " + str(sadness[i]) + ")")

plt.xlabel("Joy")
plt.ylabel("Sadness")
plt.scatter(joy, sadness)

mplcursors.cursor(hover=True)

plt.show()

