from nornir import InitNornir
from nornir_utils.plugins.functions import print_title, print_result
from parse import get_config, parse_config
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_netmiko.tasks import netmiko_send_command

from nornir.core.plugins.connections import ConnectionPluginRegister
import nornir_napalm.plugins.connections as napalm
import nornir_netmiko.connections as netmiko
from napalm.ios import IOSDriver

ConnectionPluginRegister.register(napalm.CONNECTION_NAME, napalm.Napalm)
ConnectionPluginRegister.register(netmiko.CONNECTION_NAME, netmiko.Netmiko)
ConnectionPluginRegister.available


nr = InitNornir(config_file="config.yml", dry_run=True)
#switches = nr.filter(role="switch")

#my_hosts = nr.inventory.hosts
#host_keys = list(my_hosts.keys())
result = nr.run(napalm_cli ,commands=["show running-config"])

print_result(result)
#config = switches.run(name="Get Configurations",task=get_config)
#print_title(config)

#parsed = switches.run(name="Parse Configurations", task=parse_config)
#print_title(parsed)
#print_result(parsed)
