from abc import ABCMeta, abstractmethod
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from functools import singledispatch

# metaclass=ABCMeta抽象クラスとして動作
# ブラウザ本体としてFirefoxが必要です。
# またFirefoxを制御するために、Selenium WebdriverのバックエンドとしてFirefox Geckodriverが必要です。
# @see https://daily.belltail.jp/?p=2691#hs_342b04f4780e5780c15898f3454cffaa_header_5


class BaseE2E(metaclass=ABCMeta):
    # これアクセスできないかも
    # @see https://qiita.com/ukisoft/items/b7c410b96dde1922a2d0
    _driver: webdriver.Firefox  # クラス変数

    # クラス変数とインスタンス変数
    # @see https://uxmilk.jp/41600
    @abstractmethod
    def __init__(self):
        options = Options()
        # Headless mode
        options.headless = True
        # firefox(ブラウザ)のバイナリを指定
        options.binary = FirefoxBinary("/usr/bin/firefox")
        # Firefoxがクラッシュする場合はgeckodriverのログレベルを上げる
        # Firefoxのログをカレントディレクトリのgeckodriver.logに吐くようにできます。
        # options.log.level = "trace"
        self._driver = webdriver.Firefox(
            executable_path="/usr/bin/geckodriver", options=options
        )

    # methodを設定しないとerrorを吐く
    # @singledispatch
    # self._driver.get
    # def site_open(self, url: str) -> None:
    #     raise NotImplementedError()

    # methodを設定しないとerrorを吐く
    @abstractmethod
    def driver_down(self) -> None:
        raise NotImplementedError()
