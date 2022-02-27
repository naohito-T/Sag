# Introduction

## 要件定義

ハッシュタグを指定できる
いいねの数を指定
再いいね防止機能（1回いいねした投稿へいいねするとキャンセルになってしまうから。）
手動実行のみ
いいねの数を知り、いいねを見送る

## 非機能要件

海外か、日本で分ける

## 機能要件

Selenium
Docker

## Docker

[リファレンス](https://github.com/SeleniumHQ/docker-selenium)

## Selenium

Web ブラウザ
Chrome, Firefox, IE, Opera など
WebDriver(ブラウザのバージョンに合ったバージョンを選ばないと動作しないという若干面倒な問題があるのですが、)
ブラウザを操作するための API を公開するモジュール
Selenium
WebDriver と通信しプログラムからブラウザを操作するライブラリ

---

以下を参考にした
[参考URL](https://inasala.com/docker-selenium-python/)

## Docker上でSeleniumで動かす

Docker上でSeleniumを使うには、パソコン上のブラウザにアクセスして使うのは困難
このため、Docker上でSeleniumを使うには3つの環境が必用

・selenium/hub

・selenium/node-chrome-debug

・Python環境

## selenium/hub

これは、「selenium/node-chrome-debug」に向けてseleniumのコマンド（処理）を実行するための環境（コンテナ）です。

このコンテナのイメージは、Docker hubで公開されていて、誰でも使えます。

## selenium/node-chrome-debug

これは、selenium/hubからの処理を実際にChromeで実行する環境です。

1つのselenium/hubに対して、複数の実行環境を作ることも可能です。

また、実行画面を確認するために、VNCという画面共有するアプリもインストールされています。

## pip version

```sh
# pip freeze
async-generator==1.10
attrs==21.4.0
certifi==2021.10.8
cffi==1.15.0
cryptography==36.0.1
h11==0.13.0
idna==3.3
outcome==1.1.0
pycparser==2.21
pyOpenSSL==22.0.0
PySocks==1.7.1
selenium==4.1.2
sniffio==1.2.0
sortedcontainers==2.4.0
trio==0.20.0
trio-websocket==0.9.2
typing_extensions==4.1.1
urllib3==1.26.8
wsproto==1.1.0
```
