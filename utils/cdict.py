def dict_list_append(d, key, to_append):
	try:
		d[key].append(to_append)
	
	except KeyError as e:
		d[key] = list()
		d[key].append(to_append)