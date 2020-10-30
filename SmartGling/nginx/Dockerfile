FROM nginx

WORKDIR /conf
ADD . /conf

RUN chmod +x /conf/entrypoint.sh

ENTRYPOINT /conf/entrypoint.sh
