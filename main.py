import sys
import random
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


def main():
  
  midi = MIDIFile(1, adjust_origin=True)
  scale = stayInKey(0)

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


try:
  from midiutil.MidiFile import MIDIFile
except ImportError:
  print('\nMissing requirements.')
  print('run:\n\tpip install -r requirements.txt\n')
  sys.exit(0)


if __name__ == "__main__":
  main()
