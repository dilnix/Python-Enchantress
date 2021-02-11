## Saving, extracting and packing back edited docker image in Linux

#### Before starting to make following as example make sure that your Linux distribution have already isntalled all needed dependencies, that is: tar, docker and gzip.

#### Then try:

`cd homework/docker_practice-hw` go to current folder

`mkdir my_ubuntu` create a folder for future manipulations

`docker save ubuntu:latest | gzip > ubuntu_latest.tar.gz` save image as archive

`docker inspect ubuntu` output saved image metadata

`tar -xvzf ubuntu_latest.tar.gz --directory ./my_ubuntu/ && cd my_ubuntu/` extract the tar file to get access to the raw image data and go to folder with contains

lookup and make changes (if necessary) to files like: manifest.json (global image metadata with HEX numbers) and HEX.json (detailed image metadata) in root directory and in root of additional directories

`tar -cvzf ../my_ubuntu.tar.gz ./*` pack back edited files into my_ubuntu.tar.gz

`cd .. && cat my_ubuntu.tar.gz | docker load` re-import the modified image

`docker inspect my_ubuntu` output your image metadata to verify changes have been applied

## Runiing container that just outputs a date and time in Rome, Italy

`docker build -t date_in_rome .` build image according to present Dockerfile based on previously re-packed "my_ubuntu" image

`docker run --rm date_in_rome` run container to see if it works and outputs expected results
