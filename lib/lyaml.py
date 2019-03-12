from utils.cyaml import write_yaml_file, read_yaml_file
from utils.cstr import str_equals_to_dict
from utils.cdict import dict_to_str_equals, include_update


def write_docker_compose_file(file_path, _dict, *args, **kwargs):
	def dump(data):
		environment_key = 'environment'

		for _data, env, key in dc_data_item_key_iter(data):
			if key == environment_key:
				_data[key] = dict_to_str_equals(env)

		return data

	write_yaml_file(
		file_path,
		dump(_dict),
		*args, **kwargs
	)


def read_docker_compose_file(file_path, *args, **kwargs):
	def load(data):
		environment_key = 'environment'

		for _data, env, key in dc_data_item_key_iter(data):
			if key == environment_key:
				_data[key] = str_equals_to_dict(env)

		return data

	return load(
		read_yaml_file(
			file_path,
			*args, **kwargs
		)
	)


def update_docker_compose_file(file_path, updated_data, *args, **kwargs):
	yaml_file = read_docker_compose_file(file_path, *args, **kwargs)

	include_update(yaml_file, updated_data)

	write_docker_compose_file(file_path, yaml_file, *args, **kwargs)


def dc_data_item_key_iter(dc_data):
	services = dc_data.get('services')

	if services:
		environment_key = 'environment'

		for name, _data in services.items():
			environment = _data.get(environment_key)

			if environment:
				yield _data, environment, environment_key