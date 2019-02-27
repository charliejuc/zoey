def dict_list_append(d, key, to_append):
	try:
		d[key].append(to_append)
	
	except KeyError as e:
		d[key] = list()
		d[key].append(to_append)


def get_joined_dict_lists(_dict, key, sep):
	try:
		return _dict[key]

	except KeyError:
		excluded = list()

		for key in key.split(sep):
			excluded += _dict[key]

		return excluded