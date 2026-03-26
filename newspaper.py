from bs4 import BeautifulSoup
import pandas as pd
import requests

box = []

for x in range(1,201):
    
    # url
    website = f"https://indianexpress.com/section/india/page/{x}/"
    

    r = requests.get(website)                       # request
    soup = BeautifulSoup(r.content,"html.parser")

    news_bundle = soup.find_all("h2",class_="hdg3")

    for news in news_bundle:
        headline = news.find("a")
        headline = headline.get_text(strip=True) if headline else None

        all_news = {
            "news" : headline
        }

        box.append(all_news)


# create dataframe
df = pd.DataFrame(box)

# saving dataframe into csv file
df.to_csv("news_headings.csv")

