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

def main():
	# Reading data 
	reader = Reader()
	reader.start_process()

	# Structuring data
	converter = Converter(reader.lines)
	converter.convert()
	
	# Reducing keys to lems (working on synonyms)

	# Extrating recurring data



main()
