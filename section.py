import random
#from createScale import stayInKey
from chord import Chord

class Section(object):
		
	def __init__(self, key, timesig, measures, startOnRoot):
		self._chordDurations = [.25, .5, .75, 1, 1, 2, 2, 3, 4, 4, 4, 6, 8] # by measure
		
		self.key = key
		self.timesig = timesig
		self.measures = measures
		self.startOnRoot = startOnRoot
		self.keyRoot = self.key[3*7]
		self.range = []
		
		self.chordDurMap = []
		self.rootsMap = []
		self.chords = []
		
		self.__buildSection()


	def __buildSection(self):
		self.__addChordDurs()	
		self.__buildRange()
		self.__addRoots()
		self.__buildChords()

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
			self.range.append(self.key[i])

	def __buildChords(self):
		for i in range(0, len(self.rootsMap)):
			self.chords.append(Chord(self.key, self.rootsMap[i], random.randrange(2, 5)))
	
	def getSection(self):
		return self.chords, self.chordDurMap

	def getSectionDur(self):
		count = 0
		for i in range(0, len(self.chordDurMap)):
			count += self.chordDurMap[i]
		return count

	
# test
'''
intro = Section(stayInKey(1), 4, 4, True)
chords = intro.getSection()[0]
chordDur = intro.getSection()[1]
print intro.getSectionDur()
print chordDur

for i in range(0, len(chords)):
	print chords[i].getVoices()
'''


