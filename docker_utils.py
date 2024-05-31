import subprocess

def docker_login(username, password, url):
    login_command = ['docker', 'login', '--username', username, '--password-stdin', url]
    process = subprocess.Popen(login_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=password.encode())
    if process.returncode != 0:
        print(stderr.decode())
        raise RuntimeError('Failed to login to Docker registry.')

def pull_images(images, docker_repo, username, password):
    docker_login(username, password, docker_repo)
    if images:
        for image in images:
            # Split image name and tag if specified
            image_parts = image.split(':')
            if len(image_parts) > 1:
                image_name = image_parts[0]
                tag = image_parts[1]
            else:
                image_name = image
                tag = 'latest'  # Set tag to "latest" if not specified

            pull_command = f'docker pull {docker_repo}/{image_name}:{tag}'
            subprocess.run(pull_command, shell=True, check=True)
    else:
        print('Please specify image(s) via list or command line.')

def push_images(images, harbor_url, username, password):
    docker_login(username, password, harbor_url)
    if images:
        for image in images:
            # Split image name and tag if specified
            image_parts = image.split(':')
            if len(image_parts) > 1:
                image_name = image_parts[0]
                tag = image_parts[1]
            else:
                image_name = image
                tag = 'latest'  # Set tag to "latest" if not specified

            new_image = f'{harbor_url}/docker/{image_name}:{tag}'
            tag_command = f'docker image tag {image} {new_image}'
            push_command = f'docker image push {new_image}'
            subprocess.run(tag_command, shell=True, check=True)
            subprocess.run(push_command, shell=True, check=True)
    else:
        print('Please specify image(s) via list or command line.')

def pull_n_push(images, docker_repo, harbor_url, username, password):
    pull_images(images, docker_repo, username, password)
    push_images(images, harbor_url, username, password)
