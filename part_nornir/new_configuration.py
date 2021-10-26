from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
import logging

int_access = [
  {
    "id": "1",
    "name": "GigabitEthernet0/3",
    "mode": "access",
    "vlan": "4"
  },
  {
    "id": "2",
    "name": "GigabitEthernet1/0",
    "mode": "access",
    "vlan": "5"
  }
]

def build_config(task):
    r = task.run(task=template_file,
                name="New Configuration",
                template="vlans.j2",
                path=f"templates",
                interfaces=task.host.interface,
                #access_ports=task.host['access_ports'] if task.host.hostname == '172.16.0.13' or task.host.hostname == '172.16.0.13' else "", 
                #trunk_ports=task.host['trunk_ports'],
                severity_level=logging.DEBUG,
                int_access=int_access
                )

    cmds = r.result
    #print(r.access_ports)
    print(task.host.interface)

    task.host['nconfig'] = r.result

    task.run(task=napalm_configure,
            name="Loading Configuration on the switch",
            replace=True,
            configuration=task.host['nconfig'],
            severity_level=logging.INFO
            )
