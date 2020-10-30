set -x

rm -rf Dockerfile entrypoint.sh

mv /conf/records.config /opt/ts-712/etc/trafficserver/records.config

mv /conf/remap.config /opt/ts-712/etc/trafficserver/remap.config

/opt/ts-712/bin/trafficserver start

while true; do
	sleep 60
done;
