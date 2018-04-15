import random
from section import Section
#from createScale import stayInKey

class Structure(object):
	
	def __init__(self, key, timesig, measures):
		self.sectionDurs = [1, 2, 2, 3, 4, 4, 4, 6, 8, 8, 9, 10, 12, 16]
		self.rootFirst = [True, False]		

		self.structure = []
		self.sections = []

		self.key = key
		self.timesig = timesig
		self.measures = measures
		self.beats = self.measures * self.timesig
		self.uniqueMeasures = self.measures
		
		self.__buildStructure()
		self.__addSections()

	def __buildStructure(self):
		full = 0
		dur = self.uniqueMeasures + 1		

		while full < self.uniqueMeasures:
			dur = random.choice(self.sectionDurs)
			if dur > (self.uniqueMeasures - full):
				while dur > (self.uniqueMeasures - full):
					dur = random.choice(self.sectionDurs)
			full += dur
			self.structure.append(dur)
	
	def __addSections(self):
		full = 0
		for i in range(0, len(self.structure)):
			if i == 0:
				root = True
			else:
				root = random.choice(self.rootFirst)
			
			sec = Section(self.key, self.timesig, self.structure[i], root)
			length = sec.getSectionDur()
			
			repeat = 0
			ch = [2, 4]
			if length > 4 and length <= 8 and full < self.beats:
				repeat = random.choice(ch)
			else:
				repeat = 0
			for j in range(0, repeat):
				self.sections.append(sec)		
			
			if repeat > 0:
				full += length*repeat
			else:
				full += length

	def getStructure(self):
		return self.measures, self.uniqueMeasures, self.structure
	
	def getSections(self):
		#print self.sections
		return self.sections
	
	def getLength(self):
		length = 0
		for i in range(0, len(self.sections)):
			length += self.sections[i].getSectionDur()
		return length	

# test
#struct = Structure(stayInKey(0), 4, 60)
#print struct.getStructure()
