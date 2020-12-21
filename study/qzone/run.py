from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    bros = webdriver.Chrome("../../chromedriver.exe",chrome_options=chrome_options)
    url = "https://qzone.qq.com/"
    bros.get(url)

    bros.switch_to.frame('login_frame')
    password_username = bros.find_element_by_id("switcher_plogin")
    password_username.click()
    '''action_chain = ActionChains(bros)
    action_chain.click(password_username)'''
    print("进入qq空间登录页面")
    qq = bros.find_element_by_id("u")
    pwd = bros.find_element_by_id("p")
    go = bros.find_element_by_id("login_button")
    qq.send_keys("591193117")
    pwd.send_keys("L15810898455")
    go.click()
    print("成功登录")
    print(bros.page_source)
    bros.quit()


    