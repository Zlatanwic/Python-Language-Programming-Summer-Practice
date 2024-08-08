from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class tj_web:
    def __init__(self):
        self.tj_browser = webdriver.Chrome()
        self.first_page = "https://www.tongji.edu.cn"
        self.wait_time = 10

    def auto_click(self, txt_list):
        self.tj_browser.get(self.first_page)
        for txt in txt_list:
            menu_element = self.tj_browser.find_element(value=txt,by=By.LINK_TEXT)
            menu_element.click()
            time.sleep(self.wait_time)
            # 截图并保存为菜单名.png
            self.tj_browser.save_screenshot(f"{txt}.png")
            # 保存页面内容为txt文件（utf-8编码）
            with open(f"{txt}.txt", "w", encoding="utf-8") as txt_file:
                txt_file.write(self.tj_browser.page_source)

# 示例用法
if __name__ == "__main__":
    first_page_url = "https://www.tongji.edu.cn"
    txt_list = ['科学研究','招生就业']
    my_tj_web = tj_web()
    my_tj_web.auto_click(txt_list)