# coding: utf-8
# ↑を入れると勝手に整形しだす
import sys
import pprint
from config.config import Config
from main import main

pprint.pprint(sys.path)
print(">Sag Project Start")


config = Config()


args = sys.argv
# 実行ファイル
executable_file = args[0]
# argsの第二引数が存在しなければtrue
if not args[1:2]:
    args_words = "n"
else:
    # Noneじゃなければそのまま引数代入
    args_words = args[1]

# 対話式で入れてくのがいいのではないか？
# yesかnoで対話式か設定ファイルか
# main
print(">>> Sag Project Start")
print(">>> Give me an argument")
print(">>> y: Run from argument n: Run from file")
input_args = input()

if input_args == "y":
    print(">>>>>>>>引数から実行します")
    if args_words:
        # 引数をsystemsのclassに代入し渡す
        args_words
        main()
    else:
        print(">>>>>>>>引き数がないため何もせず終了しました。")
        exit(0)
else:
    print(">>>>>>>>file読み込みから実行します")
    # 引数をsystemsのclassに代入し渡す
    main()
