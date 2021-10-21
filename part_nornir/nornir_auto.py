from nornir import InitNornir
from nornir_utils.plugins.functions import print_title, print_result
from parse import get_config, parse_config
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_netmiko.tasks import netmiko_send_command

from nornir.core.plugins.connections import ConnectionPluginRegister
import nornir_napalm.plugins.connections as napalm
import nornir_netmiko.connections as netmiko

ConnectionPluginRegister.register(napalm.CONNECTION_NAME, napalm.Napalm)
ConnectionPluginRegister.register(netmiko.CONNECTION_NAME, netmiko.Netmiko)
ConnectionPluginRegister.available


nr = InitNornir(config_file="config.yml", dry_run=True)

result = nr.run(napalm_cli ,commands=["show ip interface brief"])

#print_result(result)

hosts = nr.inventory.hosts

for host in hosts:
  res = host.run(napalm_cli ,commands=["show ip interface brief"])
  print_result(res)

