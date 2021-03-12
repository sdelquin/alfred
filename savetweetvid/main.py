import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

SERVICE_URL = 'https://www.savetweetvid.com'
tweet_url = sys.argv[1]

try:
    if not tweet_url.startswith('https://twitter.com/'):
        raise Exception('Input url does not come from Twitter')

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(SERVICE_URL)

    element = driver.find_element_by_xpath('//*[@id="form_download"]/div/input')
    element.send_keys(tweet_url, Keys.ENTER)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div/div[2]/div/div[1]/h5')
        )
    )

    element = driver.find_elements_by_css_selector('a.btn-download')[0]
except Exception as err:
    print('Something did not work!', err)
else:
    print(element.get_attribute('href'))
