## Getting Started

These instructions describe what you need, so that you will be able to run the automation scripts run in your machine.

## Part_1 => Ansible

### Prerequisites

Packages you need to install:-

Install python3 and ansible

```
sudo apt-get install python3
pip install ansible
```


### Command used to run the playbook

```
ansible-playbook -i inventory.ini --vault-id @prompt playbook.yml -K
vault.yml encryption password => 123abc
```

## Part_2 => Nornir

### Prerequisites

Packages you need to install:-

Install nornir using pip

```
pip install nornir
pip install nornir-napalm  // Napalm for the connections
pip install nornir-utils   // 
pip install nornir_ansible
pip install nornir-jinja2
pip install nornir-netmiko
```


### Command used to run the script

```
Here comes the way you run the script
```



## Author

Tsigereda Nebai Kidane

