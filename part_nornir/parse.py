from nornir import InitNornir
from ttp import ttp
from nornir_napalm.plugins.tasks import napalm_get


def parse_interfaces(config):
    parser = ttp(data=config, template='ttp/interfaces.j2')
    parser.parse()
    interfaces = parser.result()[0][0]
    return interfaces

def parse_config(task):
    print('Parsing config for ' + task.host.hostname)

    task.host['interfaces'] = [interface for interface in parse_interfaces(task.host['config'])
                             if 'mode' in interface.keys()]
    task.host['access_ports'] = [interface for interface in task.host['interfaces']
                                      if interface['mode'] == 'access'
                                      and 'access_vlan' in interface.keys()]
    task.host['trunk_ports'] = [interface for interface in task.host['interfaces']
                                     if interface['mode'] == 'trunk'
                                     and 'native_vlan' in interface.keys()]


def get_config(task):
    r = task.run(
        task=napalm_get,
        getters="config",
        retrieve="all"
    )
    task.host['config'] = r.result['config']['running']    