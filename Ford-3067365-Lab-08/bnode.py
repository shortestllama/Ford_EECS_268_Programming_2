'''
Author: Jack Ford
KUID: 3067365
Date: 04/23/2022
Lab: Lab 08
Last modified: 04/25/2022
Purpose: Create a binary node class to help create our binary search tree
'''

class BNode:
	def __init__(self, entry):
		self.entry = entry
		self.left = None
		self.right = None
