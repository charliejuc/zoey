from utils.cfiles import write_file, read_file
from utils.cdict import include_update

from collections import OrderedDict
import json

def write_json_file(file_path, _dict, *args, **kwargs):
	json_dumps = kwargs.pop('json_dumps', dict())

	write_file(
		file_path,
		json.dumps(_dict, **json_dumps), 
		*args, **kwargs
	)

def read_json_file(file_path, *args, **kwargs):
	json_loads = kwargs.pop('json_loads', dict())

	if json_loads.pop('ordered', False):
		json_loads['object_pairs_hook'] = OrderedDict

	return json.loads(
		read_file(
			file_path,
			*args, **kwargs
		),
		**json_loads
	)


def update_json_file(file_path, updated_data, *args, **kwargs):
	json_file = read_json_file(file_path, *args, **kwargs)

	include_update(json_file, updated_data)

	write_json_file(file_path, json_file, json_dumps={ 'indent': 4 }, *args, **kwargs)


def update_ordered_json_file(file_path, updated_data, *args, **kwargs):
	return update_json_file(file_path, updated_data, json_loads={ 'ordered': True }, *args, **kwargs)