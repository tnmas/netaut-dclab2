from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure, napalm_get
import logging

from nornir_utils.plugins.functions.print_result import print_result

int_access = [
  {
    "id": "1",
    "name": "GigabitEthernet0/3",
    "mode": "access",
    "vlan": "4",
    "hostname": "172.16.0.13"
  },
  {
    "id": "2",
    "name": "GigabitEthernet1/0",
    "mode": "access",
    "vlan": "5",
    "hostname": "172.16.0.14"
  }
]

def build_config(task):
    all_interfaces = task.run(task=napalm_get, getters=["interfaces"])

    r = task.run(task=template_file,
                name="New Configuration.....",
                template="vlans.j2",
                path=f"templates",
                interfaces=all_interfaces,
                host_name=task.host.hostname,
                int_access=int_access
                )

    cmds = r.result
    print(r.interfaces)
    print(cmds)

    task.host['nconfig'] = r.result

    task.run(task=napalm_configure,
            name="Getting Running Config.....",
            replace=True,
            configuration=task.host['nconfig'],
            severity_level=logging.INFO
            )
