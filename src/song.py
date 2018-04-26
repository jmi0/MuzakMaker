import random
import datetime
import time
from createScale import stayInKey
from structure import Structure
from chordBlock import ChordBlock

class Song(object):
        
	def __init__(self, songDict):
		self.title = songDict['title']
		self.tempo = songDict['tempo']
		self.key = songDict['key']
		self.timesig = songDict['time_signature']
		self.measures = songDict['measures']
		self.sections = songDict['sections']
		self.beats = (self.measures * self.timesig) / self.timesig
		self.genre = songDict['genre']
		self.midi = songDict['mh']

	def showSong(self):
		print (self.title, self.tempo, self.key, self.measures, self.mood)

	def __getRandomVol(self):
		return random.randint(20, 120)

	def __getRandomDur(self):
		return random.randint(1, 12)

	def __createAndSave(self):
		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
		with open(self.title + "_" + dt + ".mid", "wb") as output_file:
			self.midi.writeFile(output_file)

	def test(self):
		self.midi.addTempo(0, 0, self.tempo)
		struct = Structure(self.key, self.timesig, self.measures)
		print '\n' 
		print self.title + '...\n' 
		#print struct.getStructure
		secs = struct.getSections()
		currentbeat = 1
		for i in range(0, len(secs)):
			print secs[i]
			chords = secs[i].getSection()[0]
			chordDurs = secs[i].getSection()[1]
			#print chords[j].getVoices()
			print 'chord durations:  '
			print chordDurs
			for j in range(0, len(chords)):
				print 'chord voices:'
				print chords[j].getVoices()
					
				for k in range(0, len(chords[j].getVoices())):
					if struct.getLength() - currentbeat <= 1:
						dur = self.timesig*2
					else:
						dur = chordDurs[j]
						note = chords[j].getVoices()[k]
						vol = self.__getRandomVol()
						self.midi.addNote(0, 0, note, currentbeat, dur, vol)
				
					# add bass notes on whole notes
					if float(currentbeat).is_integer():
						note = self.key[self.key.index(random.choice(chords[j].getVoices())) - 7]
						vol = self.__getRandomVol()
						self.midi.addNote(0, 0, note, currentbeat, chordDurs[j], vol)
				
				currentbeat += chordDurs[j]
			
		print '\n'
			
		self.__createAndSave()
