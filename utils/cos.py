from subprocess import Popen, PIPE
import os

makedirs = os.makedirs

def zmakedirs(_path):
	try:
		makedirs(_path)
		return True

	except FileExistsError as e:
		return False


def run_cmd(cmd, **kwargs):
	popen_kwargs = { 
		'stdout': PIPE,
		'stderr': PIPE,
		'shell': True
	}

	popen_kwargs.update(kwargs)

	process = Popen(cmd, **popen_kwargs)

	output, err = process.communicate()

	return output, err, process.returncode