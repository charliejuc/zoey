from utils.cdict import get_joined_dict_lists

import settings

s_excluded = settings.excluded
excluded_sep = ':'

def get_excluded(key):
	return get_joined_dict_lists(s_excluded, key, excluded_sep)