## Getting Started

These instructions you need to follow, so that you will be able to run the automation scripts in your machine.

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
cd '$FOLDER_LOCATION/ansible_lab/'
ansible-playbook playbook.yml -i inventory.yml
```

## Part_2 => Nornir

### Prerequisites

Packages you need to install:-

Install nornir using pip

```
pip install nornir
pip install nornir-napalm 
pip install nornir-utils   
pip install nornir_ansible
pip install nornir-jinja2
pip install nornir-netmiko
```


### Command used to run the script

```
cd '$FOLDER_LOCATION/nornir__lab/' 
python3 run_nornir.py
```



## Author

Tsigereda Nebai Kidane

