#!/usr/bin/env python

from lib.lcopy import zcopy

import os, re

re_sub = re.sub

def str_to_raw(string):
	return re_sub(r"(^'|'$)", r'', '%r' % string)

from_path = '/egg_web'
new_path = './project'

custom_exclude = [ 
	r'.*/checksum_package\.txt$',
	r'.*/\.nyc',
	r'.*/dist',
	r'.*/coverage',
	r'.*/postgresql.*'
]

zcopy(from_path, new_path, exclude=custom_exclude)

# from pprint import pprint
# import json

# with open('zoey.json', 'w') as file:
# 	file.write(json.dumps(fbe))

# file_path = os.path.join(cache['json'][1][0], cache['json'][1][1])

# with open(file_path, 'rb') as f:
# 	package_json = json.load(f)

# 	pprint(package_json)