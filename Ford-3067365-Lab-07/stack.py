'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/27/2022
Purpose: Create a node-based stack class that handles
         the nodes inside our stack.
'''

from node import Node

class Stack:
        def __init__(self):
                self._top = None

        #adds an entry to the top of the stack
        def push(self, entry):
                temp = self._top
                self._top = Node(entry)
                self._top.next = temp

        #removes the entry at the top of the stack
        def pop(self):
                if not self.is_empty():
                        temp = self._top
                        self._top = self._top.next
                        return temp.entry

                raise RuntimeError("Stack is empty")

        #returns the entry at the top of the stack
        def peek(self):
                if not self.is_empty():
                        return self._top.entry

                raise RuntimeError("Stack is empty")

        #checks to see if the stack is empty
        def is_empty(self):
                if self._top == None:
                        return True

                return False
