import random
from structure import Structure

class Song(object):
        
	def __init__(self, title, tempo, key, timesig, measures, sections, mood, midi):
                self.title = title
                self.tempo = tempo
                self.key = key
		self.timesig = timesig
                self.measures = measures
		self.sections = sections
		self.beats = self.timesig * self.measures
                self.mood = mood
		self.midi = midi
		
		self.low = None
		self.mid = None
		self.high = None		
		self.__setRanges()

        def showSong(self):
                print (self.title, self.tempo, self.key, self.measures, self.mood)

	def __addTrack(self):
		# TODO
		pass

	def __getRandomNote(self, array):
		return random.choice(array)
		
	def __getRandomTime(self):
		return random.randint(1, self.beats)
	
	def __getRandomBeat(self):
		return random.randint(1, 4)
	
	def __getRandomVol(self):
		return random.randint(20, 120)
	
	def __getRandomDur(self):
		return random.randint(1, 12)

	def __setRanges(self):
		full_length = len(self.key)
	 	l = []
		m = []
		h = []
		thirds = full_length / 3
	
		for i in range(7, thirds):
			l.append(self.key[i])
		for i in range(i, thirds*2):
			m.append(self.key[i])
		for i in range(i, full_length - 7):
			h.append(self.key[i])
		
		self.low = l
		self.mid = m
		self.high = h
		
	def __lowTrack(self, midi):
		# temporary algo, will be handled differently
		progression = []
		note = self.low[7]
		for i in range(0, (self.beats / (self.timesig))):
			if (i % self.timesig == 0):
				note = self.__getRandomNote(self.low)
			
    			midi.addNote(0, 0, note, i*(self.timesig), 4, self.__getRandomVol())
		
	
	def __midTrack(self, midi):
		# temporary algo, will be handled differently
		for i in range(0, self.beats * 2):
    			midi.addNote(0, 1, self.__getRandomNote(self.mid), .5*i, self.__getRandomDur(), self.__getRandomVol())
		
	
	def __highTrack(self, midi):
		# temporary algo, will be handled differently
		for i in range(0, self.beats * 2):
			time = self.__getRandomTime()
			if i % self.__getRandomDur() - 2 == 0:
				time = time + .25	
			if i % self.__getRandomDur() - 1 == 0:
				time = time + .5

		
    			midi.addNote(0, 2, self.__getRandomNote(self.high), time, self.__getRandomDur(), self.__getRandomVol())
			
		
	
	def create(self):
		self.__setRanges()
		self.midi.addTempo(3, 0, self.tempo)
		
		self.__lowTrack(self.midi)
		self.__midTrack(self.midi)
		self.__highTrack(self.midi)		
		

		with open(self.title + ".mid", "wb") as output_file:
    			self.midi.writeFile(output_file)
