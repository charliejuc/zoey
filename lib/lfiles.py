from utils.cre import remove_excluded
from utils.cdict import dict_list_append
from utils.cfiles import get_excluded

from lib.ljson import read_zoey_json_file

import os, re

splitext = os.path.splitext
path_join = os.path.join
re_sub = re.sub

def get_files_by_ext(directory, exclude=list(), *args, **kwargs):
	exclude_conf = kwargs.get('exclude_conf')
	json_file_exclude = read_zoey_json_file().get('exclude')

	if exclude_conf:
		exclude += get_excluded(exclude_conf)

	if json_file_exclude:
		exclude += json_file_exclude

	fbe = dict()
	empty_str = ''

	def exclude_full_path_root(l, root, exclude):
		_l = remove_excluded(
			(path_join(root, e) for e in l), 
			exclude
		)

		slash = '/'
		if not root.endswith(slash):
			root += slash

		return [ re_sub(root, empty_str, e) for e in _l ]

	for root, dirs, files in os.walk(directory, topdown=True):
		dirs[:] = exclude_full_path_root(dirs, root, exclude)
		files = exclude_full_path_root(files, root, exclude)

		for filename in files:
			ext = splitext(filename)[1][1:]
			_t = ( root, filename )

			dict_list_append(fbe, ext, _t)

	return fbe