# from lib.ljson import write_zoey_json_file, read_zoey_json_file
# from lib.lfiles import get_files_by_ext

from pprint import pprint
from utils.ctime import speed_test

# import shlex
from lib.lcommand import zcmd_func


func_cmd = """update_json_file('node/app/project-conf/conf.json', '{
	"database": { "database": "example", "username": "cacatua1" }
}');"""


zcmd_func(func_cmd, '/var/www/html/clients/example_web')