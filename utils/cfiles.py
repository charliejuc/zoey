from utils.cdict import get_joined_dict_lists

import settings

s_excluded = settings.excluded
excluded_sep = ':'

def get_excluded(key):
	return get_joined_dict_lists(s_excluded, key, excluded_sep)

def write_file(file_path, data, binary=False):
	mode = 'w'
	if binary:
		mode += 'b'

	with open(file_path, mode) as file:
		file.write(data)

def read_file(file_path, binary=False):
	mode = 'r'
	if binary:
		mode += 'b'

	with open(file_path, mode) as file:
		return file.read()