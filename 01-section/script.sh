#!/bin/bash
# Script to run ansible commands

# ping command
ansible target* -m ping -i inventory.txt