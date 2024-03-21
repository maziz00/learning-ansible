import subprocess

def get_container_ids(base_name="ssh-srv"):
  """
  Retrieves a list of container IDs based on the provided base name.

  Args:
    base_name: The base name for container names (default: "ssh-srv").

  Returns:
    A list of container IDs (strings) or an empty list if no containers match.
  """
  # Get container IDs using docker ps filtering and capture output
  command = ["docker", "ps", "-aqf", f"name={base_name}*-*"]
  output = subprocess.run(command, capture_output=True).stdout.decode().strip()

  # Split output into lines (container IDs)
  container_ids = output.splitlines() if output else []

  return container_ids

if __name__ == "__main__":
  # Replace 'your_base_name' with the actual base name for your containers
  base_name = "ssh-srv"
  container_ids = get_container_ids(base_name)

  if container_ids:
    print(f"Container IDs based on '{base_name}':")
    for container_id in container_ids:
      print(container_id)
  else:
    print(f"No containers found with the base name '{base_name}'.")
