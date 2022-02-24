# bashで実行する
SHELL=/bin/bash

# docker-compose downはコンテナやネットワークを停止するだけではなく、それらを破棄する
# 規定ではボリュームは削除しない(だからボリュームのリセットも必用)

# ---------------------------------------------------------------#
#  											Variables		 														 #
# ---------------------------------------------------------------#

# ログの色
R := \e[31m
G := \e[32m
B := \e[34m
N := \e[0m

# .envrc書き込みパス
DECODING_PATH := dotenv ./env/decrypt/.env.

# ---------------------------------------------------------------#
#  											Make for Docker.		 										 #
# ---------------------------------------------------------------#

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

# ---------------------------------------------------------------#
#  												setup make 													 	 #
# ---------------------------------------------------------------#

# @をつけると実行コマンドを標準出力に出力しない。
# 暗号化
# Usage. $ (make env.encrypt KEY=xxxx FILE_PATH=xxx)
.PHONY: env.encrypt
env.encrypt:
	@make _env.encrypt KEY=$(KEY) INPUT=./env/decrypt/$(FILE_PATH) OUTPUT=./env/encrypt/$(FILE_PATH)

# 復号化
# Usage. $ (make env.decrypt KEY=xxxx FILE_PATH=xxx)
.PHONY: env.decrypt
env.decrypt:
	@make _env.decrypt KEY=$(KEY) INPUT=./env/encrypt/$(FILE_PATH) OUTPUT=./env/decrypt/$(FILE_PATH)

# .envrc 作成
.PHONY: envrc.make
envrc.make:
	@make _env.makerc ENVIRONMENT=$(ENVIRONMENT)

# ---------------------------------------------------------------#
#  												make method 													 #
# ---------------------------------------------------------------#

# 暗号化 method
_env.encrypt:
	@if [ -n "$(KEY)" ]; then\
		openssl aes-256-cbc -e -in $(INPUT) -pass pass:$(KEY) | base64 > $(OUTPUT);\
		printf '${B}%s\n' "# 鍵を暗号化し配置しました。→→$(OUTPUT)";\
	else\
		printf '${R}%s\n' "# you need define KEY.\nyou need read README.md.";\
	fi

# 復号化 method
_env.decrypt:
	@if [ -n "$(KEY)" ]; then\
		cat $(INPUT) | base64 -d | openssl aes-256-cbc -d -out $(OUTPUT) -pass pass:$(KEY);\
		printf '${B}%s\n' "# 鍵を復号化し配置しました。→→$(OUTPUT)";\
	else\
		printf '${R}%s\n' "# you need define KEY.\nyou need read README.md.";\
	fi

# .envrc 作成method
# 最初の > で.envrcを必ず上書きします。
_env.makerc:
	@if [ -n "$(ENVIRONMENT)" ]; then\
		printf '${B}%s\n' "# envを.envrcに記載";\
		echo ${DECODING_PATH}$(ENVIRONMENT) > .envrc;\
		direnv allow;\
		printf '${B}%s\n' "# $(ENVIRONMENT)用の.envrcを作成。\n.envrc done";\
	else\
		printf '${R}%s\n' "# you need define ENVIRONMENT.\nyou need read README.md.";\
	fi
