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


def ask_if_needed(string, regexp, clean_variable=lambda s: s):
	matches = re_findall(regexp, string)

	if not matches:
		return string

	bars = ( ( match, clean_variable(match) ) for match in set(matches) )
	enter_bar_format = 'Enter {bar}: '.format

	for match, bar in bars:
		val = input(enter_bar_format(bar=bar))

		string = string.replace(match, val)

	return string