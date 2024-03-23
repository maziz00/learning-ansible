#!/bin/bash

# Install Python Pip and dependencies on Centos 7
sudo yum install -y epel-release python python-pip

sudo pip install flask flask-mysql
# with certification
sudo pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org flask flask-mysql

# Install MySQL Serve
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm

sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm

sudo yum update

sudo yum -y install mysql-server

sudo service mysql start