# coding: utf-8
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # OSのKeyがbindされている

# import os
# import urllib.parse
# import time

# import datetime
# import sys
# import traceback

# import readfile

from systems.e2e.e2e import E2E
from config.config import Config
from typing import List

# def main(system):


def main():
    # injectの雰囲気でやる
    e2e: E2E = E2E()

    config: Config = Config()
    # e2e.test()
    # Instagramのサイトを開く
    e2e.site_open(config.login_url)
    # loginする
    e2e.login()

    if "アカウントが不正使用されました" in driver.page_source:
        print(driver.page_source)
        print("ブロックされました。パスワードを変更する必要があります。")
        print("処理を終了します。")
        exit()

    e2e.driver_down()

    # ハッシュタグ毎のループ
    # ハッシュタグ検索用のURL

    off = False  # 処理を終了する切り替えスイッチ
    error_cnt = 0
    words: List[str] = ["", ""]

    # これは自動で要素分繰り返してくれるのでは？
    for word in words:

        # 繰り返しを終了(wordsがなくなったらでいいのでは？)
        if off:
            break

        # これLineに送信でいいのでは？
        print("http req get hashtag page: " + tag_search_url.format(word))
        #  ハッシュタグのURLを開く
        e2e.site_open(config.tag_search_url.format(word))
        #  これはなにをしている？
        e2e.driver_implicitly_wait()

        #  リンクのhref属性の値を取得
        mediaList = e2e.find_elements_by_tag_name("a")
        hrefList: List[str] = []

        # 1つのハッシュタグに表示された画像のhrefを配列に格納
        for media in mediaList:
            href = media.get_attribute("href")
            if "/p/" in href:
                hrefList.append(href)

        # 画像のhrefを格納した配列でループ処理
        for href in hrefList:
            # すでにいいね！していた場合はスルー
            if href in already_likes_url:
                print("[いいね！済]" + href)
            else:
                e2e.site_open(href)
                try:
                    e2e.find_element_by_xpath().click()

                    if "ブロックされています" in driver.page_source:
                        print("ブロックされました。処理を終了します。")
                        off = True
                        break

                    likes_cnt += 1
                    print("いいね！ {}".format(likes_cnt))
                    flc = open(file_l_cnt, "w")
                    flc.write(
                        data_other_than_today + today + "\t" + str(likes_cnt) + "\n"
                    )
                    flc.close()

                    fa = open(file_alu, "a")
                    fa.write(href + "\n")
                    fa.close()

                    # [ already_likes_url ] へいいねしたURLを追加
                    already_likes_url.append(href)

                    # この地点を通過する時にいいね！max_limit_likes_counter(デフォルト値500)回超えてたら終了
                    # BAN防止
                    if likes_cnt >= max_limit_likes_counter:
                        print(
                            "いいね！の上限回数({})を超えました。処理を終了します。".format(
                                max_limit_likes_counter
                            )
                        )
                        off = True

                except Exception as e:
                    ex, ms, tb = sys.exc_info()
                    print(ex)
                    print(ms)
                    traceback.print_tb(tb)
                    error_cnt += 1
                    time.sleep(5)
                    if error_cnt > max_limit_error_cnt:
                        print("エラーが{}回を超えました。処理を終了します。".format(max_limit_error_cnt))
                        off = True

                if off:
                    break

    print("本日のいいね！回数 {}".format(likes_cnt))
    ブラウザを閉じる
