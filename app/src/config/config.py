import dataclasses
import os


# config class
# イミュータブル(変更不可)にし環境変数をsetする


@dataclasses.dataclass(frozen=False)
class Config:
    def __init__(self):
        # instagram user_name
        self._username: str = os.environ["USER_NAME"]
        # instagram password
        self._password: str = os.environ["PASSWORD"]
        # １日にいいね！できる最大値。この数を超えたら処理終了
        self._max_limit_likes_counter: int = 100
        # 自動いいね！時、エラーがこの数を超えたら処理終了
        self._max_limit_error_cnt: int = 10
        # Instagram ログインURL
        self._login_url: str = "https://www.instagram.com/"
        # ログイン用フォームへのパス
        self._username_path: str = "//form//div[1]//input"
        # ログイン用フォームへのパス
        self._password_path: str = "//form//div[2]//input"
        # いいね！ボタン取得用
        self._like_x_path: str = "//main//section//button"

    # @see
    # https://naruport.com/blog/2019/8/27/python-tutorial-class-property-getter-setter/

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def max_limit_likes_counter(self) -> int:
        return self._max_limit_likes_counter

    @property
    def max_limit_error_cnt(self) -> int:
        return self._max_limit_error_cnt

    @property
    def login_url(self) -> str:
        return self._login_url

    @property
    def username_path(self) -> str:
        return self._username_path

    @property
    def password_path(self) -> str:
        return self._password_path

    @property
    def like_x_path(self) -> str:
        return self._like_x_path
