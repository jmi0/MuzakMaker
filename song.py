import random
from createScale import stayInKey
from structure import Structure

class Song(object):
        
	def __init__(self, title, tempo, key, timesig, measures, sections, genre, midi):
                self.title = title
                self.tempo = tempo
                self.key = key
		self.timesig = timesig
                self.measures = measures
		self.sections = sections
		self.beats = self.timesig * self.measures
                self.genre = genre
		self.midi = midi
		

        def showSong(self):
                print (self.title, self.tempo, self.key, self.measures, self.mood)

	def __getRandomVol(self):
		return random.randint(20, 120)
	
	def __getRandomDur(self):
		return random.randint(1, 12)
	
	def create(self):
		self.midi.addTempo(0, 0, self.tempo)
		
		struct = Structure(self.key, self.timesig, self.measures)
		
		print '\n\n\n'  
		print struct.getStructure
	
		secs = struct.getSections()
		currentbeat = 1

		for i in range(0, len(secs)):
        		print secs[i]
                	chords = secs[i].getSection()[0]
                	chordDurs = secs[i].getSection()[1]
			#print chords[j].getVoices()
			print chordDurs
			for j in range(0, len(chords)):
                        	print chords[j].getVoices()
                		for k in range(0, len(chords[j].getVoices())):
					#print chords[j].getVoices()[k]
					self.midi.addNote(0, 0, chords[j].getVoices()[k], currentbeat, chordDurs[j], self.__getRandomVol())
				
				# add bass notes
				if float(currentbeat).is_integer():
					self.midi.addNote(0, 0, self.key[self.key.index(random.choice(chords[j].getVoices())) - 7], currentbeat, chordDurs[j], self.__getRandomVol())
				currentbeat += chordDurs[j]

		
		with open(self.title + ".mid", "wb") as output_file:
    			self.midi.writeFile(output_file)






