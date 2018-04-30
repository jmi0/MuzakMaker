from src.chord import Chord

class Measure():
  
  def __init__(self, scale, beats, random):
    self.scale = scale
    self.beats = beats*2
    self.random = random
    self.currentBeat = 0
    self.chords = []
    self.__setRange()
    self.__setChordLens()
    self.__setChords()

  def __setRange(self):
    # grab a single octave for root notes
    start = (len(self.scale)/4)*2
    self.range = self.scale[start:start+7]

  def __beatsRemaining(self):
    return self.beats - self.currentBeat

  def __getRandomChordLen(self):
    return self.random.choice(self.chordLens)
  
  def __getRandomRoot(self):
    return self.random.choice(self.range)

  def __setChordLens(self):
    self.chordLens = []
    for i in range(1, self.beats):
      self.chordLens.append(self.beats/i)

  def __setChords(self):
    while (self.__beatsRemaining() > 0):
      chordLen = self.__getRandomChordLen()
      root = self.__getRandomRoot()
      chord = Chord(chordLen, self.random, root, self.scale, self.currentBeat)
      self.chords.append(chord)
          
      self.currentBeat += chordLen
