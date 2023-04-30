'''
Author: Jack Ford
KUID: 3067365
Date: 03/07/2022
Lab: Lab 04
Last modified: 03/09/2022
Purpose: Create a linked list-based browser class that
	 performs the file-given commands on the browser
	 using the linked list
'''

from linkedlist import LinkedList

class Browser:
	def __init__(self):
		self._list = LinkedList()
		self._pointer = -1

	#inserts the given url at the index after the pointer
	def navigate_to(self, url):
		self._list.insert(self._pointer + 1, url)

		#removes the urls that follow the given url
		#if the url was not inserted at the end of
		#the linked list
		if self._pointer < self._list.length() - 1:
			temp = self._pointer + 2

			while self._list.length() - 1 > self._pointer + 1:
				self._list.remove(self._list.length() - 1)

		self._pointer += 1

	#moves the pointer so that it is pointing at the next
	#url in the browser history, or node in the linked list
	def forward(self):
		if self._pointer < self._list.length() - 1:
			self._pointer += 1

		else:
			self._pointer = self._pointer

	#moves the pointer so that it is pointing at the last
	#url in the browser history, or node in the linked list
	def back(self):
		if self._pointer > 0:
			self._pointer = self._pointer - 1

		else:
			self._pointer = self._pointer

	#prints the urls visited in order and labels the current url
	def history(self):
		hist = "Oldest\n============\n"
		new = "============\nNewest\n"

		for i in range(self._list.length()):
			if i == self._pointer:
				hist += f"{self._list.get_entry(i)} <==current\n"

			else:
				hist += f"{self._list.get_entry(i)}\n"

		return hist + new
