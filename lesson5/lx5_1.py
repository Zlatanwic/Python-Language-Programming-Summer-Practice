from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baidu_brower=webdriver.Chrome()
url='https://top.baidu.com/board'
baidu_brower.get(url)
time.sleep(3)
hot_block=baidu_brower.find_element(value='//*[@id="sanRoot"]/main/div[1]/div[1]',by=By.XPATH)
hot_list=hot_block.find_elements(value='item-wrap_2oCLZ',by=By.CLASS_NAME)
#print(len(hotlist))
toplist=[]
#top=hot_block.find_element(value='//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[1]',by=By.XPATH).find_element(value='normal_1fQqB',by=By.CLASS_NAME).find_element(value='content-wrap_1RisM',by=By.CLASS_NAME).find_element(value='name_2Px2N',by=By.CLASS_NAME).find_element(value='c-single-text-ellipsis',by=By.CLASS_NAME).text
top=baidu_brower.find_element(value='//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[1]',by=By.XPATH).text
#top=baidu_brower.find_element(value='item-wrap_2oCLZ.active',by=By.CLASS_NAME).find_element(value='normal_1fQqB',by=By.CLASS_NAME).find_element(value='content-wrap_1RisM',by=By.CLASS_NAME).find_element(value='name_2Px2N',by=By.CLASS_NAME).find_element(value='c-single-text-ellipsis',by=By.CLASS_NAME).text
#print(top)
toplist.append(top)
#//*[@id="sanRoot"]/main/div[1]/div[1]/div[2]/a[1]
for each in hot_list:
    #rank=each.find_element(value='normal_1fQqB',by=By.CLASS_NAME).find_element(value='div',by=By.TAG_NAME)[0].text
    content=each.find_element(value='normal_1fQqB',by=By.CLASS_NAME).find_element(value='content-wrap_1RisM',by=By.CLASS_NAME).find_element(value='name_2Px2N',by=By.CLASS_NAME).find_element(value='c-single-text-ellipsis',by=By.CLASS_NAME).text
    #print(rank)
    #print(content)
    if content:
        toplist.append(content)
print(toplist)
import xlwt
workbook=xlwt.Workbook(encoding = 'utf-8')
worksheet=workbook.add_sheet('百度热搜')
for i in range(len(toplist)):
    worksheet.write(i,0, toplist[i])
workbook.save('百度热搜.xls')

