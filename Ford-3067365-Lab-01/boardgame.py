'''
Author: Jack Ford
KUID: 3067365
Date: 1/24/2022
Lab: Lab 01
Last modified: 1/26/2022
Purpose: Create a Boardgame class with getters for certain parameters,
	 a difference method, and a string magic method.
'''

class Boardgame:
	def __init__(self, name, year, gr, pr, mp, mt):
		self.name = name
		self.year = year
		self.gr = gr
		self.pr = pr
		self.mp = mp
		self.mt = mt

	def get_year(self):
		return self.year

	def get_gr(self):
		return self.gr

	def get_mt(self):
		return self.mt

	#return the absolute value of the difference between gibbon's
	#rating and the peoples' rating
	def difference(self):
		return abs(self.gr - self.pr)

	def __str__(self):
		return f"{self.name} ({self.year}) [GR={self.gr}, PR={self.pr}, MP={self.mp}, MT={self.mt}]"
