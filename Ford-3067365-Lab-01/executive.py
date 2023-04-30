'''
Author: Jack Ford
KUID: 3067365
Date: 1/24/2022
Lab: Lab 01
Last modified: 1/26/2022
Purpose: Execute the main function as well as interact with the user.
'''

from boardgame import Boardgame

class Executive:
	def __init__(self, file):
		self.file = file
		self.boardgames = []

	#creates a list of boardgames based on information from the file,
	#then calls the other two methods in this class
	def run(self):
		boardgame_file = open(self.file)

		for line in boardgame_file:
			line = line.replace('\n', '')
			temp_list = line.split('\t')
			boardgame = Boardgame(temp_list[0], int(temp_list[1]), float(temp_list[2]), float(temp_list[3]), int(temp_list[4]), int(temp_list[5]))
			self.boardgames.append(boardgame)

		self.print_menu()
		self.user_interaction()

		boardgame_file.close()

	#prints the menu
	def print_menu(self):
		print('1. Print all games')
		print('2. Print all games from a year')
		print('3. Print all games between a ranking range')
		print('4. The People VS Dr. Gibbons')
		print('5. Print based on play time')
		print('6. Exit')

	#obtains a menu option from the user and carries out that
	#corresponding menu function
	#loops until the user selects exit
	def user_interaction(self):
		choice = int(input("Please select an option: "))

		while choice != 6:
			if choice == 1:
				for boardgame in self.boardgames:
					print(boardgame)

			elif choice == 2:
				count = 0
				user_year = int(input("Please enter a year: "))

				for boardgame in self.boardgames:
					if boardgame.get_year() == user_year:
						print(boardgame)
						count += 1

				if count == 0:
					print("No games found")

			elif choice == 3:
				low = -1
				hi = 11

				while low < 0 or low > 10:
					low = float(input("Please enter a valid lower bound: "))

				while hi < 0 or hi > 10:
					hi = float(input("Please enter a valid upper bound: "))

				for boardgame in self.boardgames:
					if boardgame.get_gr() > low and boardgame.get_gr() < hi:
						print(boardgame)

			elif choice == 4:
				test = -1

				while test < 0 or test > 10:
					test = float(input("Please enter a number between 0 and 10: "))

				for boardgame in self.boardgames:
					if boardgame.difference() >= test:
						print(boardgame)

			elif choice == 5:
				pt = int(input("Please enter a play time: "))

				while pt < 0:
					pt = int(input("Please enter a valid play time: "))

				for boardgame in self.boardgames:
					if boardgame.get_mt() <= pt:
						print(boardgame)

			elif choice > 6:
				choice = int(input("Please enter a valid option: "))

			self.print_menu()
			choice = int(input("Please select an option: "))
