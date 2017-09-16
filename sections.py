
class Section(object):
	secLens = [4, 8, 12, 16]
			
	def __init__(self, key, timesig, measures):
		self.key = key
		self.timesig = timesig
		self.measures = measures
		self.keyRoot = self.key[0] + (3*7)
	
	
	def __buildSection(self):
		# TODO
		pass	
		
		
