import re

re_search = re.search
re_findall = re.findall

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


ain_cache = {}
def ask_if_needed(string, regexp, clean_variable=lambda s: s):
	matches = re_findall(regexp, string)

	if not matches:
		return string

	bars = ( ( match, clean_variable(match) ) for match in set(matches) )
	enter_bar_str = 'Enter {bar}'
	enter_bar_format = (enter_bar_str + ': ').format
	enter_bar_default_format = (enter_bar_str + ' (default: {default}): ').format

	def _input(bar):
		cache_val = ain_cache.get(bar)
		question_str = enter_bar_default_format(bar=bar, default=cache_val) if cache_val else enter_bar_format(bar=bar)

		val = input(question_str)

		if not val and cache_val:
			return cache_val

		ain_cache[bar] = val
		return val

	for match, bar in bars:
		val = _input(bar)

		string = string.replace(match, val)

	return string