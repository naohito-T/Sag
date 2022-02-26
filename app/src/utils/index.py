# coding: utf-8
# ↑を入れると勝手に整形しだす

import os
import urllib.parse
import datetime
from typing import Any

# いいね！したいワードをファイルから取得
def readFile() -> str:
    words = open("")
    words = readfile.readWords(file_words)
    return words


# 指定されたパスにあるファイルの存在確認をする
def is_file(path: str) -> bool:
    return os.path.isfile(path)


# 本日、いいねしている数をファイルから取得
# if 本日を決め、読み込む。または今日の日付のファイルがない場合はelse
# else fileがない、または本日のファイルがなければを作成し書き込む
def load_count_today_like(today: Any = datetime.date.today()) -> int:
    # today = datetime.date.today() # 2022-02-26
    _likes_cnt = 0
    path = "{0}/tmp/{1}_count.txt".format(os.getcwd(), str(today))
    # ファイル確認(本日のファイルがあるのか)
    if is_file(path):
        # 読み込んでcountを返す

        return _likes_cnt
    else:
        # ファイル作成し0を渡す
        return _likes_cnt


# ファイル作成
def touch_file() -> None:
    # カレントディレクトリの絶対パス
    # @see https://note.nkmk.me/python-script-file-path/
    today = datetime.date.today()  # 2022-02-26
    path = "{0}/tmp/{1}_count.txt".format(os.getcwd(), today)
    f = open(path, "w")
    f.write("{0} \t0\n".format(today))
    f.close()
    # 環境変数のpassを読み込みパスを作成する


# すでにいいね！したURLの読み込み
already_likes_url = readfile.readAlreadyLikesURL(file_alu)
