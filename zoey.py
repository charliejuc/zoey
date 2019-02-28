#!/usr/bin/env python

from lib.lcopy import zcopy
import argparse, sys, settings

def show_parser_help(parser):
	parser.print_help()
	sys.exit()

help_choices = ['-h', '--help']
def show_parser_help_if_needed(parser, help_index):
	try:
		if sys.argv[help_index] in help_choices:
			show_parser_help(parent_parser)

	except IndexError:
		pass

parent_parser = argparse.ArgumentParser(
	description='Help with common project tasks', 
	add_help=False
)
parent_parser.add_argument(
	'task',
	type=str, 
	choices=settings.allowed_tasks, 
	help='Select task to do'
)

help_index = 1
show_parser_help_if_needed(parent_parser, help_index)

args = parent_parser.parse_known_args()[0]

if args.task == 'cp':
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


# from pprint import pprint
# import os, json

# with open('zoey.json', 'w') as file:
# 	file.write(json.dumps(fbe))

# file_path = os.path.join(cache['json'][1][0], cache['json'][1][1])

# with open(file_path, 'rb') as f:
# 	package_json = json.load(f)

# 	pprint(package_json)