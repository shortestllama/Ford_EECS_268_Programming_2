'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/15/2022
Purpose: Create a node class to handle the nodes that get used.
'''

class Node:
        def __init__(self, entry):
                self.entry = entry
                self.next = None
