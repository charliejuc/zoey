allowed_tasks = [ 
	'cp', 
	'help'
]
json_conf_file = 'zoey.json'

excluded = {
	'node': [ 
		r'.*/node_modules',
		r'.*/\.git'
	],
	'webpack': [ 
		r'.*/dist'
	],
	'nyc': [
		r'.*/\.nyc',
		r'.*/coverage'
	]
}