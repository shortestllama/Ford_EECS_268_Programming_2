'''
Author: Jack Ford
KUID: 3067365
Date: 04/24/2022
Lab: Lab 08
Last modified: 04/25/2022
Purpose: Create a binary tree class to add items to the binary tree,
	 search for items in the tree, and return a list of the
	 binary tree traversed in different orders
'''

from bnode import BNode
from pokemon import Pokemon

class BinaryTree:
	def __init__(self):
		self._root = None

	#checks the first three nodes to see if they can be added to,
	#otherwise calls the recursive add function
	def add(self, entry):
		if self._root == None:
			self._root = BNode(entry)

		elif self._root.entry > entry:
			if self._root.left == None:
				self._root.left = BNode(entry)

			else: self._rec_add(entry, self._root)

		elif self._root.entry < entry:
			if self._root.right == None:
				self._root.right = BNode(entry)

			else:
				self._rec_add(entry, self._root.right)

		else:
			raise RuntimeError('No duplicates allowed.')

	#calls the recursive search function
	def search(self, target):
		return self._rec_search(target, self._root)

	#returns the entry at the node being searched for
	def _rec_search(self, target, cur_node):
		if cur_node == None:
			raise RuntimeError('Target not found.')

		elif cur_node.entry.id == target:
			return cur_node.entry

		elif cur_node.entry.id < target:
			return self._rec_search(target, cur_node.right)

		elif cur_node.entry.id > target:
			return self._rec_search(target, cur_node.left)

	#adds the entry at the node based on the rules meant for adding
	#items to a binary search tree
	def _rec_add(self, entry, cur_node):
		if cur_node.entry > entry:
			if cur_node.left == None:
				cur_node.left = BNode(entry)

			else:
				self._rec_add(entry, cur_node.left)

		elif cur_node.entry < entry:
			if cur_node.right == None:
				cur_node.right = BNode(entry)

			else:
				self._rec_add(entry, cur_node.right)

		else:
			raise RuntimeError('No duplicates allowed.')

	#returns a list of the items in the tree traversed in order
	def in_order_traversal(self, cur_node):
		ans = []

		if cur_node != None:
			ans = self.in_order_traversal(cur_node.left)
			ans.append(cur_node.entry)
			ans = ans + self.in_order_traversal(cur_node.right)

		return ans

	#returns a list of the items in the tree traversed pre order
	def pre_order_traversal(self, cur_node):
		ans = []

		if cur_node != None:
			ans.append(cur_node.entry)
			ans = ans + self.pre_order_traversal(cur_node.left)
			ans = ans + self.pre_order_traversal(cur_node.right)

		return ans

	#returns a list of the items in the tree traversed post order
	def post_order_traversal(self, cur_node):
		ans = []

		if cur_node != None:
			ans = self.post_order_traversal(cur_node.left)
			ans = ans + self.post_order_traversal(cur_node.right)
			ans.append(cur_node.entry)

		return ans
