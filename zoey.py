#!/usr/bin/env python

from lib.lcopy import zcopy
import sys

from_path = '/egg_web'
new_path = './project'

custom_exclude = [ 
	r'.*/checksum_package\.txt$',
	r'.*/postgresql.*'
]

zcopy(from_path, new_path, exclude=custom_exclude, exclude_conf='node:webpack:nyc')

sys.exit()

# from pprint import pprint
# import os, json

# with open('zoey.json', 'w') as file:
# 	file.write(json.dumps(fbe))

# file_path = os.path.join(cache['json'][1][0], cache['json'][1][1])

# with open(file_path, 'rb') as f:
# 	package_json = json.load(f)

# 	pprint(package_json)