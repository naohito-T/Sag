# from selenium import webdriver

# # Chrome のオプションを設定する
# options = webdriver.ChromeOptions()

# # Selenium Server に接続する
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=options,
# )

# # Selenium 経由でブラウザを操作する
# driver.get('https://qiita.com')
# print(driver.current_url)

# # ブラウザを終了する
# driver.quit()

# 成功
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)
driver.implicitly_wait(5)

driver.get("https://www.time-j.net/worldtime/country/jp")

print(driver.find_element_by_xpath(
    "/html/body/div/div[6]/div[1]/div/p[5]").text)
driver.quit()
