import requests
from bs4 import BeautifulSoup
import tqdm
import time
import json
import os

BASE_URL = 'https://old.aviny.com/quran/estekhareh/index2.aspx?mode=manual'
EXPORT_PATH = 'data/src.jsonnl'
SLEEP_TIME = 2

data = []

# Loop through the pages and extract the data
for page in tqdm.tqdm(range(1, 604, 2)):
  item = {
    'page': page,
    'result': None,
    'general_result': None,
    'marriage_result': None,
    'trade_result': None,
  }
  url = f'{BASE_URL}&page={page}'
  response = requests.get(url)
  response.raise_for_status()
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')

  result = soup.find('span', id='L_GoodBad_Name')
  if result:
    item['result'] = result.get_text()
  
  general_result = soup.find('span', id='L_Result_General')
  if general_result:
    item['general_result'] = general_result.get_text()

  marriage_result = soup.find('span', id='L_Result_Marriage')
  if marriage_result:
    item['marriage_result'] = marriage_result.get_text()

  trade_result = soup.find('span', id='L_Result_Trade')
  if trade_result:
    item['trade_result'] = trade_result.get_text()

  data.append(item)
  # Sleep for a while to avoid getting blocked
  time.sleep(SLEEP_TIME)

# create the data directory if it does not exist
os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)

# save the data as jsonnl
with open(EXPORT_PATH, 'w', encoding='utf-8') as f:
  for item in data:
    f.write(json.dumps(item, ensure_ascii=False) + '\n')

