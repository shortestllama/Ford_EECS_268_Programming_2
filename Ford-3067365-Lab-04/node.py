'''
Author: Jack Ford
KUID: 3067365
Date: 03/06/2022
Lab: Lab 04
Last modified: 03/06/2022
Purpose: Create a node class to handle the nodes that get used.
'''

class Node:
	def __init__(self, entry):
		self.entry = entry
		self.next = None
