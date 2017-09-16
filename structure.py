import random

class Structure(object):
	
	def __init__(self, timesig, measures):
		self.sectionDurs = [1, 2, 2, 3, 4, 4, 4, 6, 8, 8, 9, 10, 12, 16]
		
		self.timesig = timesig
		self.measures = measures
		self.beats = self.measures * self.timesig
		self.uniqueMeasures = self.measures / 2
		self.structure = []
		
		self.__buildStructure()

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

	def getStructure(self):
		return self.measures, self.uniqueMeasures, self.structure

# test
#struct = Structure(4, 60)
#print struct.getStructure()
