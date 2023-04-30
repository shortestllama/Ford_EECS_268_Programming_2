'''
Author: Jack Ford
KUID: 3067365
Date: 04/24/2022
Lab: Lab 09
Last modified: 05/02/2022
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

	#calls the recursive remove function
	def remove(self, target):
		return self._rec_remove(self._root, target)

	#makes a new tree, then calls the recursive copy function
	def copy(self):
		tree = BinaryTree()
		tree._root = self._rec_copy(self._root)
		return tree

	#returns a copy of the root and subtrees
	def _rec_copy(self, cur_node):
		if cur_node is None:
			return None

		cur_node_copy = BNode(cur_node.entry)
		cur_node_copy.left = self._rec_copy(cur_node.left)
		cur_node_copy.right = self._rec_copy(cur_node.right)

		return cur_node_copy

	#removes the node at the target key
	def _rec_remove(self, cur_node, target):
		if cur_node is None:
			return cur_node

		if target < cur_node.entry.id:
			cur_node.left = self._rec_remove(cur_node.left, target)

		elif target > cur_node.entry.id:
			cur_node.right = self._rec_remove(cur_node.right, target)

		else:
			if cur_node.left is None:
				temp = cur_node.right
				cur_node = None
				return temp

			elif cur_node.right is None:
				temp = cur_node.left
				cur_node = None
				return temp

			temp = self.max_value(cur_node.left)
			cur_node.entry.id = temp.entry.id
			cur_node.left = self._rec_remove(cur_node.left, temp.entry.id)

		return cur_node

	#utility function to find the maximum value in the BST
	def max_value(self, target_node):
		while(target_node.right is not None):
			target_node = target_node.right

		return target_node

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
