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


def dict_to_str_equals(_dict):
	equal_format = '{key}={value}'.format

	return [ equal_format(key=key, value=value) for key, value in _dict.items() ]


# Include values from updated_data keeping actual values
# Example:
# a = {
# 	'a': {
# 		'b': 2,
# 		'w': 3,
# 		'j': [ 3,4,5,6 ],
# 		'r': {
# 			100: 2,
# 			50: 30
# 		}
# 	},
# 	'z': 5
# }

# b = {
# 	'a': {
# 		'w': 7,
# 		'j': [ 100 ],
# 		'r': {
# 			100: 13
# 		}
# 	},
# }

# include_update(a, b)

# >>> {
# 		'a': {
#			'b': 2, 
#			'w': 7,
#			'j': [3, 4, 5, 6, 100], 
#			'r': {50: 30, 100: 13}
# 		}, 
# 		'z': 5
# 	  }
def include_update(_dict, updated_data):
	def add_data(_dict, key, data):
		if isinstance(_dict[key], list): 
			_dict[key] += data
			return

		_dict[key] = data

	def update(_dict, key, element):
		if isinstance(element, dict):
			include_update(_dict[key], element)
			return

		add_data(_dict, key, element)

	for key, data in updated_data.items():
		try:
			update(_dict, key, data)

		except KeyError:
			_dict[key] = type(data)()
			update(_dict, key, data)