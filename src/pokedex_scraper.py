import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 

# Obtaining data from bulbapedia with selenium
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_II-V)'
driver = webdriver.Chrome()
driver.get(url) 
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.sortable.roundy.jquery-tablesorter')))
rows = table.find_elements(By.TAG_NAME, 'tr')

if not rows:
    raise Exception("No rows found in the table.")

# Skip dex num
# Skip image row
name = []
hp = []
attack = []
defense = []
sp_attack = []
sp_defense = []
speed = []
# Skip bst 
# Skip average

for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, 'td')
    name_col = cols[2].text.strip()
    hp_col = cols[3].text.strip()
    attack_col = cols[4].text.strip()
    defense_col = cols[5].text.strip()
    spattack_col = cols[6].text.strip()
    spdefense_col = cols[7].text.strip()
    speed_col = cols[8].text.strip()

    name.append(name_col)
    hp.append(hp_col)
    attack.append(attack_col)
    defense.append(defense_col)
    sp_attack.append(spattack_col)
    sp_defense.append(spdefense_col)
    speed.append(speed_col)

data = {'Pokemon': name,
        'HP': hp,
        'Attack': attack,
        'Defense': defense,
        'Sp. Attack': sp_attack,
        'Sp. Defense': sp_defense,
        'Speed': speed}

df = pd.DataFrame(data)

print(df)
df.to_csv('pokedex.csv', index=False)
driver.quit()

