import random
from midiutil.MidiFile import MIDIFile
from src.song import Song
from src.createScale import stayInKey

##################################################
# 16 beats = 1 quarter note
# timesig = */4
##################################################
# Song: 
#   tempo, key, time signature(beats only), 
#   numbner of unique sections, number of measures, 
#   midi handler
##################################################

midi = MIDIFile(1, adjust_origin=True)
scale = stayInKey(3)

songDict = {
  'tempo': 100, 
  'key': scale, 
  'time_signature': 4, 
  'sections': 4,
  'measures': 60,
  'mh': midi,
  'random': random
}

song = Song(songDict)
song.test()
