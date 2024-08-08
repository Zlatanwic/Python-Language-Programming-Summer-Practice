from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#打开浏览器
brower = webdriver.Chrome()
url='https://music.163.com/#/discover/toplist'
brower.get(url)
time.sleep(5)
iframe = brower.find_element(value='g_iframe',by=By.ID)
brower.switch_to.frame(iframe)

#寻找大容器
toplist = brower.find_element(value='toplist',by=By.ID)
#寻找tbody 通过标签名
tbody = toplist.find_elements(value='tbody',by=By.TAG_NAME)[0]
#寻找所有tr
trs = tbody.find_elements(value='tr',by=By.TAG_NAME)

dataList = []
for each in trs:
    #排名
    rank = each.find_elements(value='td',by=By.TAG_NAME)[0].find_elements(value='num',by=By.CLASS_NAME)[0].text
    musicName = each.find_elements(value='td',by=By.TAG_NAME)[1].find_elements(value='txt',by=By.CLASS_NAME)[0].\
        find_element(value='b',by=By.TAG_NAME).get_attribute('title')
    print(musicName)
    singer = each.find_elements(value='td',by=By.TAG_NAME)[3].find_elements(value='text',by=By.CLASS_NAME)[0].\
        get_attribute('title')
    print(singer)
    dataList.append([rank,musicName,singer])

print(dataList)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = '云音乐飙升榜'
ws.append(['排名','歌名','歌手'])
for data in dataList:
    ws.append(data)

wb.save("云音乐飙升榜.xlsx")