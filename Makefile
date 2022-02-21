# docker-compose downはコンテナやネットワークを停止するだけではなく、それらを破棄する
# 規定ではボリュームは削除しない(だからボリュームのリセットも必用)

# 起動
.PHONE: up
up:
	docker-compose down; docker-compose up -d

# 停止
.PHONE: down
down:
	docker-compose down

# イメージ作成
.PHONE: build
build:
	docker-compose build


.PHONE: exec
exec:
	docker-compose exec app /bin/bash

