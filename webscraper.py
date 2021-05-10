# imports --------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# code ----------------------------------------------------------------------------------------------

# Scrape:

page = requests.get("https://www.espn.com/mma/fightcenter")
soup = BeautifulSoup(page.content, "html.parser")

# soup_list = list(soup.children)
# html = soup_list[3]
# body = list(html.children)[3]
# p_tag = list(body.children)
# p = list(body.children)[1]

fight_stats = []
for item in soup.find_all(class_="Accordion"):
    fight_stats.append(item.get_text())

fighter_names = []
for item in soup.find_all(class_="truncate"):
    fighter_names.append(item.get_text())


# Extract:

print(fighter_names)
print(fight_stats)
fight_stat_dict = {"Fighters: " : "",
                   "Total Strikes: " : "",
                   "Significant Strikes: " : "",
                   "Head Strikes: " : "",
                   "Body Strikes: " : "",
                   "Leg Strikes: " : "",
                   "Time in Control: " : "",
                   "Takedowns: " : "",
                   "Submissions: " : ""}

for fighters in fighter_names:
    for index in range(0, 2):
        fight_stat_dict["Fighters: "] += fighter_names[index]
    fighter_names = fighter_names[2:]

print(fight_stat_dict)









