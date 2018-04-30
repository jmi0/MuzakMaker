import random
import datetime
import time
from src.measure import Measure

class Song():
        
  def __init__(self, songDict):

    self.timesig = songDict['time_signature']
    self.measures = songDict['measures']
    self.sections = songDict['sections']
    self.beats = self.measures * self.timesig
    self.tempo = songDict['tempo']
    self.key = songDict['key']
    self.midi = songDict['mh']
    self.random = songDict['random']
    self.currentBeat = 0

    if self.beats % self.sections != 0:
      raise Exception("section number must be a factor of measures")

    self.sectionSize = self.beats / self.sections


  def __getRandom(self, mn, mx):
    return random.randint(mn, mx)


  def __beatsRemaining(self): 
    return self.beats - self.currentBeat


  def __write(self):
    ts = time.time()
    dt = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    with open("song_" + dt + ".mid", "wb") as output_file:
      self.midi.writeFile(output_file)


  def test(self):
    self.midi.addTempo(0, 0, self.tempo)
    
    while self.__beatsRemaining() > 0:
      # new measure
      measure = Measure(self.key, self.timesig, self.random)
      for i in range(0, len(measure.chords)):
        chord = measure.chords[i]
          
        for j in range(0, len(chord.voices)):
          voice = chord.voices[j]
          midiPos = self.currentBeat
          duration = chord.beats+1 # add a trailing sustain
          dynamics = self.__getRandom(20, 120)
          print('currentBeat: ' + str(self.currentBeat))
          print('dur: ' + str(duration-1))
          print('note: ' + str(voice.root))
          self.midi.addNote(0, 0, voice.root, midiPos, duration, dynamics)
        self.currentBeat += chord.beats

    self.__write()
