"""
    Desktop Notifier
Gives notification on desktop if there's a new post on the website,
main title of the post is displayed in the notification.

- https://beautiful-soup-4.readthedocs.io/en/
- https://plyer.readthedocs.io/en/

"""

import os
import json
import time
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from plyer import notification


def notify_me(post_title, post_link, ico_img):
    notification.notify(
        title = "KUN.UZ Yangiliklari",
        message = post_title,
        app_name = "News",
        app_icon = ico_img,
        timeout = 2
    )


def notify_new_post():

    WEBSITE_URL = "https://kun.uz/news/list"

    resp = requests.get(WEBSITE_URL)
    if resp.status_code != 200:
        print("Error: Could not get data from the website.")
        exit(1)

    soup = BeautifulSoup(resp.text, "lxml")
    latest_post = soup.find("div", id="news-list").find_all("a")[1]
    post_link = "https://kun.uz" + latest_post["href"]
    post_title = latest_post.find("p", class_="news-title").text
    if latest_post.find("img"):
        post_img = latest_post.find("img")["src"]
        ico_img = "icon.ico"
        # Converts an image from a URL to ICO format and saves it.
        Image.open(BytesIO(requests.get(post_img).content)).save(ico_img)
    else:
        post_img = None
        ico_img = None

    try:
        with open("cache.json", 'r') as file:
            cache = json.load(file)
            latest_cache = cache[-1]
    except:
        cache = []
        latest_cache = {"title": ""}

    if post_title.lower() == latest_cache["title"].lower():
        print("No new post.")
    else:
        # Notify
        print("TITLE:", post_title)
        print("LINK:", post_link)

        notify_me(post_title, post_link, ico_img)

        # Save the post data
        latest_cache = {"title": post_title, "link": post_link, "img": post_img}
        cache.append(latest_cache)
        with open("cache.json", 'w') as file:
            json.dump(cache, file, indent=4)


if __name__ == "__main__":
    while True:
        notify_new_post()
        time.sleep(900)  # pause 15 minutes
        if os.path.exists("icon.ico"): os.remove("icon.ico")