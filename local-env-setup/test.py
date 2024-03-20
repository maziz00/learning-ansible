import docker

client = docker.from_env()
containers = client.containers.list()

running_containers_id = [container.id for container in containers if 'ssh-srv-' in container.name and container.status == 'running']

print(running_containers_id)
