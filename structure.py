from chord import Chord

class Structure(object):
	
	def __init__(self, timesig, measures, beats, key, sections, feeling):
		self.timesig = timesig
		self.measures = measures
		self.beats = beats
		self.key = key
		self.sections = sections
		self.feeling = feeling # vocabulary
		self.sectionStyle = ['block', 'arpeggiate', 'glissando']
	
	def __setRoots(self):
		# TODO
		pass
	
	def __setRootDuration(self):
		# TODO
		pass

	def __createSection(self):
		# TODO
		pass
	
	def build(self):
		# TODO
		pass
