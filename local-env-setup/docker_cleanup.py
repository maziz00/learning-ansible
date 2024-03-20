import subprocess

def cleanup_containers(base_name="ssh-srv"):
  """
  Stops and removes all containers with names starting with the provided base name.

  Args:
    base_name: The base name for container names (default: "ssh-srv").
  """
  # Get container IDs (using container names)
  containers = subprocess.run(["docker", "ps", "-aqf", "name={base_name}"r'\*'], capture_output=True).stdout.decode().strip().splitlines()

  # Stop and remove all created containers
  for container_id in containers:
    subprocess.run(["echo", container_id])
    subprocess.run(["docker", "stop", container_id])
    subprocess.run(["docker", "rm", "f", container_id])

  print(f"Stopped and removed all containers starting with '{base_name}'")

  # Optionally remove the tagged image (uncomment if desired)
  subprocess.run(["docker", "rmi", f"{base_name}"])

if __name__ == "__main__":

  cleanup_containers()