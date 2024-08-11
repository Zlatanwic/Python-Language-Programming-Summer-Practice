from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ph_broswer=webdriver.Chrome()
url='https://cn.pornhub.com/pornstars'
ph_broswer.get(url)
time.sleep(3)
popstar=ph_broswer.find_element(value='//*[@id="popularPornstars"]',by=By.XPATH)
top_list=popstar.find_elements(value='li',by=By.TAG_NAME)
print(len(top_list))
star_list=[]
#name=top_list[0].find_element(value='wrap',by=By.CLASS_NAME).find_element(value='thumbnail-info-wrapper',by=By.CLASS_NAME).find_element(value='title',by=By.CLASS_NAME).find_element(value='modelName.performerCardName').text
for i in range(50):
    name=top_list[i].find_element(value='//*[@id="popularPornstars"]/li['+str(i+1)+']/div/div[2]/a',by=By.XPATH).text
    star_list.append(name)
#print(name)


print(star_list)
import xlwt
workbook=xlwt.Workbook(encoding = 'utf-8')
worksheet=workbook.add_sheet('phstars')
for i in range(len(star_list)):
    worksheet.write(i,0, star_list[i])
workbook.save('starlist.xls')

