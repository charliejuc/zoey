def dict_list_append(d, key, to_append):
	try:
		d[key].append(to_append)
	
	except KeyError as e:
		d[key] = list()
		d[key].append(to_append)


def get_joined_dict_lists(_dict, key, sep, unique=True):
	try:
		return _dict[key]

	except KeyError:
		excluded = list()

		keys = key.split(sep)

		if unique:
			keys = set(keys)

		for key in keys:
			excluded += _dict[key]

		return excluded