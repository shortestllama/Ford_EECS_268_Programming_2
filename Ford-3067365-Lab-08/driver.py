'''
Author: Jack Ford
KUID: 3067365
Date: 04/24/2022
Lab: Lab 08
Last modified: 04/25/2022
Purpose: Obtain a file from the user, create a pokedex using the
	 binary search tree, and allow the user to perform actions
	 on the pokedex from a set of menu options
'''

from binarytree import BinaryTree
from pokemon import Pokemon

#print the menu the user gets to choose from
def menu():
	print('---------')
	print('1. Search')
	print('2. Add')
	print('3. Print')
	print('4. Quit')
	print('---------')

#performs the main function of the program
def main():
	#get a file from the user, add each pokemon's attributes to a list
	#and then add those lists to another list in order to create
	#pokemon to add to the binary search tree
	pokedex = BinaryTree()
	file = input('Please enter a file: ')

	try:
		file_in = open(file, 'r')

	except:
		raise RuntimeError('File does not exist.')

	pokelist = []

	try:
		for line in file_in:
			line = line.replace('\n', '')
			temp = line.split('\t')
			temp[1] = int(temp[1])
			pokelist.append(temp)

	except:
		print('File does not exist.')

	for poke in pokelist:
		temp = Pokemon(poke[0], poke[1], poke[2])
		pokedex.add(temp)

	#continually prints the menu and asks the user to select an
	#option until the user decides to quit
	choice = 0

	while choice != 4:
		menu()

		try:
			choice = int(input('Please select an option: '))

		except:
			raise RuntimeError('Invalid input.')

		#searches for the given id in the binary search tree
		#and prints the information for that pokemon
		if choice == 1:
			try:
				id = int(input('Please enter a pokedex id: '))

			except:
				raise RuntimeError('Invalid input.')

			pokemon = pokedex.search(id)
			print(f'American name: {pokemon.a_name}')
			print(f'Pokedex number: {pokemon.id}')
			print(f'Japanese name: {pokemon.j_name}')

		#asks the user for the attributes for a new pokemon,
		#then adds the pokemon to the pokedex
		elif choice == 2:
			try:
				a_name = input('Please enter a new Pokemon name: ')
				id = int(input('Please enter the Pokedex number: '))
				j_name = input('Please enter the Japanese name: ')

			except:
				raise RuntimeError('Invalid input.')

			pokedex.add(Pokemon(a_name, id, j_name))

		#asks the user for a traversal order, then prints the
		#binary search tree in that order
		elif choice == 3:
			try:
				order = input('Please enter a traversal order (in, pre, post): ')

			except:
				raise RuntimeError('Invalid input.')

			if order == 'in':
				for pokemon in pokedex.in_order_traversal(pokedex._root):
					print(pokemon)

			elif order == 'pre':
				for pokemon in pokedex.pre_order_traversal(pokedex._root):
					print(pokemon)

			elif order == 'post':
				for pokemon in pokedex.post_order_traversal(pokedex._root):
					print(pokemon)

		elif choice != 4:
			raise RuntimeError('Selection not on menu.')

if __name__ == '__main__':
	main()
