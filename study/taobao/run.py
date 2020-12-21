import requests
from selenium import webdriver
import time

if __name__ == '__main__':
    bro = webdriver.Chrome("../../chromedriver.exe")
    bro.get("https://www.taobao.com/")
    #标签交互
    input = bro.find_element_by_id("mq")
    input.send_keys("原神")
    #执行一组js程序
    bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    #按钮交互
    submit = bro.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
    submit.click()
    time.sleep(5)
    bro.close()
    print(1)