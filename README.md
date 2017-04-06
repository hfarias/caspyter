## Caspyter BASE (CASA + Jupyter)


## Install Caspyter on Docker
---

### 1.- Docker
The first step is install docker, docker is:

> Docker is the world’s leading software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux and Windows Server apps. [More info](https://www.docker.com/what-docker)

To install follow the following instructions [Download Docker Community Edition](https://www.docker.com/community-edition#/download)


After installation of docker, create a folder named CASPYTER and next run the next command in your terminal:
~~~python
      docker run --name caspyter  -it -d \
      -v /rute/to/caspyter:/data \
      -p 8022:22 -p 8080:80 -p 8081:8081\
      -h caspyter ubuntu:14.04
~~~

It's time to access the container, run the next command in your terminal:
~~~python
    docker exec -it caspyter /bin/bash
~~~

### 2.- Clone Caspyter/Casanova files

This project is base on [Casanova](https://github.com/kaspervd/casanova) project, before clone this project you must install git, copy and run (as root) the scrip **install_caspyter.sh** (in this repository  [/script/install_caspyter.sh](https://github.com/hfarias/caspyter/blob/master/README.md))


### 3.- Start Caspyter

Firts go to caspyter user and restart bash variables

~~~python
    su caspyter
    cd /home/caspyter
    source /home/caspyter/.bashrc
~~~

then got to the notebook folder and start caspyter


~~~python
    cd /home/caspyter/notebook
    caspyter
~~~

Caspyter will show you this message:
~~~python
Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8081/?token=908b0654058e58f6a81f4f54cf392f1a0f401f2da9d6cc62
~~~

Now you must replace 0.0.0.0 for localhost in you browser.

