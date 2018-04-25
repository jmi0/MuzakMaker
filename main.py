from midiutil.MidiFile import MIDIFile
from src.song import Song
from src.createScale import stayInKey

midi = MIDIFile(1, adjust_origin=True)

# Song object; Song(title, tempo, key(0-12), time signature(beats only), # of measures, vocabulary (for future), midi object)

songDict = {
	'title': 'shmuzak', 
	'tempo': 60, 
	'key': stayInKey(1), 
	'time_signature': 4, 
	'measures': 200, 
	'sections': 8, 
	'genre': 'test', 
	'mh': midi
}

song = Song(songDict)

# create method is one and only public method for Song class

song.create()



