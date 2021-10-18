from nornir import InitNornir
from nornir_utils.plugins.functions import print_title, print_result
from parse import get_config, parse_config
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_netmiko.tasks import netmiko_send_command


nr = InitNornir(config_file="config.yaml", dry_run=True)

result = nr.run( netmiko_send_command ,command_strings="show running-config")

