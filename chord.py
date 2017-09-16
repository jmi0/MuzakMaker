
class Chord(object):
	
	def __init__(self, key, root, notes):
		self.key = key
		self.root = root
		self.notes = notes # 1 through 4
		self.voices = []
		self.__setVoices()	

	def __setVoices(self):
		self.voices.insert(0, self.root)
		for i in range(0, self.notes):
			# TODO
			pass

	def getVoices(self):
		return self.voices
