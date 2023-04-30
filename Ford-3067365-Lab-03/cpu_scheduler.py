'''
Author: Jack Ford
KUID: 3067365
Date: 02/15/2022
Lab: Lab 03
Last modified: 02/27/2022
Purpose: Creates a list of commands for each line
	 of the input file, then does the necessary
	 actions for each command that appears in
	 the list of commands.
'''

from process import Process
from queue import Queue

class CPU:
	def __init__(self, file):
		self.file = file

	#the main method that handles the funcitonality
	#of the program
	def run(self):
		q = Queue()
		commands = []
		input = open(self.file, "r")

		#creates a list of commands where each command
		#is a line of the input file
		for line in input:
			line = line.replace("\n", "")
			commands.append(line)

		#performs the appropriate actions based on
		#what the next command in the list is
		for command in commands:
			if "START" in command:
				temp_process = Process(command[6::])
				q.enqueue(temp_process)
				print(f"{command[6::]} added to queue")

			elif "CALL" in command:
				curr_process = q.peek_front()
				curr_process.call(command[5::])
				moving_process = q.dequeue()
				q.enqueue(moving_process)
				print(f"{curr_process.name} called {command[5::]}")

			elif "RETURN" in command:
				curr_process = q.peek_front()
				func = curr_process.ret()
				print(f"{curr_process.name} returned {func}")

				if curr_process.call_stack.is_empty():
					q.dequeue()
					print(f"{curr_process.name} process has ended")

				else:
					temp = q.dequeue()
					q.enqueue(temp)
