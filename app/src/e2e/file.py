# coding: utf-8
# ↑を入れると勝手に整形しだす


class FileSystem:
    # アクセス修飾子がないためprivateは慣例で_(アンスコ)をつける
    _word = ""
    _file = ""

    # コンストラクタ
    def __init__(self, word: str, file: str):
        self._word = word
        self._file = file

    # static mehods (引数にインスタンスを受け取らない)
    # インスタンスを生成しなくてもクラスから直接呼び出すことができるメソッドです。
    # @staticmethod
    # def function():

    # classメソッド
    # classメソッドとは、インスタンスを生成しなくてもクラスから直接呼び出すことができるメソッドです
