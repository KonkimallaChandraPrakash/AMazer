# Class definition for Matrix Maps for each level
class Mat:

	# Initialization
	def __init__(self):
		# Current supported minimum and maximum levels
		'''
		Args:
		 	None
		Returns:
			None
		'''
		self.min = 1
		self.max = 5

	# To check if a level is supported
	def issupported(self,level,log=True):
		'''
		Args:
			level : integer level number
			log : boolean to control logging information
		Returns:
			A boolean True if the level is supported else False
		'''
		if self.min<=level<=self.max:
			return True
		elif level<1 and log:
			print('We are only positive :)')
		elif log:
			print('Under Construction :)')
		return False

	# Matrix Maps
	def matrix(self,level=1):
		'''
		Args:
			level : integer level number
		Returns:
			A Map which is a matrix of ones and zeros
		'''
		if level==1:
			return [
				[1,1],
				[0,1]
			]

		elif level==2:
			return [
				[1,1,0],
				[0,1,0],
				[1,1,1],
			]

		elif level==3:
			return [
				[1,1,0,1],
				[0,1,1,0],
				[1,0,1,1],
				[1,0,0,1],
			]

		elif level==4:
			return [
				[1,1,1,1,0,1],
				[0,1,0,1,1,0],
				[1,1,1,1,0,1],
				[0,1,0,1,1,1],
				[1,1,1,1,0,1],
			]

		elif level==5:
			return [
				[1,1,1,1,0,1,1,0],
				[0,1,0,1,1,0,1,1],
				[1,1,1,1,0,1,1,0],
				[0,1,0,1,1,1,1,1],
				[1,1,1,1,0,0,1,0],
				[0,1,0,1,1,0,1,1],
			]