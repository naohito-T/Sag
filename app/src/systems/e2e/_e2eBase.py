from abc import ABCMeta, abstractmethod
from typing import Any
from selenium import webdriver

# metaclass=ABCMeta抽象クラスとして動作


class BaseE2E(metaclass=ABCMeta):
    # これアクセスできないかも
    # @see https://qiita.com/ukisoft/items/b7c410b96dde1922a2d0
    _driver: Any

    @abstractmethod
    def __init__(self, _):
        self._driver = webdriver.Firefox()

    # methodを設定しないとerrorを履く使用
    @abstractmethod
    def site_opne(self) -> None:
        raise NotImplementedError()
