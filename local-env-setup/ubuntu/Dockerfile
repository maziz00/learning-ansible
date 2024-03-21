FROM ubuntu:20.04

# RUN --mount=type=secret,id=cred_secret && \
#     sed -i "s/CREDS=/CREDS=$(cat /run/secrets/cred_secret)/" .env.ubuntu

# Install Packages
RUN apt-get update && apt-get install -y openssh-server curl vim && \
    mkdir /var/run/sshd /home/ansible && \
    useradd -r -s /bin/bash -d /home/ansible ansible && \
    echo "root:Passw0rd" | chpasswd && \
    echo "ansible:Passw0rd" |  chpasswd && \
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

# Copy custom  ssh config
COPY sshd_config  /etc/ssh/

# SSH port
EXPOSE 22 3306

# Start ssh service
CMD ["/usr/sbin/sshd", "-D"]