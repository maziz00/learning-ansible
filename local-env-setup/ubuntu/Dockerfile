FROM ubuntu:20.04

# Install Packages
RUN apt-get update && apt-get install -y openssh-server curl vim && \
    mkdir /var/run/sshd /home/ansible && \
    useradd -r -s /bin/bash -d /home/ansible ansible && \
    echo 'root:Passw0rd' | chpasswd && \
    echo 'ansible:Passw0rd' |  chpasswd && \
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

# Copy custom  ssh config
COPY sshd_config  /etc/ssh/

# SSH port
EXPOSE 22

# Start ssh service
CMD ["/usr/sbin/sshd", "-D"]