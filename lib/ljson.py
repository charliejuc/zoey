from utils.cjson import write_json_file, read_json_file
import settings, json, sys, os

path_join = os.path.join

zoey_json_data = None

def write_zoey_json_file(to_dir, data):
	global zoey_json_data
	zoey_json_data = data

	write_json_file(
		path_join(to_dir, settings.json_conf_file), 
		data, 
		json_dumps={ 
			'indent': 4
		}
	)

def read_zoey_json_file(to_dir, force=False):
	global zoey_json_data

	if not force and zoey_json_data is not None:
		return zoey_json_data

	json_conf_file = path_join(to_dir, settings.json_conf_file)

	try:
		zoey_json_data = read_json_file(json_conf_file)

	except json.decoder.JSONDecodeError as e:
		if os.stat(json_conf_file).st_size != 0:
			raise e

		print('[JSONDecodeError read_zoey_json_file]', e, file=sys.stderr)
		zoey_json_data = {}

	except FileNotFoundError:
		zoey_json_data = {}

	return zoey_json_data