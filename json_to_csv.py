import json

with open("emotion-data.json") as f:
	data = json.load(f)

with open("emotion-data.csv", "w") as f:
	f.write("song,joy,anger,fear,sadness,surprise\n")
	for song in data:
		f.write(song + "," + str(data[song]["joy"]) + "," + str(data[song]["anger"]) + "," + str(data[song]["fear"]) + "," + str(data[song]["sadness"]) + "," + str(data[song]["surprise"]) + "\n")