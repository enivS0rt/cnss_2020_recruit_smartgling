FROM python:3.7-alpine

WORKDIR /app
ADD . /app

RUN pip3 install /app/whls/click*.whl && \
    pip3 install /app/whls/its*.whl && \
    cd /app/whls/MarkupSafe-1.1.1 && \
    python3 setup.py install && \
    pip3 install /app/whls/Werk*.whl && \
    pip3 install /app/whls/Jinja2*.whl && \
    pip3 install /app/whls/Flask*.whl && \
    pip3 install /app/whls/*redis*.whl && \
    pip3 install /app/whls/requests*.whl && \
    chmod +x /app/entrypoint.sh

ENTRYPOINT /app/entrypoint.sh
