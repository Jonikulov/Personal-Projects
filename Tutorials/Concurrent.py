import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--ignore-certificate-errors") 
opts.add_argument("--allow-insecure-localhost")
# opts.add_argument("--start-maximized")

def do_task(click_range):
    driver = webdriver.Chrome(options=opts)
    # driver.maximize_window()

    driver.get("https://xkcd.com/1002/")

    main_win = driver.current_window_handle
    for i in click_range:

        driver.switch_to.window(main_win)
        print(f'{i}: {driver.title}')
        next = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="middleContainer"]/ul[1]/li[4]/a')
        ))
        next.click()

        link_url = "https://google.com"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(link_url)

        input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        input.send_keys("Hello, World!", Keys.ENTER)
        time.sleep(2)
        driver.close()

    # print(driver.current_window_handle)
    # driver.switch_to.window()

    # driver.close()
    driver.quit()


num_threads = 5  # 4 5 6 7 8
num_rows = 31  # 31
thread_chunk = num_rows // num_threads
remainder = num_rows % num_threads

start = 0
thread_ranges = []
for i in range(num_threads):
    end = start + thread_chunk + (1 if i < remainder else 0)
    thread_ranges.append(range(start, end))
    start = end

start_time = time.time()
# for t_range in thread_ranges:
#     do_task(t_range)
exec_time = time.time() - start_time
print("\nSequential execution time:", exec_time)

print("#" * 70)

start_time = time.time()
threads = []

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(do_task, thread_ranges)

exec_time = time.time() - start_time
print("\nParallel execution time:", exec_time)

print('num_threads:', num_threads)
print('num_rows:', num_rows)
print('thread_chunk:', thread_chunk)
print('thread_ranges:', thread_ranges)

# 31, 8 threads -> 34 seconds
# 31, 7 threads -> 38.7 seconds
# 31, 6 threads -> 39.5 seconds
# 31, 5 threads -> 43 seconds
# 31, 4 threads -> 44.5 seconds