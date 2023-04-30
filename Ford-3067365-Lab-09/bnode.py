'''
Author: Jack Ford
KUID: 3067365
Date: 04/23/2022
Lab: Lab 09
Last modified: 05/02/2022
Purpose: Create a binary node class to help create our binary search tree
'''

class BNode:
	def __init__(self, entry):
		self.entry = entry
		self.left = None
		self.right = None
