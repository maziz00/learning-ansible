import subprocess

def pull_and_run_containers(image_name, tag, base_name="ssh-srv"):
  """
  Pulls a Docker image, tags it, runs 3 detached containers, and cleans up.

  Args:
    image_name: The name of the Docker image to pull.
    tag: The new tag to assign to the image.
  """
  # Pull the image
  subprocess.run(["docker", "pull", image_name])

  # Tag the image
  subprocess.run(["docker", "tag", image_name, f"{tag}"])

  # Run 3 detached containers from the tagged image with unique names
  for i in range(3):
    container_name = f"{base_name}-{i+1}"  # Add incrementing number for uniqueness
    subprocess.run(["docker", "run", "-d", "--name", container_name, f"{tag}"])

  # Get container IDs
  # containers = subprocess.run(["docker", "ps", "-aq"], capture_output=True).stdout.decode().strip().splitlines()


if __name__ == "__main__":
  # Replace 'your_image_name' and 'your_tag' with actual values
  image_name = "mohaziz00/ssh-srv:v0.1"
  tag = "ssh-srv"
  pull_and_run_containers(image_name, tag)
  print(f"Successfully pulled, tagged as '{tag}', ran 3 containers from {image_name}")
