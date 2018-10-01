#BlackJack Game : Exceptions
#By Nikodem Celiński 

#file created : 14:00 | 01.10.18 

class MovementFail(Exceptions) :
	def __init__(self,msg):
		self.msg=msg

	def print_exception(self):
		print("Movement_Error:",self.msg)