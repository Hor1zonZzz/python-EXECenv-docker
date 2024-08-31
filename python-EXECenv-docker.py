import docker
import os 

# Get current script absloute path
current_directory = os.path.abspath(os.path.dirname(__file__))

# Connect to Docker daemon
client = docker.DockerClient(base_url='npipe:////./pipe/docker_engine')

try:
    # Create and start the container
    container = client.containers.run(
        image="python:3.11-slim",
        name="my-python-exec-env",
        volumes={
            current_directory: {'bind': '/app', 'mode': 'ro'} # Mount local files to the app directory of the container.
        },
        command='ls /app',
        detach=True
    )

    # Wait for the container to finish and retrieve logs
    container.wait()
    result = container.logs()

    # Print the logs
    print(result.decode('utf-8'))


finally:
    # Clean up the container
    container.remove(v=True, force=True)

