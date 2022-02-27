# coding: utf-8
# ↑を入れると勝手に整形しだす


class E2E:
    def __init__(self, arg):
        self._var = arg


# ユーザー名とパスワードを入力してリターンキーを押す
usernameField = driver.find_element_by_xpath(username_path)
usernameField.send_keys(username)
time.sleep(1)
passwordField = driver.find_element_by_xpath(password_path)
passwordField.send_keys(password)
passwordField.send_keys(Keys.RETURN)
time.sleep(3)
