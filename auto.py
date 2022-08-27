
email='saisivakumar.2000@gmail.com'
password='David@joy1289'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import os
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

repository=input("Enter repository name:")

driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://github.com/login')

user=driver.find_element_by_id('login_field')
user.send_keys(email)

user=driver.find_element_by_id('password')
user.send_keys(password)

sign=driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
sign.submit()

time.sleep(4)
new=driver.find_element_by_xpath('/html/body/div[5]/div/aside/div/div[1]/div/h2/a')
new.click()

time.sleep(3)
new=driver.find_element_by_xpath('/html/body/div[5]/main/div/form/div[2]/auto-check/dl/dd/input')
new.send_keys(repository)

check=driver.find_element_by_xpath('/html/body/div[5]/main/div/form/div[5]/div[4]/div[1]/label/input[2]')
check.click()

time.sleep(3) 
create=driver.find_element_by_xpath('/html/body/div[5]/main/div/form/div[5]/button')
create.submit()

time.sleep(5)
clone=driver.find_element_by_xpath('/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary')
clone.click()
#/html/body/div[5]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary


clone=driver.find_element_by_xpath('/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy')
clone.click()

url=clipboard.paste()
print(url)

#/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary
#/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy

os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "first commit"')
os.system('git branch -M main')
os.system('git remote add origin '+ url)
os.system('git push -f origin main')

print('\n',8*'==', 'Successfully uploaded...! Thank you..!',8*'==')



