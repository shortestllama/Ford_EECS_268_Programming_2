'''
Author: Jack Ford
KUID: 3067365
Date: 03/07/2022
Lab: Lab 04
Last modified: 03/09/2022
Purpose: Get a file of commands from the user, create a
	 list of commands using that file, and execute
	 each command on the browser object.
'''

from browser import Browser

def main():
	b = Browser()
	commands = []
	file = input("Please enter a file name: ")
	inp = open(file, "r")

	#creates a list of commands where each command
	#is a line of the input file
	for line in inp:
		line = line.replace("\n", "")
		commands.append(line)

	#performs the appropriate actions based on
	#what the next command in the list is
	for command in commands:
		if "NAVIGATE" in command:
			b.navigate_to(command[9::])

		elif "BACK" in command:
			b.back()

		elif "FORWARD" in command:
			b.forward()

		elif "HISTORY" in command:
			print(b.history())

if __name__ == '__main__':
	main()
