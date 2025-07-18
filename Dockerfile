FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        strace \
        vim \
        python3 \
        python3-pip

WORKDIR /work
