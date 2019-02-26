import re

re_search = re.search

def re_search_list(patterns, string, *args, **kwargs):
	for pattern in patterns:
		if re_search(pattern, string):
			yield True
			break

		yield False

def remove_excluded(l, excluded, iterable=True):
	if iterable:
		return ( e for e in l if not any(re_search_list(excluded, e)) )

	return [ e for e in l if not any(re_search_list(excluded, e)) ]