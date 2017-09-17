
class Chord(object):
	
	def __init__(self, key, root, notes):
		self.key = key
		self.root = root
		self.notes = notes # 1 through 4
		self.voices = []
		self.__setVoices()	

	def __setVoices(self):
		self.voices.insert(0, self.root)
		for i in range(0, self.notes - 1):
			if i == 0:
				self.voices.append(self.getThird())
			elif i == 1:
				self.voices.append(self.getFifth())	

	def getVoices(self):
		return self.voices

	def getThird(self):
		return self.root + 2	

	def getFourth(self):
		return self.root + 3

	def getFifth(self):
		return self.root + 4
	
	def getSixth(self):
		return self.root + 5

	def getSeventh(self):
		return self.root + 6

	def getOct(self):
		pass	
