import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class JINKO:
    def __init__(self):
        self.op = Options()
        # self.op.add_argument("--headless")
        self.op.add_argument("no-sandbox")
        self.op.add_argument("--disable-extensions")
        self.op.add_argument('--disable-gpu')  
        self.op.add_argument('--ignore-certificate-errors')
        self.op.add_argument('--allow-running-insecure-content')
        self.op.add_argument('--disable-web-security')
        self.op.add_argument('--disable-desktop-notifications')
        self.op.add_argument("--disable-extensions")
        self.op.add_argument('--lang=ja')
        self.op.add_argument('--blink-settings=imagesEnabled=false')
        self.op.add_argument('--disable-dev-shm-usage')
        self.op.add_argument('--proxy-server="direct://"')
        self.op.add_argument('--proxy-bypass-list=*')
        # self.op.add_argument('--start-maximized')
        self.op.add_experimental_option("excludeSwitches", ['enable-automation'])

    def syokika(self):
        driver = webdriver.Chrome(options=self.op)
        driver.implicitly_wait(30)
        return driver

    def strato(self):
        url = "https://www.worldometers.info/world-population/"
        self.driver.get(url)

    def get_current_population(self):
        try:
            counter_element = self.driver.find_element(By.CLASS_NAME, 'maincounter-number')
            population_element = counter_element.find_element(By.CLASS_NAME, 'rts-counter')
            population = population_element.text.strip()
            print(f"現在の人口：{population}人")
        except Exception as e:
            print(f"Failed to retrieve data: {e}")
        finally:
            self.driver.refresh()

    def liset(self):
        print("「ブラウザを再起動します。」")
        self.driver.quit()
        self.driver = self.syokika()
        time.sleep(3)
        self.strato()
        

    def main(self):
        self.driver = self.syokika()
        self.strato()
        self.get_current_population()
        schedule.every().hour.at(":30").do(self.liset)
        schedule.every().minutes.at(":00").do(self.get_current_population)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    JINKO().main()