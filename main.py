import sys
import argparse
import os
from docker_utils import pull_images, push_images, pull_n_push

def print_help():
    help_text = """
    Docker Image Management Script

    Usage:
        python main.py [options] action

    Actions:
        pull            Pull images from the specified Docker repository.
        push            Push images to the specified local repository.
        pull_n_push     Pull images from the Docker repository and then push them to the local repository.

    Options:
        -u, --username  Username for dockerhub.com or local_repo.
        -p, --password  Password for dockerhub.com or local_repo.
        -L, --local-repo Local repository URL.
        -l, --list      Path to file with list of images.
        -i, --image     Image name(s) separated by spaces.
        -d, --docker-repo
                        Docker repository for pulling images. Choices are 'dockerhub', 'mirror', 'huecker'.
                        Default is 'dockerhub'.
        -h, --help      Show help message and exit.

    Examples:
        python main.py -u myuser -p mypass -d dockerhub -i image1 image2 pull
        python main.py -u myuser -p mypass -L mylocalrepo.io -i image1 image2 push
        python main.py -u myuser -p mypass -d dockerhub -L mylocalrepo.io -i image1 image2 pull_n_push
    """
    print(help_text)

docker_repos = {
    'dockerhub': 'docker.io',
    'mirror': 'mirror.gcr.io',
    'huecker': 'huecker.io'
}

def main():
    parser = argparse.ArgumentParser(description='Docker image management script.', add_help=False)
    parser.add_argument('-u', '--username', type=str, help='Username for dockerhub.com or local_repo.')
    parser.add_argument('-p', '--password', type=str, help='Password for dockerhub.com or local_repo.')
    parser.add_argument('-L', '--local-repo', type=str, help='Local repository URL.')
    parser.add_argument('-l', '--list', type=str, help='Path to file with list of images.')
    parser.add_argument('-i', '--image', type=str, nargs='*', help='Image name(s) separated by spaces.')
    parser.add_argument('-d', '--docker-repo', choices=['dockerhub', 'mirror', 'huecker'], default='dockerhub', help='Docker repository for pulling images.')
    parser.add_argument('-h', '--help', action='store_true', help='Show help message and exit.')
    parser.add_argument('action', nargs='?', choices=['pull', 'push', 'pull_n_push'], help='Action to perform: pull, push, or pull_n_push.')

    # Check if the first argument matches any of the actions
    if len(sys.argv) > 1 and sys.argv[1] in ['pull', 'push', 'pull_n_push']:
        # Set the action accordingly
        parser.set_defaults(action=sys.argv[1])

    args = parser.parse_args()

    if args.help or not args.action:
        print_help()
        return

    images = []
    if args.list:
        list_file = args.list
        if os.path.isfile(list_file):
            with open(list_file, 'r') as file:
                images.extend([line.strip() for line in file])

    if args.image:
        # Exclude the action from the images list
        images = [image for image in args.image if image != args.action]

    if args.action == 'pull':
        if args.docker_repo and args.username and args.password and images:
            docker_repo = docker_repos[args.docker_repo]
            pull_images(images, docker_repo, args.username, args.password)
        else:
            print('Please provide all required arguments (-u, -p, -d, -l/-i) for the pull operation.')

    elif args.action == 'push':
        if args.username and args.password and args.local_repo and images:
            push_images(images, args.local_repo, args.username, args.password)
        else:
            print('Please provide all required arguments (-u, -p, -L, -l/-i) for the push operation.')

    elif args.action == 'pull_n_push':
        if args.docker_repo and args.username and args.password and args.local_repo and images:
            docker_repo = docker_repos[args.docker_repo]
            pull_n_push(images, docker_repo, args.local_repo, args.username, args.password)
        else:
            print('Please provide all required arguments (-u, -p, -d, -L, -l/-i) for the pull_n_push operation.')

if __name__ == '__main__':
    main()