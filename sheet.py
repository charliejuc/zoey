from lib.ljson import write_zoey_json_file, read_zoey_json_file
from lib.lfiles import get_files_by_ext
from pprint import pprint
from utils.ctime import speed_test

folder = '/egg_web'

# write_zoey_json_file(folder, { 
# 	'exclude': [
# 		r'.*/checksum_package\.txt$',
# 		r'.*/postgresql.*'
# 	]
# })

# get_files_by_ext(folder)

# print(read_zoey_json_file(folder))