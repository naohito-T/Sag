# Introduction

```sh
##################################################
################   For Firefox  ##################
##################################################
```

## Setup

```sh
$ git clone [Sag repository name]
$ cd Sag
# zshの場合、zshではない場合は各環境変数の渡し方を参照する。
$ (make env.decrypt KEY=xxxx FILE_PATH=xxx)
```

## Usage

Slackに送信
cronで対応(macのcronをgitで管理するのは？)
test
https://qiita.com/flcn-x/items/fcbbc2fb291b970290f2

## Enviroment

pythonは型付けをできるようにした。
Python + Selenium WebDriver + Headless Firefox + Docker + pytest

---

## How To

### 1. テストを実行したい時

- docker起動
`$ make up`

- 起動後実行
`$ make exec.selenium`

**※docker起動後、すぐにコマンド実行を施してもよかったが何度も実行したい場合を加味しそちらで対応している。**

### 2. テストを並列に実行したい時

本環境ではSelenium Gridが構築されているため

- VNCサーバー接続確認(Mac)
Finder > 移動 > サーバへ接続 > サーバーアドレス: vnc://localhost:5900

## Thank you.

[reference](https://www.selenium.dev/ja/)
[reference(日本語版)](https://kurozumi.github.io/selenium-python/api.html)
[参考URL](https://ang.tokyo/insta_auto_likes/)
