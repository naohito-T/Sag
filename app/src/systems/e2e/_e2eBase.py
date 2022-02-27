from abc import ABCMeta, abstractmethod
from typing import Any
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# metaclass=ABCMeta抽象クラスとして動作


class BaseE2E(metaclass=ABCMeta):
    # これアクセスできないかも
    # @see https://qiita.com/ukisoft/items/b7c410b96dde1922a2d0
    _driver: Any

    @abstractmethod
    def __init__(self):
        options = Options()
        options.headless = True
        options.binary = FirefoxBinary("/usr/bin/firefox")
        self._driver = webdriver.Firefox(
            executable_path="/usr/bin/geckodriver", options=options
        )

    # methodを設定しないとerrorを履く使用
    @abstractmethod
    def site_opne(self) -> None:
        raise NotImplementedError()
