# coding: utf-8
# ↑を入れると勝手に整形しだす
import sys
from config.config import Config
from main import main

config = Config()


args = sys.argv
# 実行ファイル
executable_file = args[0]
# 第一引数
args_words = args[1]

# 対話式で入れてくのがいいのではないか？
# yesかnoで対話式か設定ファイルか

print(">Sag Project Start")
print(">Give me an argument")
print(">  y: Run from argument n: Run from file")
input_args = input()

if args_words[1] != "file" or input_args == "y":
    print(">>>>>>>>引数から実行します")
    # 引数をsystemsに代入し渡す
    args_words
    main()
elif args_words[1] == "file" or input_args != "n":
    print(">>>>>>>>file読み込みから実行します")
    main()
else:
    print(">>>>>>>>引き数がないため何もせず終了しました。")
    exit(0)
