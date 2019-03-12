# from lib.ljson import write_zoey_json_file, read_zoey_json_file
# from lib.lfiles import get_files_by_ext

from pprint import pprint
from utils.ctime import speed_test

import os, sys

project_dir = '/var/www/html/clients/example_web'
file_path = os.path.join(project_dir, 'docker-compose.yml')

# print(dir(yaml))

from utils.cstr import str_equals_to_dict
from utils.cdict import dict_to_str_equals, include_update
from lib.lyaml import read_docker_compose_file, write_docker_compose_file, update_docker_compose_file


update_docker_compose_file(file_path, {
	'services': {
		'postgresql': {
			'environment': {
				'USER': 'UnNota',
				'PASS': 'CCCCCCCCCCCCCCCCCC'
			}
		}
	}
})

# with open(file_path, 'r') as file:
# 	data = yaml.load(file)
# 	pg_env = str_equals_to_dict(data['services']['postgresql']['environment'])

# 	print(pg_env)

# 	pg_env['PASS'] = '1sdafjLJlsjdlfaslkdsKJlkadsf7281'

# 	pg_env = dict_to_str_equals(pg_env)

# 	data['services']['postgresql']['environment'] = pg_env


# with open(file_path, 'w') as file:
# 	file.write(yaml.dump(data))

# import shlex
# from lib.lcommand import zcmd_func


# func_cmd = """update_json_file('node/app/project-conf/conf.json', '{
# 	"database": { "database": "example", "username": "cacatua1" }
# }');"""


# zcmd_func(func_cmd, project_dir)