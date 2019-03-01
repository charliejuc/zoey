from lib.lcopy import zcopy

import argparse, settings

def copy(parent_parser):
	#implements cp one file
	cp_parser = argparse.ArgumentParser('cp', parents=[parent_parser])
	cp_parser.add_argument('from_path', type=str, help='Project folder to copy')
	cp_parser.add_argument('to_path', type=str, help='New project folder')
	cp_parser.add_argument(
		'--exclude-conf', 
		type=str,
		default='node',
		help='Exclude files and folders with existing config separated by ":" options: {{{choices}}}'\
				.format(choices=','.join(key for key in settings.excluded.keys()))
	)

	args = cp_parser.parse_args()

	from_path = args.from_path
	new_path = args.to_path

	custom_exclude = [
		r'.*/checksum_package\.txt$',
		r'.*/postgresql.*'
	]

	zcopy(
		from_path,
		new_path,
		exclude=custom_exclude,
		exclude_conf=args.exclude_conf
	)

task_funcs = {
	'cp': copy
}
def get_task(name):
	return task_funcs[name]