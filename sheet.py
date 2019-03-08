# from lib.ljson import write_zoey_json_file, read_zoey_json_file
# from lib.lfiles import get_files_by_ext

from pprint import pprint
from utils.ctime import speed_test

# import shlex
from utils.cos import run_cmd



pprint(run_cmd('ls', stdout=None))


# print(cmd_ask_if_needed("docker-compose exec postgresql bash -c \"su postgres -c 'createdb <{?db_name}>'\""))