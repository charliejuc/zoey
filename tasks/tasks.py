from lib.lcopy import zcopy
from lib.lhelp import zhelp
from lib.lcommand import zcommands

from utils.cfiles import full_dir

import sys, argparse, settings

def copy(parent_parser):
	#implements cp one file
	cp_parser = argparse.ArgumentParser('cp', parents=[parent_parser])
	cp_parser.add_argument('from_path', type=str, help='Project folder to copy')
	cp_parser.add_argument('to_path', type=str, help='New project folder')
	cp_parser.add_argument(
		'-excnf', '--exclude-conf', 
		type=str,
		default='node',
		help='Exclude files and folders with existing config separated by ":" options: {{{choices}}}'\
				.format(choices=','.join(key for key in settings.excluded.keys()))
	)

	args = cp_parser.parse_args()

	from_path = args.from_path
	new_path = args.to_path

	zcopy(
		from_path,
		new_path,
		exclude_conf=args.exclude_conf
	)

def command(parent_parser):
	c_parser = argparse.ArgumentParser('commands', parents=[parent_parser])

	c_parser.add_argument(
		'command_name', 
		type=str,
		help='Command to run'
	)
	c_parser.add_argument(
		'--project-dir', 
		type=str,
		help='Project folder', 
		default=full_dir('.')
	)

	args = c_parser.parse_args()

	zcommands(args.command_name, args.project_dir)

# def _help(parent_parser):
# 	h_parser = argparse.ArgumentParser('help', parents=[parent_parser])
# 	h_parser.add_argument(
# 		'-pd', '--project-dir', 
# 		type=str, 
# 		help='Project folder', 
# 		default=full_dir('.')
# 	)
# 	h_parser.add_argument(
# 		'-c', '--create', 
# 		action='store_true',
# 		help='Create help file from your source file'
# 	)
# 	h_parser.add_argument(
# 		'--src-file', '--source-file',
# 		type=str,
# 		help='Source file to create help file'
# 	)
# 	args = h_parser.parse_args()

# 	src_file = args.src_file

# 	if args.create and not src_file:
# 		print('[ERR] Source file is required', file=sys.stderr) #create function on util
# 		h_parser.print_help()
# 		sys.exit(1)

# 	print(src_file)
# 	sys.exit()

# 	zhelp(args.project_dir, create=args.create)

task_funcs = {
	'cp': copy,
	'command': command
}
def get_task(name):
	return task_funcs[name]