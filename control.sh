#!/bin/bash

name="star_bot"
image="stars_bot"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

start() {
    if [ ! "$(docker ps -q -f name=$name)" ]; then
        if [ "$(docker ps -aq -f status=exited -f name=$name)" ]; then
            echo "Old container found, removing..."
            docker rm $name
        fi
        docker run -d --name $name $image
    fi
}

stop() {
    docker container kill $name
}

build() {
    docker build -t $image .
    stop
    start

}

reload() {
    docker kill -s HUP $name
}

case "$1" in
    start)
       start
       ;;
    stop)
       stop
       ;;
    reload)
       reload
       ;;
    build)
       build
       ;;
    *)
       echo "Usage: $0 {start|stop|build|reload}"
esac

exit 0
