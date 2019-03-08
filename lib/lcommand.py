from lib.ljson import read_zoey_json_file

from utils.cos import run_cmd
from utils.cre import ask_if_needed

import sys, re

re_sub = re.sub

clean_cmd_var_regexp = r'(<\{\?|\}>)'
def clean_cmd_variable(string):
	return re_sub(clean_cmd_var_regexp, '', string)


ask_variable_regexp = r'<\{\?[a-zA-Z0-9_]+\}>'
def zcmd(cmd, directory, need_pipe=False):
	parsed_cmd = ask_if_needed(
		cmd,
		ask_variable_regexp,
		clean_variable=clean_cmd_variable
	)

	if not need_pipe:
		_kwargs = { 'stdout': None }

	run_cmd(parsed_cmd, **_kwargs)


from utils.cjson import update_json_file
import json

allowed_funcs = {
	'update_json_file': (update_json_file, ( str, json.loads ))
}
def zcmd_func(funcs, directory, need_pipe=False):
	def get_func_name(func):
		return re.search(r'^[a-zA-Z_]+', func).group()

	def get_func_args(func):
		args = re.findall(r'\((.*)', func, flags=re.DOTALL)[0]

		return [ arg for arg in args.split(', ') ]

	parsed_funcs = ask_if_needed(
		funcs,
		ask_variable_regexp,
		clean_variable=clean_cmd_variable
	)

	print(parsed_funcs)

	parsed_funcs = ( pf.strip() for pf in parsed_funcs.split(');') if pf )

	for pf in parsed_funcs:
		af = allowed_funcs[get_func_name(pf)]
		func = af[0]
		args_parsers = af[1]
		args = get_func_args(pf)

		for i, parser in enumerate(args_parsers):
			args[i] = parser(args[i])

		func(*args)


def run_zcmd(cmd_obj, directory):
	need_pipe = cmd_obj.get('pipe', False)
	print(cmd_obj.get('info', ''))
	cmd = cmd_obj.get('cmd')
	func_cmd = cmd_obj.get('func_cmd')

	if cmd is None and func_cmd is None:
		raise Exception('"cmd" or "func_cmd" is required.')

	if cmd:
		return zcmd(cmd, directory, need_pipe=need_pipe)

	zcmd_func(func_cmd, directory, need_pipe=need_pipe)


def zcommands(command_name, directory):
	json_file = read_zoey_json_file(directory)
	commands = json_file.get('commands', dict())

	if not commands:
		print('There are no commands')
		sys.exit(0)

	for cmd in commands[command_name]:
		run_zcmd(cmd, directory)