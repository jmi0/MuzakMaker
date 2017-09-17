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
		self.uniqueMeasures = self.measures / 2
		
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
		for i in range(0, len(self.structure)):
			if i == 0:
				root = True
			else:
				root = random.choice(self.rootFirst)
			
			self.sections.append(Section(self.key, self.timesig, self.structure[i], root))		

	def getStructure(self):
		return self.measures, self.uniqueMeasures, self.structure
	
	def getSections(self):
		first = self.sections
		last = self.sections
		secs = first + last 
		return secs

# test
#struct = Structure(stayInKey(0), 4, 60)
#print struct.getStructure()
