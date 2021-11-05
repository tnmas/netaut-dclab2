from nornir import InitNornir
from nornir_utils.plugins.functions import print_title, print_result
from parse import parse_config
from new_configs import build_config
from nornir.core.plugins.connections import ConnectionPluginRegister
import nornir_napalm.plugins.connections as napalm
import nornir_netmiko.connections as netmiko

ConnectionPluginRegister.register(napalm.CONNECTION_NAME, napalm.Napalm)
ConnectionPluginRegister.register(netmiko.CONNECTION_NAME, netmiko.Netmiko)
ConnectionPluginRegister.available

nr = InitNornir(config_file="config.yml")

parsed = nr.run(name="Parsed Configs.....", task=parse_config)
print_title(parsed)
print_result(parsed)

new_config = nr.run(name="New Configs.....", task=build_config)
print_result(new_config)

