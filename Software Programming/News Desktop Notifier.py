"""
    Desktop Notifier
Gives notification on desktop if there's a new post on the website,
main title of the post is displayed in the notification.

- https://beautiful-soup-4.readthedocs.io/en/
- https://versa-syahptr.github.io/winotify/docs/

"""

import os
import json
import time
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from winotify import Notification, audio


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
        ico_img = "D:\GitHub\Personal-Projects\Software Programming\icon.png"
        # Converts an image from a URL to ICO format and saves it.
        Image.open(BytesIO(requests.get(post_img).content)).save(ico_img)
    else:
        post_img = None
        ico_img = ""

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

        toast = Notification(app_id="KUN.UZ yangiliklari",
                             title=post_title,
                            #  msg="There's a message for you!",
                             duration="short",
                             icon=ico_img)
        toast.set_audio(audio.SMS, loop=False)
        toast.add_actions(label="Batafsil ko'rish", launch=post_link)
        toast.show()

        # Save the post data
        latest_cache = {"title": post_title, "link": post_link,
                        "img": post_img}
        cache.append(latest_cache)
        with open("cache.json", 'w') as file:
            json.dump(cache, file, indent=4)


if __name__ == "__main__":
    while True:
        notify_new_post()
        time.sleep(3)  # pause 15 minutes
        if os.path.exists("icon.png"):
            os.remove("icon.png")
