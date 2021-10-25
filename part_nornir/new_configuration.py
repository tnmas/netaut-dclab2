from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
import logging


def build_config(task):
    r = task.run(task=template_file,
                name="New Configuration",
                template="vlans.j2",
                path=f"templates",
                access_ports=task.host['access_ports'] if task.host.hostname == '172.16.0.13' or task.host.hostname == '172.16.0.13' else "",
                trunk_ports=task.host['trunk_ports'],
                severity_level=logging.DEBUG
                )

    cmds = r.result
    print(cmds)

    task.host['nconfig'] = r.result

    task.run(task=netmiko_send_config,
            name="Loading Configuration on the switch",
            replace=False,
            config_commands=task.host['nconfig'],
            severity_level=logging.INFO
            )
