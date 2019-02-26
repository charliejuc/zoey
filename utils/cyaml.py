import yaml

with open('/egg_web/docker-compose.yml', 'rb') as file:
	print(yaml.load(file))