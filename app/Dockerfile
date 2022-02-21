FROM python:3.7

ARG WORKDIR
# default 引数
ARG ENCODING="UTF-8"
ARG SELENIUM_URL="http://selenium:4444/wd/hub"

# イメージからコンテナに渡す
ENV HOME=${WORKDIR}} \
  PYTHONIOENCODING=${ENCODING}

WORKDIR ${WORKDIR}

COPY . .

RUN pip install -r requirements.txt
