#!/usr/bin/env bash

apt update

apt install -y \
    curl geany aptitude synaptic \
    build-essential gdb dh-autoreconf libgl1-mesa-dev pkg-config python-zmq libzmq3-dev libxslt1.1 git
