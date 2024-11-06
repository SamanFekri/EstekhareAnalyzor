from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import tqdm

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if you want to run headless

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://old.aviny.com/quran/estekhareh/index2.aspx"
n = 1000
result_path = 'data/test_result.txt'

# if directory does not exist, create it
os.makedirs(os.path.dirname(result_path), exist_ok=True)
# if file does not exist, create it
if not os.path.exists(result_path):
  with open(result_path, 'w') as f:
    f.write('')

for i in tqdm.tqdm(range(n)):
  try:
    # Open the URL
    driver.get(url)
    time.sleep(1)
    # read the page in the url of the browser and print it 
    random_page = driver.current_url.split('page=')[-1]
    with open(result_path, 'a') as f:
      f.write(f'{random_page}\n')
  except Exception as e:
    print(f"An error occurred: {e}")