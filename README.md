# ZOEY
## Copy
It allows copy old project excluding unnecesary files or folders.

### Usage
```bash
./zoey.py cp [-h] [-excnf EXCLUDE_CONF] from_path to_path
```

#### Exclude conf
```bash
--exclude-conf -excnf
```
This configuration use values from **excluded** variable in settings.py.

```python
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
```

**Example:**
```bash
./zoey.py cp --exclude-conf node:webpack ./old_project ./new_project
```

With this command we don't copy files or folders that match these regexp:

```python
[
	r'.*/node_modules',
	r'.*/\.git',
	r'.*/dist'
]
```

We can also create **zoey.json** file in the directory folder of the old project and include `--exclude-conf` configuration without having to type the command each time.

**zoey.json file:**
```json
{
    "exclude_conf": "node:webpack"
}
```

And type your custom regexp to exclude.
```json
{
    "exclude": [
        ".*/checksum_package\\.txt$",
        ".*/package-lock\\.json$",
        ".*/postgresql.*"
    ],
    "exclude_conf": "node:webpack"
}
```

## Commands
Run bash or zoey commands to set up your project.

### Usage
```bash
./zoey.py command [-h] [--project-dir PROJECT_DIR] command_name
```

#### Command variables
When type a command you can use variables for zoey ask for values, variables looks like this **"<{?variable_name}>"**, for example: "<{?db_name}>". Zoey has a **variable cache** and when you type the same variable name several times, use cache value, whether no value is provided, by default.

#### Add custom commands
**zoey.json:**
```json
{
    "commands": {
    	"start": [
    		{
    			"cmd": "docker-compose build",
    			"info": "Build containers"
    		},
    		{
				"func_cmd": "update_json_file('node/app/project-conf/conf.json', '{ \"database\": { \"database\": \"<{?db_name}>\" } }');",
				"info": "Set 'node/app/project-conf/conf.json' config"
			},
    		{
    			"cmd": "docker-compose up -d",
    			"info": "Run containers"
    		},
    		{
    			"cmd": "docker-compose exec postgresql bash -c \"su postgres -c 'createdb <{?db_name}>'\"",
    			"info": "Create postgresql database"
    		},
    		{
    			"cmd": "docker-compose down",
    			"info": "Down containers"
    		}
    	]
    }
}

```

##### CMD
Allows run bash scripts.

```json
{
	"cmd": "docker-compose build",
	"info": "Build containers"
}
```

##### FUNCTION CMD
Allows run zoey functions. Always wrap function arguments with single quotes.

```json
{
	"func_cmd": "update_json_file('node/app/project-conf/conf.json', '{ \"database\": { \"database\": \"<{?db_name}>\" } }');",
	"info": "Set 'node/app/project-conf/conf.json' config"
}
```

##### ZOEY FUNCTIONS

- **update_json_file(file_path, json_data):** Update json file with passed values, this function only includes new values or update indicated values, it never removes existing values.
- **update_yaml_file(file_path, json_data):** The same as **update_json_file** but for **yaml** files.
- **update_dc_file(file_path, json_data):** The same as **update_yaml_file** but for **docker-compose.yml** files. Avoid having to write **"services"** in json_data.
