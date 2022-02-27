# coding: utf-8
# ↑を入れると勝手に整形しだす
import os
from datetime import date
# from typing import Anys


class File:
    # アクセス修飾子がないためprivateは慣例で_(アンスコ)をつける
    _path: str # path = "{0}/tmp/{1}_count.txt".format(os.getcwd(), today)
    today: date

    # 参考演算子
    # x = "OK" if n == 10 else "NG"

    # コンストラクタ
    def __init__(self, path: str, today: date):
        self._path = path
        self._today = today

    # static mehods (引数にインスタンスを受け取らない)
    # インスタンスを生成しなくてもクラスから直接呼び出すことができるメソッドです。
    # @staticmethod
    # def function():

    # classメソッド
    # classメソッドとは、インスタンスを生成しなくてもクラスから直接呼び出すことができるメソッドです
    # いつ使うと良いか
    # インスタンス変数やインスタンスメソッドにアクセスしないとき(メソッド内でselfを使わないとき）は classmethod、staticmethodを使おう。
    # classmethod: クラス変数にアクセスすべきときや、継承クラスで動作が変わるべきときは classmethodを使おう。
    # staticmethod: 継承クラスでも動作が変わらないときはstaticmethodを使おう
    # どちらもデコレーターで定義できる。classmethodでは第一引数にclsを与えて定義する

    # 指定されたパスにあるファイルの存在確認をする
    def is_file(self) -> bool:
        return os.path.isfile(self._path)

    # いいね！したいワードをファイルから取得
    @classmethod
    def readFile(cls) -> list[str]:
        with open(cls._path, "r", encoding="utf-8") as f:
            words = f.readlines
        return words

    # ファイル作成(新規作成をwithにする)
    # staticのためdateがなくても動作させる
    # defaultは今日。違う場合は指定の日時
    # 指定された日時のファイルを作成する(pathは固定させる)
    @classmethod
    def touch_file(cls, today: date = date.today()) -> None:
        # カレントディレクトリの絶対パス
        # @see https://note.nkmk.me/python-script-file-path/
        today = date.today()  # 2022-02-26
        with open(cls._path, "w", encoding="utf-8") as f:
            f = open()
            f.write("{0} \t0\n".format(today))
            f.close()
        # 環境変数のpassを読み込みパスを作成する


    # 本日、いいねしている数をファイルから取得
    # if 本日を決め、読み込む。または今日の日付のファイルがない場合はelse
    # else fileがない、または本日のファイルがなければを作成し書き込む
    def load_count_today_like(today: date = date.today()) -> int:
        # today = datetime.date.today() # 2022-02-26
        _likes_cnt = 0
        path = "{0}/tmp/{1}_count.txt".format(os.getcwd(), str(today))
        # ファイル確認(本日のファイルがあるのか)
        if is_file(path):
            # 読み込んでcountを返す
            with open(path, "r", encoding="utf-8") as f:
                _likes_cnt = f.readline()
                return int(_likes_cnt)
        else:
            # ファイル作成し0を渡す
            return _likes_cnt




    # すでにいいね！したURLの読み込み 2回目のいいねはキャンセルになるから
    def already_liked_urls() -> dict:
        # 配列を作成。ファイルにはURLが一行ずつ記載されている。読み込んだ行数のカウント数とurl
        # {
        #     urls: ['str', 'str1', 'str2'],
        #     count: 0
        # }
        # 辞書型作成 dict型 アクセス d['name']
        liked_url_list = { 'urls': [], 'count': 0}
        path = "{0}/tmp/liked_urls.txt".format(os.getcwd())
        with open(path, "r", encoding="utf-8") as f:
            # 行数文読み込んで代入する。最後にcountを挿入

        return liked_url_list
    # いいねした回数を求める
