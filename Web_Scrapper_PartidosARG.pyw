from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--headless")#que no se abra chrome

#Pantalla de Display
driver = webdriver.Chrome(options = chrome_options)#cargar las opciones
driver.implicitly_wait(30) 

driver.get('https://www.adamchoi.co.uk/teamgoals/detailed')#web

#Acciones
all_matches_button = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))#select para dropdown
dropdown.select_by_visible_text('Argentina')


matches = driver.find_elements(By.TAG_NAME, 'tr')#Tabla completa


#Organizacion de Informacion
partidos = []
for match in matches:
    partidos.append(match.text)

driver.quit()

#Pandas 
df = pd.DataFrame({'Partidos':partidos})
print(df)
df.to_excel('partidos.xlsx')

