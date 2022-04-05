from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

def start():

    webdriver = initialize_webdriver()
    # Keeps the webdriver open for 10 seconds
    time.sleep(10)
    
    if webdriver == None:
        print("Something went wrong")
        return

    return

def initialize_webdriver():
    try:

        print("Initializing Webdriver...")

        options = Options()

        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # specify where your chrome driver is downloaded
        service = Service("/Users/breakthealgo/Downloads/chromedriver")

        driver = webdriver.Chrome(service=service, options=options)
        
        # This line is duplicated in the video
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'})

        return driver

    except Exception as e:
        print("Issue initializing webdriver: " + str(e))
        return None

if __name__ == '__main__':
    start()
