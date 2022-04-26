import requests
from datetime import datetime
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def tabela(godzin):
    TOKEN = "213721372137"
    USERNAME = "aapa123daaw"
    TODAY = datetime.now()

    pixela_endpoint = "https://pixe.la/v1/users"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    graph_id = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
    graph_data = {
        "date": TODAY.strftime("%Y%m%d"),
        "quantity": godzin,
    }

    response = requests.post(url=graph_id, json=graph_data, headers=headers)
    print(f"Liga tabela status: {response.text}")


def SMS(numery):
    TOKEN = "censored"
    SID = "censored"
    client = Client(SID, TOKEN)

    for numer in numery:
        message = client.messages \
                        .create(
            body="We are playing now, get in",
            from_="+17402792849",
            to=f"{numer}"
        )

def mecz():
    service = Service("/Users/kubo-/chrome driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://oksjuwejaroszowice2.futbolowo.pl/")

    print("Poprzedni mecz:\n")
    team1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/table/tbody/tr[2]/td[1]')
    team2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/table/tbody/tr[2]/td[3]')
    data = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/div/time/span[2]')
    wynik2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/table/tbody/tr[4]/td[3]')
    wynik1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/table/tbody/tr[4]/td[1]')
    godzina = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/aside[1]/section/div/div/div[3]/div[1]/div/time/span[4]')
    text = f"```\nOstatni mecz odbył się: {data.text} o godzinie: {godzina.text}\n{team1.text}\nKontra\n{team2.text}\nWynik: {wynik1.text}:{wynik2.text}\n```"
    driver.quit()
    return text

def nextmecz():
    service = Service("/Users/kubo-/chrome driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://oksjuwejaroszowice2.futbolowo.pl/schedule/friendly/33465")
    data = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/section/section/table/tbody/tr[1]/td[1]/time')
    godzina = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/section/section/table/tbody/tr[1]/td[2]/time')
    gra = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/section/section/table/tbody/tr[1]/td[7]/div')
    text = f"Juw-e zagra {data.text} o godzinie {godzina.text} z {gra.text}"
    driver.quit()
    return text

def fb():
    option = Options()
    service = Service("/Users/kubo-/chrome driver/chromedriver.exe")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(options=option, service=service)
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys("censored")
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("censored")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/span/div/div[1]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div[5]/div/div[1]/a/div[1]/div/div[2]/div/div/span/span').click()
    chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[1]/p')
    chat.send_keys("censored")
    chat.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.quit()
    return