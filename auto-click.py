from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
import configparser
import random

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                ]

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])

driver_path = './chromedriver'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://schoo.jp/')
time.sleep(3)

element = driver.find_elements(By.ID,"btn_login_modal")[1]

# モーダルを開く
actions = ActionChains(driver)
actions.click(element).perform()

# ログイン画面入力

mail = config_ini['CONFIG']['Mail']
password = config_ini['CONFIG']['Pass']

driver.find_element(By.NAME,"mail").send_keys(mail)
driver.find_element(By.NAME,"passwd").send_keys(password)

actions.click(driver.find_element(By.ID,"btn_login_submit")).perform()
time.sleep(3)

lecture_video_url = config_ini['CONFIG']['Video']
driver.get(lecture_video_url)

# マウスを動かし続ける処理
perform_time_sec = config_ini['CONFIG']['VideoTimeMin'] * 60

start_time = time.time()

while True:
    actions.move_to_element(driver.find_element(By.CLASS_NAME,"complex-box")).perform()
    actions.move_by_offset(50,50)
    time.sleep(random.randrange(30,40))
    actions.move_by_offset(-50,-50)
    time.sleep(random.randrange(30,40))
    actions.click(driver.find_element(By.CLASS_NAME,"js-sleepIcon")).perform()
    if time.time() == start_time + int(perform_time_sec):
        break;