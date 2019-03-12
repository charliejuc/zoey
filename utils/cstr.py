import re

re_sub = re.sub


def str_to_raw(string):
	return re_sub(r"(^'|'$)", r'', '%r' % string)


def str_equals_to_dict(env):
	equal = '='
	env_split = ( e.split(equal, 1) for e in env )

	return { key: value for key, value in env_split }