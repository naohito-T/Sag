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

