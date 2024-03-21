FROM centos:centos7.9.2009


# RUN --mount=type=secret,id=cred_secret && \
#     sed -i "s/CREDS=/CREDS=$(cat /run/secrets/cred_secret)/" .env.centos

# ARG name
# ENV pass $name

# Install Packages
RUN yum update -y && yum install -y openssh-server curl vim sudo epel-release && \
    mkdir /var/run/sshd mkdir /home/ansible && \
    useradd -r -s /bin/bash -d /home/ansible ansible && \
    echo "root:Passw0rd" | chpasswd && \
    echo "ansible:Passw0rd" |  chpasswd && \
    usermod -aG wheel ansible && \
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

# Copy custom  ssh config
COPY sshd_config  /etc/ssh/ 

# gen dummy keys, centos doesn't autogen them, & modify sshd_config
RUN /usr/bin/ssh-keygen -A && \
    sed -i 's/^Include/# Include/' /etc/ssh/sshd_config

#to pass environment variables when running a Dockerized SSHD service. 
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# SSH port
EXPOSE 22 3306

# Keep container running
ENTRYPOINT ["/usr/sbin/sshd","-eD"]