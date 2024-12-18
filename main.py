import requests
import time

from bs4 import BeautifulSoup

url = ""

result = requests.get(url)

print(result.text)


# After fetching data
time.sleep(10) # waits 10 seconds before making the next request




# Websites

# TCGPlayer = API available
# Cardmarket = Web scraping?
# Amazon = API?