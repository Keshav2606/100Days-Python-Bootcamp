from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

news_articles = soup.select(".titleline a")
news_titles = []
news_links = []
news_upvotes = []

for news_title in news_articles:
    news_titles.append(news_title.getText())
    news_links.append(news_title.get("href"))

news_title_upvotes = soup.find_all(name="span", class_="score")

for news_upvote in news_title_upvotes:
    news_upvotes.append(int(news_upvote.getText().split()[0]))

for i in range(len(news_titles)):
    print(news_titles[i])
    print(news_links[i])
    print(news_upvotes[i])
    print("")

