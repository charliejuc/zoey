import os

makedirs = os.makedirs

def zmakedirs(_path):
	try:
		makedirs(_path)
		return True

	except FileExistsError as e:
		return False