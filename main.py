from midiutil.MidiFile import MIDIFile
from song import Song
from createScale import stayInKey

midi = MIDIFile(1, adjust_origin=True)

# Song object; Song(title, tempo, key(0-12), time signature(beats only), # of measures, vocabulary (for future), midi object)

song = Song("shmuzak", 140, stayInKey(8), 4, 30, 4, "ambient chill", midi)

# start method is one and only public method for Song class

song.create()



