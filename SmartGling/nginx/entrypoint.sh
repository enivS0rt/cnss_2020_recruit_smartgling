set -x

rm -rf Dockerfile entrypoint.sh

cp ./nginx.conf /etc/nginx/nginx.conf

nginx-debug -g "daemon off;"
