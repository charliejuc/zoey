import re

re_sub = re.sub

def str_to_raw(string):
	return re_sub(r"(^'|'$)", r'', '%r' % string)