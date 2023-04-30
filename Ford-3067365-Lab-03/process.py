'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/27/2022
Purpose: Provide methods for a process to be able
	 to execute in order to carry out the
	 desired command
'''

from queue import Queue
from stack import Stack

class Process:
	def __init__(self, name):
		self.name = name
		self.call_stack = Stack()
		self.call_stack.push("main")

	#adds a function to the process' call stack
	def call(self, func):
		self.call_stack.push(func)

	#returns the function at the top of the
	#process' call stack
	def ret(self):
		return self.call_stack.pop()
