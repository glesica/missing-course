# A container image that wraps a simple Python 3 program.
#
# To build the image:
#   docker build -t say_hello .
#
# To run the container:
#   docker run say_hello [human [computer]]

FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3

COPY say_hello.py /say_hello.py

RUN useradd -U user
USER user

VOLUME /data

ENTRYPOINT ["python3", "/say_hello.py"]

