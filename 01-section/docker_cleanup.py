import subprocess

def clean_containers(base_name="ssh-srv"):
  """
  Cleans up all docker containers with a given base name.

  Args:
    base_name: for containers to be removed
  """

  # Get container IDs (using container names)
  containers = subprocess.run(["docker", "ps", "-aqf", "name={base_name}-\*"], capture_output=True).stdout.decode().strip().splitlines()

  # Stop and remove all created containers
  for container_id in containers:
    subprocess.run(["docker", "stop", container_id])
    subprocess.run(["docker", "rm", "-f", container_id])

  # Optionally remove the tagged image (uncomment if desired)
  subprocess.run(["docker", "rmi", f"{tag}"])

if __name__ == "__main__":
  tag = "ssh-srv"

  clean_containers()
  print(f"Successfully pulled, cleanup images and running containers")

