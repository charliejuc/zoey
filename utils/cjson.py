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


def update_json_file(file_path, updated_data, *args, **kwargs):
	json_file = read_json_file(file_path, *args, **kwargs)

	def add_data(json_file, key, data):
		option = {
			isinstance(json_file[key], dict): lambda: json_file[key].update(data),
			isinstance(json_file[key], list): lambda: json_file[key].append(data)
		}[True]

		if option:
			return option()

		json_file[key] = data


	for key, data in updated_data.items():
		try:
			add_data(json_file, key, data)

		except KeyError:
			json_file[key] = {}
			add_data(json_file, key, data)

	write_json_file(file_path, json_file, json_dumps={ 'indent': 4 }, *args, **kwargs)