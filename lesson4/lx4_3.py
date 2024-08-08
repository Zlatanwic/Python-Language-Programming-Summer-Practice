from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class bbs_web():
    def __init__(self):
        self.bbs_browser= webdriver.Chrome()
        self.login_page = 'http://cyr985.net3v.club/bbs/login.asp'
        self.post_page = 'http://cyr985.net3v.club/bbs/topic.asp?id=4891&boardid=6&TB=1'
        self.wait_time=3
    def auto_login(self,username,password):
        self.bbs_browser.get(self.login_page)
        time.sleep(self.wait_time)

        username_input = self.bbs_browser.find_element(value="name",by=By.NAME)
        password_input = self.bbs_browser.find_element(value="Password",by=By.NAME)
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.bbs_browser.find_element(value="login",by=By.CLASS_NAME)
        login_button.click()
        time.sleep(self.wait_time)
    def auto_post(self,bbs_content):
        self.bbs_browser.get(self.post_page)
        time.sleep(self.wait_time)
        #liuyan=self.bbs_browser.find_element(by=By.XPATH,value='/html/body/div[5]/table[1]/tbody/tr[1]/td[2]/div[1]/a[2]')
        #liuyan.click()
        iframe=self.bbs_browser.find_element(by=By.ID,value='edit')
        self.bbs_browser.switch_to.frame(iframe)
        time.sleep(3)
        send_message=self.bbs_browser.find_element(value='/html/body',by=By.XPATH)
        send_message.send_keys(bbs_content)
        time.sleep(3)
        self.bbs_browser.switch_to.parent_frame()
        submit=self.bbs_browser.find_element(value='sayb',by=By.ID)
        submit.click()

if __name__ == "__main__":
    tj_bbs=bbs_web()
    tj_bbs.auto_login('Zlatanwic','85136688Likuo')
    tj_bbs.auto_post(bbs_content='2353113 li kuo')