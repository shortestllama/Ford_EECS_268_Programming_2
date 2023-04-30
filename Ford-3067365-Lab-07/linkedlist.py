'''
Author: Jack Ford
KUID: 3067365
Date: 03/07/2022
Lab: Lab 04
Last modified: 03/09/2022
Purpose: Create a node-based linked list class that handles
         the nodes inside our linked list.
'''

from node import Node

class LinkedList:
        def __init__(self):
                self._front = None
                self._length = 0

        #returns the length of the linked list
        def length(self):
                return self._length

        #inserts an entry into the linked list at the given
        #index and adds one to the length
        def insert(self, index, entry):
                _node = Node(entry)

                if index > (self._length) or index < 0:
                        raise RuntimeError("Index is invalid")

                if self._length == 0:
                        self._length += 1
                        self._front = _node

                else:
                        if index == 0:
                                temp = self._front
                                self._front = _node
                                self._front.next = temp

                        elif index == self._length:
                                jumper = self._front

                                for _ in range(index - 1):
                                        jumper = jumper.next

                                jumper.next = _node

                        else:
                                jumper = self._front

                                for _ in range(index - 1):
                                        jumper = jumper.next

                                temp = jumper.next
                                jumper.next = _node
                                _node.next = temp

                        self._length += 1

        #removes the node at the index from the linked list
        #and subtracts one from the length of the linked list
        def remove(self, index):
                if index > (self._length - 1) or index < 0:
                        raise RuntimeError("Index is invalid")

                if self._length == 0:
                        raise RuntimeError("Can't remove from empty list")

                else:
                        if index == 0:
                                self._front = self._front.next

                        elif index == self._length - 1:
                                jumper = self._front

                                for _ in range(index - 1):
                                        jumper = jumper.next

                                jumper.next = None

                        else:
                                temp = self._front
                                jumper = self._front

                                for _ in range(index + 1):
                                        temp = temp.next

                                for _ in range(index - 1):
                                        jumper = jumper.next

                                jumper.next = temp

                        self._length = self._length - 1

        #returns the entry at the index of the linked list
        def get_entry(self, index):
                jumper = self._front

                if index > (self._length - 1) or index < 0:
                        raise RuntimeError("Index is invalid")

                else:
                        for _ in range(index):
                                jumper = jumper.next

                        return jumper.entry

        #changes the entry at the index of the linked list
        #to the given entry
        def set_entry(self, index, entry):
                jumper = self._front

                if index > (self._length - 1) or index < 0:
                        raise RuntimeError("Index is invalid")

                else:
                        for _ in range(index):
                                jumper = jumper.next

                        jumper.entry = entry

        #clears the linked list
        def clear(self):
                self._front = None
                self._length = 0
