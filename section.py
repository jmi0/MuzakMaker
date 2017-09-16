import random
#from createScale import stayInKey
from Chord import chord

class Section(object):
		
	def __init__(self, key, timesig, measures, startOnRoot):
		self._chordDurations = [.25, .5, .75, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 6, 8, 8] # by measure
		#####################################
		
		self.key = key
		self.timesig = timesig
		self.measures = measures
		self.startOnRoot = startOnRoot
		self.keyRoot = self.key[0] + (5*7)
		self.range = []
		
		self.chordDurMap = []
		self.rootsMap = []
		
		self.__buildSection()


	def __buildSection(self):
		self.__addChordDurs()	
		self.__buildRange()
		self.__addRoots()
		
	def __addChordDurs(self):
		full = 0
		dur = self.measures + 1 # to invoke while 
		
		# add a random chord duration to chordDurMap until full
		while full < self.measures:
			dur = random.choice(self._chordDurations)
			if dur > (self.measures - full):
				while dur > (self.measures - full):
					dur = random.choice(self._chordDurations)
			full += dur
			self.chordDurMap.append(dur)

	def __addRoots(self):
		if self.startOnRoot is True:
			self.rootsMap.insert(0, self.keyRoot)
			start = 1
		else:
			start = 0
		for i in range(start, len(self.chordDurMap)):
			self.rootsMap.append(random.choice(self.range))

	
	def __buildRange(self):
		for i in range(self.keyRoot - 6, self.keyRoot + 6):	
			self.range.append(i)


	def getSection(self):
		return self.keyRoot, self.measures, self.chordDurMap, self.rootsMap


# test
#intro = Section(stayInKey(1), 4, 4, True)
#print intro.getSection()



