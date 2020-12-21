import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

if __name__ == '__main__':
    bro = webdriver.Chrome("../../chromedriver.exe")
    bro.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
    #标签交互
    bro.switch_to.frame("iframeResult")
    div = bro.find_element_by_id("draggable")
    #动作链
    action = ActionChains(bro)

    action.click_and_hold(div)
    for i in range(5):
        action.move_by_offset(17,0).perform()
        time.sleep(0.3)
    action.release()
    bro.quit()