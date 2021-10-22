from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
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

    task.run(task=napalm_configure,
            name="Loading Configuration on the switch",
            replace=False,
            configuration=task.host['nconfig'],
            severity_level=logging.INFO
            )
