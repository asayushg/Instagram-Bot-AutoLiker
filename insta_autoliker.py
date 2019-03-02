from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = r'G:\chromedriver.exe' #Here enter the location of your chromedriver exe file.
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

username = webdriver.find_element_by_name('username')
username.send_keys('yourusername')
password = webdriver.find_element_by_name('password')
password.send_keys('yourpassword')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
button_login.click()
sleep(3)
try:
  notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
  notnow.click()
sleep(1)
webdriver.get('https://www.instagram.com/username_user/') #username_user = replace with the username of the person.
sleep(5)
first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
first_thumbnail.click()
sleep(5)
next_post='1'
null=''
liked,unlike=0,0
while next_post is not null:
    if liked>0 or unlike>0:
        next_post.click()
        sleep(5)
    like = webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
    if like.get_attribute("aria-label")=="Like":
        like.click()
        liked +=1
    else:
        unlike=1
    try:
        next_post = webdriver.find_element_by_link_text('Next')
    except :
        next_post = null
print(str(liked)+' Posts Liked!')

