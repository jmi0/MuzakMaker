from chord import Chord

class Measure():
  
  def __init__(self, scale, beats, random):
    self.scale = scale
    self.beats = beats*4
    self.random = random
    self.currentBeat = 0
    self.chords = []
    self.__setChordLens()
    self.__setChords()
  
  def __beatsRemaining(self):
    return self.beats - self.currentBeat

  def __getRandomChordLen(self):
    return self.random.choice(self.chordLens)
  
  def __getRandomRoot(self):
    return self.random.choice(self.scale[0:12])

  def __setChordLens(self):
    self.chordLens = []
    for i in range(1, self.beats/2):
      self.chordLens.append(self.beats/i)     

  def __setChords(self):
    while (self.__beatsRemaining() > 0):
      chordLen = self.__getRandomChordLen()
      root = self.__getRandomRoot()
      chord = Chord(chordLen, self.random, root, self.scale, self.currentBeat)
      self.chords.append(chord)
          
      self.currentBeat += chordLen
