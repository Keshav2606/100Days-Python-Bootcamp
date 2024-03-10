from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
movie_titles.reverse()

with open("top100movies.txt", mode="w", encoding="utf8") as file:
    for title in movie_titles:
        file.writelines(f"{title.getText()}\n")
