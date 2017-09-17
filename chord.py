import random
#from createScale import stayInKey

class Chord(object):
	
	def __init__(self, key, root, notes):
		self.triad = [2, 4]
		self.intervals = [3, 5, 6]
		self.key = key
		self.root = root
		self.notes = notes # 1 through 4
		self.voices = []
		self.__setVoices()	

	def __setVoices(self):
		self.voices.append(self.root)
		for i in range(0, self.notes - 1):
			if i < 2:
				self.voices.append(self.root + self.triad[i])
			else:
				interval = random.choice(self.intervals)
				self.voices.append(self.root + interval)
				self.intervals.remove(interval)
				
	
	def getVoices(self):
		return self.voices


# test
#chord = Chord(stayInKey(0), 0, 4)
#print chord.getVoices()


