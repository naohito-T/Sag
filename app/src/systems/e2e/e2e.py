# coding: utf-8
# ↑を入れると勝手に整形しだす
from selenium.webdriver.common.keys import Keys  # OSのKeyがbindされている
import time
from _e2eBase import BaseE2E
from config.config import Config


# 抽象クラスのプロパティもselfでアクセスできる。


class E2E(BaseE2E):
    _config: Config

    def __init__(self) -> None:
        super()
        self._config = Config()

    # 指定のsiteを開く
    def site_opne(self):
        self._driver.get(self._config.login_url)
        time.sleep(3)

    # ユーザー名とパスワードを入力してリターンキーを押す
    def login(self) -> None:
        usernameField = self._driver.find_element_by_xpath(self._config.username_path)
        # key送信
        usernameField.send_keys(self._config.username)
        time.sleep(1)
        passwordField = self._driver.find_element_by_xpath(self._config.password_path)
        passwordField.send_keys(self._config.password)
        passwordField.send_keys(Keys.RETURN)
        time.sleep(3)
