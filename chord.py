
class Chord(object):
	
	def __init__(key, root):
		self.key = key
		self.root = root
		self.voice1 = None
		self.voice2 = None
		self.voice3 = None
		self.voice4 = None
		self.__setVoices()	

	def __setVoices(self):
		pass
