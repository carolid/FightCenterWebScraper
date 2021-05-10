# imports --------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# code ----------------------------------------------------------------------------------------------

# Scrape:

page = requests.get("https://www.espn.com/mma/fightcenter")
soup = BeautifulSoup(page.content, "html.parser")

soup_list = list(soup.children)
html = soup_list[3]
body = list(html.children)[3]
p_tag = list(body.children)
p = list(body.children)[1]


data = soup.find(class_="AccordionPanel__body")

# Extract:

data_display = data.get_text()
print(data_display)







