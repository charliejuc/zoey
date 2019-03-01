from utils.cfiles import write_file, read_file

import json

def write_json_file(file_path, _dict, *args, **kwargs):
	json_dumps = kwargs.pop('json_dumps', {})

	write_file(
		file_path,
		json.dumps(_dict, **json_dumps), 
		*args, **kwargs
	)

def read_json_file(file_path, *args, **kwargs):
	return json.loads(
		read_file(
			file_path,
			*args, **kwargs
		)
	)