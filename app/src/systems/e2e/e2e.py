# coding: utf-8
# pyright: reportUnknownVariableType=false
# ↑を入れると勝手に整形しだす
from selenium.webdriver.common.keys import Keys  # OSのKeyがbindされている
from time import sleep
from ._e2eBase import BaseE2E
from config.config import Config
from typing import Any, List, Unknown
from functools import singledispatch

# 抽象クラスのプロパティもselfでアクセスできる。


class E2E(BaseE2E):
    _config: Config

    def __init__(self) -> None:
        # 継承
        super().__init__()
        self._config = Config()

    # 指定のsiteを開く
    @singledispatch
    def site_open(self, url: str) -> None:
        self._driver.get(url)
        sleep(3)

    # ユーザー名とパスワードを入力してリターンキーを押す
    def login(self) -> None:
        usernameField = self._driver.find_element_by_xpath(self._config.username_path)
        # key送信
        usernameField.send_keys(self._config.username)
        sleep(1)
        passwordField = self._driver.find_element_by_xpath(self._config.password_path)
        passwordField.send_keys(self._config.password)
        passwordField.send_keys(Keys.RETURN)
        sleep(3)

    # driver終了
    def driver_down(self) -> None:
        self._driver.down()

    # これは何？(待つのかな)
    def driver_implicitly_wait(self) -> None:
        self._driver.implicitly_wait(10)

    # 配列で指定のタグが格納される
    def find_elements_by_tag_name(self, tag_name: str) -> List[str]:
        return self._driver.find_elements_by_tag_name(tag_name)

    # x path 検索(横?)
    def find_element_by_xpath(self, x_path: str) -> None:
        # self._driver.find_element_by_xpath(x_path).click()
        self._driver.find_element_by_xpath(x_path)
        sleep(2)

    # そのpageのソース
    def page_source(self) -> None:
        self._driver.page_source

    # test
    def test(self) -> None:
        self._driver.get("https://nikkei225jp.com/data/karauri.php")
        sleep(5)
        html = self._driver.page_source.encode("utf-8")
        print(html)
