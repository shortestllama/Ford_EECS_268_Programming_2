'''
Author: Jack Ford
KUID: 3067365
Date: 04/03/2022
Lab: Lab 06
Last modified: 04/04/2022
Purpose: Get a map from the user and return the blob's path along
	 with how many people the blob ate.
'''

#recursive method that moves the blob and adds to the total
def blob(grid, x, y):
#checks to see if the current square is valid
	if is_safe(grid, x, y):
#if the current square is an S, B takes it's place
		if grid[x][y] == 'S':
			grid[x][y] = 'B'

#if the current square is a P, 1 is added to the total and B takes
#it's place
		elif grid[x][y] == 'P':
			global total
			total = total + 1
			grid[x][y] = 'B'

#checks in all directions for another sewer if the current square
#is a sewer, then keeps going normally
		elif grid[x][y] == '@':
#checks all squares to the left of the current square
			for i in range(0, y):
				if grid[x][i] == '@':
					blob(grid, x - 1, i) #up
					blob(grid, x, i + 1) #right
					blob(grid, x + 1, i) #down
					blob(grid, x, i - 1) #left

#checks all squares to the right of the current square
			for i in range(y + 1, len(grid)):
				if grid[x][i] == '@':
					blob(grid, x - 1, i) #up
					blob(grid, x, i + 1) #right
					blob(grid, x + 1, i) #down
					blob(grid, x, i - 1) #left

#checks all squares below the current square
			for i in range(0, x):
				if grid[i][y] == '@':
					blob(grid, i - 1, y) #up
					blob(grid, i, y + 1) #right
					blob(grid, i + 1, y) #down
					blob(grid, i, y - 1) #left

#checks all squares above the current square
			for i in range(x + 1, len(grid[0])):
				if grid[i][y] == '@':
					blob(grid, i - 1, y) #up
					blob(grid, i, y + 1) #right
					blob(grid, i + 1, y) #down
					blob(grid, i, y - 1) #left

		blob(grid, x - 1, y) #up
		blob(grid, x, y + 1) #right
		blob(grid, x + 1, y) #down
		blob(grid, x, y - 1) #left

	return 0

#method that checks to see if the current square is valid
def is_safe(grid, x, y):
	if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and (grid[x][y] == 'S' or grid[x][y] == 'P' or grid[x][y] == '@'):
		return True

	return False

#main method that gets user input and outputs the correct informat
def main():
	global total
	total = 0
#gets a file from the user and checks to see if it's valid
	file = input('Please enter a file name: ')

	try:
		file_in = open(file, 'r')

	except:
		raise RuntimeError('File does not exist.')

	grid = []
	lines = []

	try:
		for line in file_in:
			line = line.replace('\n', '')
			lines.append(line)

	except:
		print('File does not exist.')

#assigns each line to a respective list for the grid size,
#start position, and the grid itself
	for i in range(len(lines)):
		if i == 0:
			grid_size = lines[i].split(' ')

		elif i == 1:
			start = lines[i].split(' ')

		else:
			grid.append(list(lines[i]))

#returns an error if the map is not big enough
	if int(grid_size[0]) < 1 or int(grid_size[1]) < 1:
		raise RuntimeError('Map is not big enough.')

#returns an error if the starting position is not within the given range
	if int(start[0]) < 0 or int(start[0]) >= int(grid_size[0]) or int(start[1]) < 0 or int(start[1]) >= int(grid_size[1]):
		raise RuntimeError('Start position not within range.')

	blob(grid, int(start[0]), int(start[1]))

#prints the grid and total after the recursive function is called
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end='')

		print('\n')

	print('Total eaten: ' + str(total))

if __name__ == '__main__':
	main()
