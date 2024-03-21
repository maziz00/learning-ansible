FROM ubuntu:20.04

RUN --mount=type=secret,id=cred_secret

# Install Packages
RUN apt-get update && apt-get install -y openssh-server curl vim && \
    mkdir /var/run/sshd /home/ansible && \
    useradd -r -s /bin/bash -d /home/ansible ansible && \
    echo "root:cred_secret" | chpasswd && \
    echo "ansible:cred_secret" |  chpasswd && \
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak && \
    echo cred_secret "cred_secret"

# Copy custom  ssh config
COPY sshd_config  /etc/ssh/

# SSH port
EXPOSE 22

# Start ssh service
CMD ["/usr/sbin/sshd", "-D"]