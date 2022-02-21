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

Seleniumを使う(Docker)

## Docker

[リファレンス](https://github.com/SeleniumHQ/docker-selenium)

## Selenium

Web ブラウザ
Chrome, Firefox, IE, Opera など
WebDriver(ブラウザのバージョンに合ったバージョンを選ばないと動作しないという若干面倒な問題があるのですが、)
ブラウザを操作するための API を公開するモジュール
Selenium
WebDriver と通信しプログラムからブラウザを操作するライブラリ
