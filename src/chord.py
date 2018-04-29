from note import Note

class Chord(Note):
  
  triad = [2, 4]
  intervals = [3, 5, 6]

  def __init__(self, beats, random, root, scale, start):
    Note.__init__(self, beats, random)
    self.root = root
    self.scale = scale
    self.start = start
    self.voices = []
    self.__setPoly()
    self.__setVoices()    

  def __getRandomHarmony(self):
    return self.random.choice(Chord.intervals)

  def __setPoly(self):
    self.poly = self.random.randint(1, 4)

  def __setVoices(self):
    
    for i in range(0, self.poly): 
      
      note = Note(self.beats, self.random)
      index = self.scale.index(self.root) 
      
      if i < 2:
        note.setRoot(self.scale[index + Chord.triad[i]])
      else:
        note.setRoot(self.scale[index + self.__getRandomHarmony()])
      
      self.voices.append(note)

      
