from lib.matrix import Mat
import sys

# Class for playing the maze game
class Maze():

	# Initialization of variables
	def __init__(self,level=1):
		'''
		Args : 
			level : integer level number
		Returns:
			None
		'''
		self.__mat = Mat()
		if self.level_change(level,True):
			self.__x = 0
			self.__y = 0
			self.__curlevel = level
			self.__M = len(self.__mazeMatrix)
			self.__N = len(self.__mazeMatrix[0])
			self.__dirs = {"N":[-1,0],"S":[1,0],"E":[0,1],"W":[0,-1]}
			self.__dirnow = "S"
			print("-"*50)
			print("Created Maze matrix.")
			print("Let's play the game :) !!!!")
			print("-"*50)

	# Returns the size of the Matrix
	def __target(self):
		'''
		Args:
			None
		Returns:
			tuple of ints indicating the target position to reach to complete the game
		'''
		return (self.__M-1,self.__N-1)

	# Returns the current position in the Maze
	def __state(self):
		'''
		Args:
			None
		Returns:
			tuple of ints indicating the current position in the game
		'''
		return (self.__x,self.__y)

	# Change Level
	def level_change(self,level,init=False):
		'''
		Args:
			level : integer level number
			init : boolean value indicating it was called during maze initialization or level changing
		Returns:
			Boolean value indicating whether the level is changed or not
		'''
		if self.__mat.issupported(level):
			self.__mazeMatrix = self.__mat.matrix(level)
			self.__x = 0
			self.__y = 0
			self.__curlevel = level
			self.__M = len(self.__mazeMatrix)
			self.__N = len(self.__mazeMatrix[0])
			if not init: 
				print("*"*50);print("Updated Level to :-",level)
			else:
				print("Level Number :- ", level)
			return True
		return False
	
	# Increments the level in the game
	def level_increment(self):
		'''
		Args:
			None
		Returns:
			None
		'''
		if not self.__mat.issupported(self.__curlevel+1,log=False):
			print("Congratulations you are done with the game!!!")
			sys.exit()
		else:
			print("Now you can play next level :D !!!")
			self.level_change(self.__curlevel+1)

	# Updates the direction of travel
	def __update_dir(self,dir_str):
		'''
		Args:
			dir_str : string indicating the direction to which __dirnow has to be updated
		Returns:
			Boolean value indicating if the update was possible
		'''
		dir_str = dir_str.upper()
		if dir_str=="N" or dir_str=="NORTH":
			self.__dirnow = "N"
		elif dir_str=="S" or dir_str=="SOUTH":
			self.__dirnow = "S"
		elif dir_str=="E" or dir_str=="EAST":
			self.__dirnow = "E"
		elif dir_str=="W" or dir_str=="WEST":
			self.__dirnow = "W"
		else:
			return False
		return True

	# Take action in a direction
	def action(self,direction=None):
		'''
		Args:
			direction : string indicating the direction to which it has to move
						uses previous direction if it is None
		Returns:
			Boolean value indicating whether the action lead to end of the current level
		'''
		if direction:
			if not self.__update_dir(direction):
				print("The direction given is incorrect!!!\n Possible directions are \"North(N)\", \"South(S)\", \"East(E)\" and \"West(W)\"")
				return False
		update = self.__dirs[self.__dirnow]
		if (0<=self.__x+update[0]<self.__M) and (0<=self.__y+update[1]<self.__N):
			if self.__mazeMatrix[self.__x+update[0]][self.__y+update[1]]:
				self.__x += update[0]
				self.__y += update[1]
			else:
				print("Encountered an obstacle cannot move in that direction!!!")
		else:
			print("Encountered a wall cannot move in that direction!!!")
		print("Current position : ",self.__state(),", Target location : ",self.__target())
		return self.__state()==self.__target()