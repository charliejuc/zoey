from utils.cfiles import write_file, read_file
from utils.cdict import include_update

import oyaml as yaml


def write_yaml_file(file_path, _dict, *args, **kwargs):
	yaml_dump = kwargs.pop('yaml_dump', dict())

	write_file(
		file_path,
		yaml.dump(_dict, **yaml_dump),
		*args, **kwargs
	)


def read_yaml_file(file_path, *args, **kwargs):
	yaml_load = kwargs.pop('yaml_load', dict())

	return yaml.load(
		read_file(
			file_path,
			*args, **kwargs
		),
		**yaml_load
	)


def update_yaml_file(file_path, updated_data, *args, **kwargs):
	yaml_file = read_yaml_file(file_path, *args, **kwargs)

	include_update(yaml_file, updated_data)

	write_yaml_file(file_path, yaml_file, *args, **kwargs)