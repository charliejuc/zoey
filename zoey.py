#!/usr/bin/env python3.7
from tasks.tasks import get_task

import argparse, sys, settings

def show_parser_help(parser):
	parser.print_help()
	sys.exit()

help_choices = ['-h', '--help']
def show_parser_help_if_needed(parser, help_index):
	try:
		if sys.argv[help_index] in help_choices:
			show_parser_help(parser)

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

task = get_task(args.task)

task(parent_parser)
