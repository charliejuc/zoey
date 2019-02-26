from lib.lfiles import get_files_by_ext

from utils.cos import zmakedirs

import os, re, shutil

path_join = os.path.join
re_sub = re.sub
shutil_copy = shutil.copy

def zcopy(from_path, new_path, *args, **kwargs):
	fbe = get_files_by_ext(from_path, *args, **kwargs)

	zmakedirs(new_path)

	for ext, files in fbe.items():
		for root, filename in files:
			new_root = re_sub(from_path, new_path, root)			

			zmakedirs(new_root)

			shutil_copy(
				path_join(root, filename),
				path_join(new_root, filename)
			)