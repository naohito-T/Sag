# docker-compose downはコンテナやネットワークを停止するだけではなく、それらを破棄する
# 規定ではボリュームは削除しない(だからボリュームのリセットも必用)

#
# firefox
#

# firefox イメージ作成
.PHONE: firefox.build
firefox.build:
	docker-compose -f docker-compose-chrome.yml build

# firefox 起動
.PHONE: firefox.up
firefox.up:
	docker-compose down; docker-compose -f docker-compose-firefox.yml up

#
# Chrome
#

# chrome イメージ作成
.PHONE: chrome.build
chrome.build:
	docker-compose -f docker-compose-chrome.yml build

# chrome 起動
.PHONE: chrome.up
chrome.up:
	docker-compose down; docker-compose -f docker-compose-chrome.yml up


#
# edge
#

# edge イメージ作成
.PHONE: chrome.build
edge.build:
	docker-compose -f docker-compose-chrome.yml build

# edge 起動
.PHONE: edge.up
edge.up:
	docker-compose down; docker-compose -f docker-compose-edge.yml up
