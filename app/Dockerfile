FROM python:3.7-alpine

ARG WORKDIR
# default 引数
ARG ENCODING="utf-8"
ARG SELENIUM_URL="http://selenium:4444/wd/hub"
ARG C.UTF-8
ARG LANGUAGE

# イメージからコンテナに渡す
ENV RUNTIME_PACKAGES="build-base libffi-dev make gcc" \
  HOME=${WORKDIR} \
  PYTHONIOENCODING=${ENCODING} \
  LANG=C.UTF-8 \
  LANGUAGE=en_US:en \
  TZ=Azia/Tokyo

WORKDIR ${WORKDIR}

COPY . .

# appにfirefoxと、geckodriverがないといけないためinstall
RUN apk add --update && \
  apk upgrade && \
  apk add --virtual build-dependencies --no-cache ${RUNTIME_PACKAGES} && \
  apk add firefox && \
  wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz && \
  tar -x geckodriver -zf geckodriver-v0.30.0-linux32.tar.gz -O > /usr/bin/geckodriver && \
  chmod +x /usr/bin/geckodriver && \
  pip install -r requirements.txt && \
  rm geckodriver-v0.30.0-linux32.tar.gz && \
  apk del build-dependencies

