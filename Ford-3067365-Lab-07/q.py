'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/27/2022
Purpose: Create a node-based queue class that handles
         the nodes inside our queue.
'''

from node import Node

class Queue:
        def __init__(self):
                self._front = None
                self._back = None

        #adds an entry to the back of the queue
        def enqueue(self, entry):
                if self.is_empty():
                        self._front = Node(entry)
                        self._back = self._front

                else:
                        self._back.next = Node(entry)
                        self._back = self._back.next

        #removes the entry at the front of the queue
        def dequeue(self):
                if not self.is_empty():
                        temp = self._front
                        self._front = self._front.next
                        return temp.entry

                raise RuntimeError("Queue is empty")

        #returns the entry at the front of the queue
        def peek_front(self):
                if not self.is_empty():
                        return self._front.entry

                raise RuntimeError("Queue is empty")

        #checks to see if the queue is empty
        def is_empty(self):
                if self._front == None:
                        return True

                return False
