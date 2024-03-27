#!/bin/bash
# Script to run ansible commands

# ansible-playbook playbook-debug.yml

ansible-playbook -i "localhost" playbook-*.yml

ansible-playbook playbook.yml -i inventory
