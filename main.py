"""---------------------------------------- Film Suggestion ----------------------------------------
This project is a **Film Suggestion**.
This app takes a list of popular movies, sorts them in descending order by rating. Then it starts from the beginning
of the list and asks the user if he has seen the movie. If the user has not seen the movie,
the user is suggested to watch the movie and the name of the movie is googled for the user to choose his site to watch.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import os
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---------------------------------------- Movie List Website ----------------------------------------

best_movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# ---------------------------------------- Google for search selected movie) ----------------------------------------

selected_watch_url = "https://www.google.com/"
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

# ---------------------------------------- Get the Movie List ----------------------------------------

response = requests.get(best_movies_url)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [item.getText() for item in all_movies]
movies = movie_titles[::-1]

# ---------------------------------------- Checking Movies with user ----------------------------------------

for movie in movies:
    is_seen = input(f"Have you seen the movie{movie}?y or n\n")

    # ---------------------------------------- Unseen Movie suggestion ----------------------------------------

    if is_seen == "n":
        print(f"I suggest you watch the movie {movie}")

        # ---------------------------------------- Search movie name in Google ----------------------------------------

        driver_service = Service(executable_path=chrome_driver_path)
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=driver_service, options=chrome_option)
        driver.get(selected_watch_url)
        time.sleep(5)
        cookies_acp = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
        cookies_acp.click()
        time.sleep(3)
        search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(movie.split(") ")[1])
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        break
