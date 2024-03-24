import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
name_list = response.text
soup = BeautifulSoup(name_list, features="lxml")
film_names = soup.find_all(name="h3", class_="title")
film_names = reversed(film_names)
with open("names.txt", "a", encoding="utf-8") as file:
    for name in film_names:
        file.write(name.get_text() + "\n")








