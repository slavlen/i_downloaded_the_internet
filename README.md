# Docker Image Management Script

This is a simple script for pulling Docker images from public repositories and pushing them to private repositories.

## Features

- Pull images from specified Docker repositories.
- Push images to specified local repositories.
- Pull images from Docker repositories and then push them to local repositories in one command.

## Usage

1. **Pull Images**
    ```sh
    sudo python3 main.py pull -u <username> -p <password> -d <docker-repo> -l <path_to_list_file>
    ```
    Example:
    ```sh
    sudo python3 main.py pull -u myuser -p mypass -d dockerhub -l ./list.txt
    ```

2. **Push Images**
    ```sh
    sudo python3 main.py push -u <username> -p <password> -L <local-repo> -i <image_name(s)>
    ```
    Example:
    ```sh
    sudo python3 main.py push -u myuser -p mypass -L mylocalrepo.io -i nginx
    ```

3. **Pull and Push Images**
    ```sh
    sudo python3 main.py pull_n_push -u <username> -p <password> -d <docker-repo> -L <local-repo> -i <image_name(s)>
    ```
    Example:
    ```sh
    sudo python3 main.py pull_n_push -u myuser -p mypass -d dockerhub -i nginx
    ```

## Options

- `-u, --username` : Username for dockerhub.com or local_repo.
- `-p, --password` : Password for dockerhub.com or local_repo.
- `-L, --local-repo` : Local repository URL.
- `-l, --list` : Path to a file with a list of images.
- `-i, --image` : Image name(s) separated by spaces.
- `-d, --docker-repo` : Docker repository for pulling images. Choices are `dockerhub`, `mirror`, `huecker`. Default is `dockerhub`.
- `-h, --help` : Show help message and exit.

## Examples

1. **Pulling Images from DockerHub**
    ```sh
    sudo python3 main.py pull -u myuser -p mypass -d dockerhub -l ./list.txt
    ```

2. **Pushing Images to Local Repository**
    ```sh
    sudo python3 main.py push -u myuser -p mypass -L mylocalrepo.io -i nginx
    ```

3. **Pulling from DockerHub and Pushing to Local Repository**
    ```sh
    sudo python3 main.py pull_n_push -u user -p mypass -d dockerhub -i nginx
    ```

## Notes

- The `-l` option allows you to specify a file containing a list of images to pull or push.
- If both `-l` and `-i` are used, the script will combine the images from both sources.

## Requirements

- Python 3.x
- Docker CLI

## License

This project is MIT licensed 
