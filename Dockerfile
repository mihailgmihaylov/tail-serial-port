ARG PYTHON_VERSION="3.12.3"
ARG ALPINE_VERSION="alpine3.19"

FROM python:${PYTHON_VERSION}-${ALPINE_VERSION}

WORKDIR /scripts

COPY tail-serial-port.py /scripts

RUN pip install pyserial \
  && addgroup -g 10001 python \
  && adduser -u 10000 -S python -G python \
  && chown -R python:python /scripts

USER python

ENTRYPOINT ["python", "/scripts/tail-serial-port.py"]
