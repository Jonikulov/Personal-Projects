import os
import requests
import bs4
import time
import threading

os.makedirs("xkcd1", exist_ok=True)
os.makedirs("xkcd2", exist_ok=True)
url = 'https://xkcd.com/'

def download_xkcd_1(start_url, end_url):
    for url_num in range(start_url, end_url):
        res = requests.get(url + str(url_num))
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text, features='lxml')
            comic = soup.select('#comic img')
            if comic != []:
                img_link = 'https:' + comic[0].get('src')
                print(f'{url_num}. Downloading image: {img_link}')
                # requests.get(img_link)
                img = requests.get(img_link)
                if img.status_code == 200:
                    with open(os.path.join('xkcd1', os.path.basename(img_link)),
                              'wb') as file:
                        file.write(img.content)


def download_xkcd_2(start_url, end_url):
    for url_num in range(start_url, end_url):
        res = requests.get(url + str(url_num))
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text, features='lxml')
            comic = soup.select('#comic img')
            if comic != []:
                img_link = 'https:' + comic[0].get('src')
                print(f'{url_num}. Downloading image: {img_link}')
                # requests.get(img_link)
                img = requests.get(img_link)
                if img.status_code == 200:
                    with open(os.path.join('xkcd2', os.path.basename(img_link)),
                              'wb') as file:
                        file.write(img.content)


def download_xkcd_3(t_range):
    for url_num in t_range:
        res = requests.get(url + str(url_num))
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text, features='lxml')
            comic = soup.select('#comic img')
            if comic != []:
                img_link = 'https:' + comic[0].get('src')
                print(f'{url_num}: Downloading image: {img_link}')
                # requests.get(img_link)
                img = requests.get(img_link)
                if img.status_code == 200:
                    with open(os.path.join('xkcd2', os.path.basename(img_link)),
                                'wb') as file:
                        file.write(img.content)


start_time = time.time()
# download_xkcd_1(1, 11)
exec_time = time.time() - start_time
print("\nSequential execution time:", exec_time)

print("#" * 70)

start_time = time.time()

# download_threads = []
# for t in range(1, 1001, 10):
#     dt = threading.Thread(target=download_xkcd_2, args=[t, t+10])
#     dt.start()
#     download_threads.append(dt)

# for t in download_threads:
#     t.join()

num_threads = 4
num_rows = 31  # 341
thread_chunk = num_rows // num_threads
remainder = num_rows % num_threads

start = 0
thread_ranges = []
for i in range(num_threads):
    end = start + thread_chunk + (1 if i < remainder else 0)
    thread_ranges.append(range(start, end))
    start = end

threads = []
for t_range in thread_ranges:
    t = threading.Thread(target=download_xkcd_3, args=[t_range])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

exec_time = time.time() - start_time
print("\nParallel execution time:", exec_time)

print('num_threads:', num_threads)
print('num_rows:', num_rows)
print('thread_chunk:', thread_chunk)
print('thread_ranges:', thread_ranges)