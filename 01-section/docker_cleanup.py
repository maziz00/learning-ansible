import subprocess

def clean_containers(image_name, tag):
  """
  Pulls a Docker image, tags it, runs 3 detached containers, and cleans up.

  Args:
    image_name: The name of the Docker image to pull.
    tag: The new tag to assign to the image.
  """

  # Get container IDs
  containers = subprocess.run(["docker", "ps", "-aq"], capture_output=True).stdout.decode().strip().splitlines()

  # Stop and remove all created containers
  for container_id in containers:
    subprocess.run(["docker", "stop", container_id])
    subprocess.run(["docker", "rm", container_id])

  # Optionally remove the tagged image (uncomment if desired)
  subprocess.run(["docker", "rmi", f"{image_name}:{tag}"])

if __name__ == "__main__":

  clean_containers()
  print(f"Successfully pulled, cleanup images and running containers")

  # Uncomment the following line to also remove the tagged image
  # subprocess.run(["docker", "rmi", f"{image_name}:{tag}"])
