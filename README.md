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

[Pythonで型を極める(3.9)](https://qiita.com/papi_tokei/items/bf652696d6b98f23565a)
[最強のPython型チェッカーmypy](https://developers.microad.co.jp/entry/2021/10/04/063000#:~:text=mypy%20%E3%81%AFPython3%E3%81%A82.7%E5%90%91%E3%81%91%E3%81%AE%E9%9D%99%E7%9A%84%E5%9E%8B%E3%83%81%E3%82%A7%E3%83%83%E3%82%AB%E3%83%BC%E3%81%A7%E3%81%99%E3%80%82&text=%E5%9E%8B%E3%82%A2%E3%83%8E%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E3%82%82%E3%81%A8,%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82)
[PEP 561 以前の型情報の配布事情](https://blog.ymyzk.com/2018/09/creating-packages-using-pep-561/)

[参考URL](https://ang.tokyo/insta_auto_likes/)
