FROM python:3.7

ARG WORKDIR
# default 引数
ARG ENCODING="utf-8"
ARG SELENIUM_URL="http://selenium:4444/wd/hub"
ARG C.UTF-8
ARG LANGUAGE

# イメージからコンテナに渡す
ENV HOME=${WORKDIR} \
  PYTHONIOENCODING=${ENCODING} \
  LANG=C.UTF-8 \
  LANGUAGE=en_US:en \
  TZ=Azia/Tokyo

WORKDIR ${WORKDIR}

COPY . .

RUN pip install -r requirements.txt
