import lyricsgenius as genius
api = genius.Genius("0fcFpSvk1P4PeWrOztzBz_X38K9YMqivXQ-Ta-QBejzjfZQYDExpL_b4VtHxpJ6Z")

artist = api.search_artist('Radiohead', max_songs=0)

with open("songs.txt", "r") as file:
	for line in file:
		if line.strip() != "":
			artist.add_song(api.search_song(line.strip(), artist.name))

artist.save_lyrics()