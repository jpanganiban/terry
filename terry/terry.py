class TerryException(Exception):
	def __str__(self):
		return 'Which Terry?'

raise TerryException