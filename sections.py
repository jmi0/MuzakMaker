import random
from createScale import stayInKey

class Section(object):
		
	def __init__(self, key, timesig, measures):
		# will eventually be input parameters for decision making v
		self._sectionDurations = [4, 8, 12, 16] # by measure
		self._chordDurations = [1, 2, 2, 3, 4, 4, 4, 6, 8] # by measure
		##############################################################
		
		self.key = key
		self.timesig = timesig
		self.measures = measures
		self.keyRoot = self.key[0] + (3*7)
		self.range = []
		
		self.sectionDuration = random.choice(self._sectionDurations)
		self.chordDurMap = []
		self.rootsMap = []
		
		self.__buildSection()


	def __buildSection(self):
		self.__addChordDurs()	
		self.__buildRange()
		self.__addRoots()
		
	
	def __addChordDurs(self):
		full = 0
		dur = self.sectionDuration + 1 # just to start while 
		
		# add a random chord duration to chordDurMap until full
		while full < self.sectionDuration:
			while dur > (self.sectionDuration - full):
				dur = random.choice(self._chordDurations)
			
			full = full + dur
			self.chordDurMap.append(dur)
	
	def __addRoots(self):
		for i in range(0, len(self.chordDurMap)):
			self.rootsMap.append(random.choice(self.range))

	
	def __buildRange(self):
		for i in range(self.keyRoot - 7, self.keyRoot + 7):	
			self.range.append(i)


	def getSection(self):
		return self.sectionDuration, self.chordDurMap, self.rootsMap


# test
#intro = Section(stayInKey(1), 4, 60)
#print intro.getSection()



