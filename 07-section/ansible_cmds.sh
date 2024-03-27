#!/bin/bash
# Script to run ansible commands

# ansible-playbook playbook-debug.yml

ansible-playbook -i "localhost" playbook-debug.yml

ansible-playbook -i "localhost" playbook-random.yml

ansible-playbook playbook.yml -i inventory
