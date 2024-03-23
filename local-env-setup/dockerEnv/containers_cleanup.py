import subprocess

def get_and_remove_containers(base_name="ssh-srv"):
  """
  Retrieves container IDs based on the base name and stops/removes them.

  Args:
    base_name: The base name for container names (default: "ssh-srv").
  """
  # Get container IDs using docker ps filtering and capture output
  command = ["docker", "ps", "-aqf", f"name={base_name}*-*"]
  output = subprocess.run(command, capture_output=True).stdout.decode().strip()

  # Split output into lines (container IDs)
  container_ids = output.splitlines() if output else []

  # Stop and remove containers if any found
  if container_ids:
    print(f"Stopping and removing containers based on '{base_name}':")
    for container_id in container_ids:
      subprocess.run(["docker", "stop", container_id])
      subprocess.run(["docker", "rm", "-f", container_id])
      print(f"Removed container: {container_id}")
  else:
    print(f"No containers found with the base name '{base_name}'.")

if __name__ == "__main__":
  # Replace 'your_base_name' with the actual base name for your containers
  base_name = "ssh-srv"
  get_and_remove_containers(base_name)
