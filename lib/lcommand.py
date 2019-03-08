from lib.ljson import read_zoey_json_file

from utils.cos import run_cmd
from utils.cre import ask_if_needed

import sys, re

re_sub = re.sub

clean_cmd_var_regexp = r'(<\{\?|\}>)'
def clean_cmd_variable(string):
	return re_sub(clean_cmd_var_regexp, '', string)


def run_zcmd(cmd_obj):
	need_pipe = cmd_obj.get('pipe', False)

	print(cmd_obj.get('info', ''))
	parsed_cmd = ask_if_needed(cmd_obj['cmd'], ask_variable_regexp, clean_variable=clean_cmd_variable)

	if not need_pipe:
		_kwargs = { 'stdout': None }

	run_cmd(parsed_cmd, **_kwargs)


ask_variable_regexp = r'<\{\?[a-zA-Z0-9_]+\}>'
def zcommands(command_name, directory):
	json_file = read_zoey_json_file(directory)
	commands = json_file.get('commands', dict())

	if not commands:
		print('There are no commands')
		sys.exit(0)

	for cmd in commands[command_name]:
		run_zcmd(cmd)