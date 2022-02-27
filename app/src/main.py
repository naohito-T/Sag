# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # OSのKeyがbindされている
import os
import urllib.parse
import time
import datetime
import sys
import traceback
import readfile

def main(system):
    # injectの雰囲気でやる
    # Firefoxを起動
    driver = webdriver.Firefox()
    # Instagramのサイトを開く
    driver.get(config.login_url)
    time.sleep(3)

    if "アカウントが不正使用されました" in driver.page_source:
        print(driver.page_source)
        print("ブロックされました。パスワードを変更する必要があります。")
        print("処理を終了します。")
        exit()

# ハッシュタグ毎のループ
# ハッシュタグ検索用のURL
tag_search_url = "https://www.instagram.com/explore/tags/{}/?hl=ja"
off = False  # 処理を終了する切り替えスイッチ
error_cnt = 0
for word in words:

    if off:
        break
    print("http req get hashtag page: " + tag_search_url.format(word))
    driver.get(tag_search_url.format(word))
    time.sleep(3)
    driver.implicitly_wait(10)

    # リンクのhref属性の値を取得
    mediaList = driver.find_elements_by_tag_name("a")
    hrefList = []

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
            driver.get(href)
            time.sleep(2)
            try:
                driver.find_element_by_xpath(like_x_path).click()
                time.sleep(2)
                # print(driver.page_source)
                if "ブロックされています" in driver.page_source:
                    print("ブロックされました。処理を終了します。")
                    off = True
                    break

                likes_cnt += 1
                print("いいね！ {}".format(likes_cnt))
                flc = open(file_l_cnt, "w")
                flc.write(data_other_than_today + today + "\t" + str(likes_cnt) + "\n")
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
                        "いいね！の上限回数({})を超えました。処理を終了します。".format(max_limit_likes_counter)
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
# ブラウザを閉じる
# driver.quit()
