import random
from createScale import stayInKey


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
		dur = self.measures + 1 # just to start while 
		
		# add a random chord duration to chordDurMap until full
		while full < self.measures:
			while dur > (self.measures - full):
				if self.measures - full <= 2 and dur > 2: # optimization
					self._chordDurations.remove(dur)
				dur = random.choice(self._chordDurations)
			full += dur
			self.chordDurMap.append(dur)
		
			if (dur < 1) and (float(full).is_integer()): # dont allow too many off-beat changes
				self._chordDurations.remove(dur)
				dur = self.measures - full + 1 # reset dur to invoke while
	
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
#intro = Section(stayInKey(1), 4, 8, True)
#print intro.getSection()



