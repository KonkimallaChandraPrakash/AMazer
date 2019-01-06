from lib.maze import Maze
import sys

# Input Parser
def parser(maze,inp):
	'''
	Args:
		maze : input maze
		inp : input command from user
	'''
	inp_strip = inp.split(' ')
	# For Help
	if inp=="h" or inp=="help":
		print("-"*50)
		print('These are the helpful commands in the game:- ')
		print("h, help --- for commands information")
		print("[Enter] --- to go in the previous direction(Starts with south)")
		print("Directions :-")
		print('\t',"N (or) n (or) north --- for moving in North direction")
		print('\t',"S (or) s (or) south --- for moving in South direction")
		print('\t',"E (or) e (or) east --- for moving in East direction")
		print('\t',"W (or) w (or) west --- for moving in West direction")
		print("L [num] --- to change to level [num] Example : L 2")
		print("Exit --- for exit")
		print("-"*50)
	# Using previous direction
	elif inp=="":
		print()
		done = maze.action()
		if done:
			print()
			print("****************************")
			print("*******-***********-********")
			print("******---*********---*******")
			print("*******-*****-*****-********")
			print("****************************")
			print("*******--*********--********")
			print("*********---**---***********")
			print("***********----*************")
			maze.level_increment()
	# Exit the program
	elif inp=="Exit":
		sys.exit()
	# For Level change
	elif len(inp_strip)==2 and inp_strip[0]=="L":
		print()
		maze.level_change(int(inp_strip[1]))
	# For Action
	elif len(inp_strip)==1:
		print()
		done = maze.action(inp_strip[0])
		if done:
			print()
			print("****************************")
			print("*******-***********-********")
			print("******---*********---*******")
			print("*******-*****-*****-********")
			print("****************************")
			print("*******--*********--********")
			print("*********---**---***********")
			print("***********----*************")
			maze.level_increment()
	else:
		print("Unsupported action!!!")
		parser(maze,"h")

if __name__=="__main__":
	play = 1 # Always Playing
	maze = Maze()
	parser(maze,"h")
	while play:
		inp = input("Next Command:- ")
		parser(maze,inp)