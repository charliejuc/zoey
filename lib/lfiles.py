from utils.cre import remove_excluded
from utils.cdict import dict_list_append
from utils.cfiles import get_excluded

import os, re

splitext = os.path.splitext
path_join = os.path.join
re_sub = re.sub

def get_files_by_ext(directory, exclude=list(), *args, **kwargs):
	exclude_conf = kwargs.get('exclude_conf')

	if exclude_conf:
		exclude += get_excluded(exclude_conf)

	fbe = dict()
	empty_str = ''

	def exclude_full_path_root(l, root, exclude):
		root_slash = root + '/'

		_l = remove_excluded(
			(path_join(root, e) for e in l), 
			exclude
		)

		return [ re_sub(root_slash, empty_str, e) for e in _l ]

	for root, dirs, files in os.walk(directory, topdown=True):
		dirs[:] = exclude_full_path_root(dirs, root, exclude)
		files = exclude_full_path_root(files, root, exclude)

		for filename in files:
			ext = splitext(filename)[1][1:]
			_t = ( root, filename )

			dict_list_append(fbe, ext, _t)

	return fbe