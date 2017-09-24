import random

class ChordBlock(object):

        def __init__(self, chord, style, timesig):
                if timesig == 4:
			self.beats = [0, 1, 2, 3]
		elif timesig == 3:
			self.beats = [0, 1, 2]
		self.time = [0,1,2,3]
		self.timesig = timesig
		self.chord = chord
                self.style = style
                self.block = []
		self.time = []
                self.__buildBlock()

        def getBlock(self):
                #TODO
                pass

        def __buildBlock(self):
                for i in range(0, len(chord) - 1):
			self.time.append(random.choice())

