import subprocess

def run_containers(image_name, tag, base_name="ssh-srv"):
  """
  Pulls a Docker image, tags it, and runs 3 detached containers with names.

  Args:
    image_name: The name of the Docker image to pull.
    tag: The new tag to assign to the image.
    base_name: The base name for container names (default: "ssh-srv").
  """
  # Pull the image
  subprocess.run(["docker", "pull", image_name])

  # Tag the image
  subprocess.run(["docker", "tag", image_name, f"{tag}"])

  # Run 3 detached containers from the tagged image with unique names
  for i in range(3):
    container_name = f"{base_name}-{i+1}"  # Add incrementing number for uniqueness
    subprocess.run(["docker", "run", "-d", "--name", container_name, f"{tag}"])

  print(f"Successfully pulled, tagged as '{tag}', and ran 3 containers from {image_name}")

if __name__ == "__main__":

  image_name = "mohaziz00/ubuntu-srv:v0.2"
  tag = "ssh-srv"
  run_containers(image_name, tag)

