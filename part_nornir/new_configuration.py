from nornir import InitNornir
from nornir.plugins.tasks import networking, text
import logging


def build_config(task):
    r = task.run(task=text.template_file,
                name="New Configuration",
                template="vlans.j2",
                path=f"templates",
                access_ports_4=task.host['access_ports_4'],
                access_ports_5=task.host['access_ports_5'],
                trunk_ports=task.host['trunk_ports'],
                severity_level=logging.DEBUG
                )

    cmds = r.result
    print(cmds)

    task.host['nconfig'] = r.result

    task.run(task=networking.napalm_configure,
            name="Loading Configuration on the switch",
            replace=False,
            configuration=task.host['nconfig'],
            severity_level=logging.INFO
            )