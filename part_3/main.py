from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from body import generate_body

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"
DEFAULT_USER_DOWNLOAD_PATH = "/Users/breakthealgo/Downloads/chromedriver"

def start():

    webdriver = initialize_webdriver()

    if webdriver == None:
        print("Something went wrong")
        return

    login(webdriver)
    post(webdriver)
    logout(webdriver)

    webdriver.quit()

    return

def login(webdriver):
    
    # YOUR TWITTER PASSWORD AND USERNAME GO HERE
    username = ""
    password = ""

    webdriver.get("https://twitter.com/i/flow/login")

    WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys(username)
    time.sleep(2)

    WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys(Keys.RETURN)
    time.sleep(2)

    WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys(password)
    time.sleep(2)

    WebDriverWait(webdriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys(Keys.RETURN)
    time.sleep(4)

    return

def post(webdriver):

    title = generate_body(DEFAULT_USER_AGENT)
    tweet_text_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div"
    webdriver.find_element(by=By.XPATH, value=tweet_text_xpath).send_keys(title)
    time.sleep(3)

    tweet_submit_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]"
    webdriver.find_element(by=By.XPATH, value=tweet_submit_xpath).click()
    time.sleep(3)

    return

def logout(webdriver):

    webdriver.get("https://twitter.com/logout")

    time.sleep(4)

    logout_button_xpath = "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]"

    webdriver.find_element(by=By.XPATH, value=logout_button_xpath).click()

    time.sleep(4)

    return

def initialize_webdriver():
    try:

        print("Initializing Webdriver...")

        options = Options()

        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        service = Service(DEFAULT_USER_DOWNLOAD_PATH)

        driver = webdriver.Chrome(service=service, options=options)

        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": DEFAULT_USER_AGENT})

        return driver

    except Exception as e:
        print("Issue initializing webdriver: " + str(e))
        return None

if __name__ == '__main__':
    start()
