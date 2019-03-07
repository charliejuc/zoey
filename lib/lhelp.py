from lib.ljson import read_zoey_json_file

from utils.cos import zmakedirs

import os, sys

path_join = os.path.join

zoey_folder = '.zoey' #take to settings
help_folder = os.path.join(zoey_folder, 'help')

def zhelp_create(project_dir):
	zf_path = path_join(project_dir, help_folder)

	zmakedirs(zf_path)

def zhelp(project_dir, create):
	if create:
		zhelp_create(project_dir)

	json_file = read_zoey_json_file(project_dir)
	help_list = json_file.get('help', list())

	if not help_list:
		print('There are no help files')
		sys.exit(0)