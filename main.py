from midiutil.MidiFile import MIDIFile
from src.song import Song
from src.createScale import stayInKey

midi = MIDIFile(1, adjust_origin=True)

# Song object; Song(title, tempo, key(0-12), time signature(beats only), # of measures, vocabulary (for future), midi object)

song = Song("shmuzak", 60, stayInKey(3), 4, 100, 4, "test", midi)

# create method is one and only public method for Song class

song.create()



