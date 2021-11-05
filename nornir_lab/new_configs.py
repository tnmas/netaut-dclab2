from nornir_netmiko import netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_get

int_access = {
  "GigabitEthernet0/3": {
    "mode": "access",
    "vlan": "4",
    "hostname": "172.16.0.13"
  },
  "GigabitEthernet1/0": {
    "mode": "access",
    "vlan": "5",
    "hostname": "172.16.0.14"
  }
}

def build_config(task):
    all_interfaces = task.run(task=napalm_get, getters=["interfaces"])
    interface_accessport=int_access

    r = task.run(task=template_file,
                name="New Configuration.....",
                template="vlans.j2",
                path=f"templates",
                all_interfaces=all_interfaces,
                host_name=task.host.hostname,
                interface_accessport=interface_accessport
                )

    task.host['nconfig'] = r.result

    task.run(task=netmiko_send_config,
            config_commands=task.host['nconfig'],
            name="Running new Config.....",
            cmd_verify=False            
            )
