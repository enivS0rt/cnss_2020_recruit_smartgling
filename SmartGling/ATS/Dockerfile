FROM ubuntu:16.04

WORKDIR /conf
ADD . /conf

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    cp /conf/sources.list /etc/apt/sources.list && \
    apt-get update && apt-get install -y xinetd vim lib32z1 build-essential \
    autoconf automake libtool pkg-config libmodule-install-perl gcc \
    libssl-dev libpcre3-dev libcap-dev libhwloc-dev libncurses5-dev \
    libcurl4-openssl-dev flex tcl-dev net-tools curl wget && \
    chmod +x /conf/entrypoint.sh

RUN mv /conf/trafficserver-7.1.2.tar.gz /tmp && cd /tmp && \
    tar -xvf trafficserver-7.1.2.tar.gz && cd trafficserver-7.1.2 && \
    autoreconf -if && ./configure --prefix=/opt/ts-712 && make && make install

ENTRYPOINT /conf/entrypoint.sh
