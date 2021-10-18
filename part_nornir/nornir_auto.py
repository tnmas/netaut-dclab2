from nornir import InitNornir
from nornir.plugins.functions import print_title, print_result
#Import Tasks from parse.py & new_configs.py
from parse import get_config, parse_config


nr = InitNornir(config_file="config.yaml")
switches = nr.filter(role="switch")

username = input("Enter Username: ")
password = input("Enter Password: ")
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

config = switches.run(name="Get Configurations",task=get_config)
print_title(config)

parsed = switches.run(name="Parse Configurations", task=parse_config)
print_title(parsed)
print_result(parsed)
