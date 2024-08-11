from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyttsx3

class Tj_web():
    def __init__(self):
        self.tj_browser = webdriver.Chrome()
        self.first_page='https://news.tongji.edu.cn/info/1003/88134.htm'


    def auto_replace(self,new_name):
        self.tj_browser.get(self.first_page)
        time.sleep(3)
        #更改网页标题
        self.tj_browser.execute_script(
            "document.querySelectorAll('h3').forEach(el => { el.innerHTML = el.innerHTML.replace('覃海洋', arguments[0]); });",
            new_name
        )
          # 确保看到更改效果
        time.sleep(5)

    def speak_title(self):
        h3_elements = self.tj_browser.find_elements(value='h3',by=By.TAG_NAME)
        text_to_speak = " ".join([el.text for el in h3_elements])

        # 使用 pyttsx3 朗读文本
        engine = pyttsx3.init()
        engine.say(text_to_speak)
        engine.runAndWait()

web_instance=Tj_web()
web_instance.auto_replace('潘展乐')
web_instance.speak_title()
