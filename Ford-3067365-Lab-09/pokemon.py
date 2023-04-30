'''
Author: Jack Ford
KUID: 3067365
Date: 04/24/2022
Lab: Lab 09
Last modified: 05/02/2022
Purpose: Create a class of pokemon that overloads some comparison
	 operators and has a string magic method
'''

class Pokemon:
	def __init__(self, a_name, id, j_name):
		self.a_name = a_name
		self.id = id
		self.j_name = j_name

	#compares two given pokemon to see if the id of the first is
	#less than the id of the second
	def __lt__(self, other):
		return self.id < other.id

	#compares two given pokemon to see if the ids are equal
	def __eq__(self, other):
		return self.id == other.id

	#compares two given pokemon to see if the id of the first is
	#greater than the id of the second
	def __gt__(self, other):
		return not (self < other)

	#returns a string for a pokemon
	def __str__(self):
		return f'{self.a_name}\t{self.id}\t{self.j_name}'
