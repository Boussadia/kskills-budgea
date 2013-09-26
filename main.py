# -*- coding: utf-8 -*-

class Converter:
	"""
		This class is responsible for converting strings into structured data.

		Exemple :
			Input : ["loyer;-485.00 restaurant;-32.50 retrait;-40.00 salaire;2300.00"]
			Output : [{'loyer': -485.00, 'restaurant': -32.50, "retrait": -40.00, "salaire": 2300.00}] 
	"""

	def __init__(self, lines = []):
		"""
			lines = list of strings.
		"""
		self.lines = lines
		self.structured_data = []
	
	def convert(self):
		"""
			Conversion occurs here.
		"""
		self.structured_data = [self.convert_line(line) for line in self.lines]

	def convert_line(self, line):
		"""
			Line conversion.
		"""
		return { chunk.split(';')[0]:float(chunk.split(';')[1]) for chunk in line.split(' ') }


class Reader:
	"""
		This class is responsible for getting lines from raw_input.

		Exemple :
			Input : "loyer;-485.00 restaurant;-32.50 retrait;-40.00 salaire;2300.00"
			Output : {'loyer': -485.00, 'restaurant': -32.50, "retrait": -40.00, "salaire": 2300.00} 
	"""

	def __init__(self):
		self.nb_rows = None

	def start_process(self):
		self.nb_rows = self.get_nb_rows_from_user()
		if self.nb_rows is None:
			print 'Input must be an Integer'
			return
		else:
			self.get_lines()
	
	def get_nb_rows_from_user(self):
		"Asks for a number to a user. If input is not a proper number, return None"
		number = raw_input()
		try:
			return int(number)
		except ValueError:
			return None
	
	def get_lines(self):
		"Reads lines from raw_input"
		self.lines = [raw_input() for i in xrange(0, self.nb_rows)]
		return self.lines

class Lemmer:
	"""
		This class takes a list of words and reduces it to a list of lems.

		a lem is defined as such:
			- if a period is at the end of a word, it is a synonym of another world
			- a synonym has at least 3 letters
			- "salaire" is equivalent to : "salair." "salai." "sala." "sal."
	"""

	def __init__(self, lines = None):
		"Defined either by a dict with string keys or list of words"
		self.lines = lines
		self.words = []
		[[self.words.append(word) for word in line.keys()] for line in self.lines]
		self.words =  set(self.words)
		self.words_association = {}
		self.unique_lines = set()
	
	def build_association(self):
		primaries = [w for w in self.words if w[-1] != '.' ]
		secondaries = [w for w in self.words if w[-1] == '.' ]
		self.words_association = {}
		[self.words_association.update({w:w}) for w in primaries]
		[[self.words_association.update({sw:w}) for sw in secondaries if self.are_synonyms(w, sw) ] for w in primaries]
		

	def are_synonyms(self, primary_word, secondary_word):
		"""
			Returns true if secondary word is a contraction of primary word
		"""
		try:
			return primary_word.index(secondary_word[:-1]) == 0 and secondary_word[-1] == '.'
		except ValueError:
			return False

	def reduce(self):
		"Finding all synonyms and building reduced data"
		self.build_association()
		self.reduce_lines()
	
	def reduce_lines(self):
		self.reduce_lines = []
		[ [ self.reduce_lines.append(( self.words_association[k] , v)) for k, v in line.iteritems() ] for line in self.lines ]
		self.unique_lines = set(self.reduce_lines)
	
	def extract_frequency(self, threshold = 0):
		reduced = [ ( element , len([1 for e in self.reduce_lines if e == element]) )  for element in self.unique_lines ]
		return [r for r in reduced if r[-1] >=threshold]

class Displayer:
	"""
		Displaying information on screen
	"""
	
	def __init__(self, recurent_operations):
		self.recurent_operations = recurent_operations
		self.process()
	
	def process(self):
		"Extracting relevant informations for display"
		self.nb_r_operations = len(self.recurent_operations)
		self.sum_r_operatins = sum([ r[0][1] for r in self.recurent_operations])
	
	def display(self):
		"Display appears here"
		self.sum_r_operatins = int(10*self.sum_r_operatins)/10.0
		sum_r_operatins = str(self.sum_r_operatins)
		decimals = sum_r_operatins.split('.')[-1]
		if len(decimals)<2:
			sum_r_operatins = sum_r_operatins +'0' # we always need to display 2 numbers after period
		print str(self.nb_r_operations)+';'+sum_r_operatins

def main():
	# Reading data 
	reader = Reader()
	reader.start_process()

	# Structuring data
	converter = Converter(reader.lines)
	converter.convert()
	
	# Reducing keys to lems (working on synonyms)
	lemmer = Lemmer(converter.structured_data )
	lemmer.reduce()
	# Extrating recurring data and display it
	recurent_operations = lemmer.extract_frequency(threshold = reader.nb_rows)
	displayer = Displayer(recurent_operations)
	displayer.display()

main()
