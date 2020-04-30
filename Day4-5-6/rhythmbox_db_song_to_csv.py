from xml.etree import ElementTree as ET
from collections import namedtuple, defaultdict
import csv

input = 'rhythmdb.xml'
output ='songs.csv'

tree = ET.parse(input)
root = tree.getroot()

Song = namedtuple('Song', 'artist title tracknumber album')
artists = defaultdict(list)

for entry in root:
    if entry.attrib['type'] == 'song':
        artist = str(entry[2].text)
        title = str(entry[0].text)
        album = str(entry[3].text)
        tracknumber = int(entry[4].text)
        song = Song(artist=artist, title=title, tracknumber=tracknumber ,album=album)
        artists[artist].append(song)
        
with open(output, 'w',newline='') as csv_out:
    csvwriter = csv.writer(csv_out, delimiter=',')
    csvwriter.writerow(['artist', 'album', 'tracknumber','title'])
    for artist, songs in artists.items():
        for song in songs:
            row_out =[song.artist, song.album, song.tracknumber,song.title]
            csvwriter.writerow(row_out)


