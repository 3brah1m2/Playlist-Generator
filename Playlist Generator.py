from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/feed/trending')

time.sleep(5)

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)

video_elements = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
data = []

for video in video_elements:
    title = video.get_attribute('title')
    link = video.get_attribute('href')
    if title and link:
        title_lower = title.lower()
        if 'review' in title_lower:
            genre = 'Reviews'
        elif 'unboxing' in title_lower:
            genre = 'Unboxing'
        elif 'camera' in title_lower or 'photo' in title_lower:
            genre = 'Photography'
        elif 'gaming' in title_lower:
            genre = 'Gaming'
        else:
            genre = 'Other'
        tags = [word for word in title_lower.split() if len(word) > 3]
        data.append({'title': title, 'link': link, 'genre': genre, 'tags': tags})

playlist = {}
for item in data:
    genre = item['genre']
    if genre not in playlist:
        playlist[genre] = []
    playlist[genre].append(item)

genres = list(playlist.keys())
print('Genres:', genres)

for genre in genres:
    print(f'\n{genre} Playlist:')
    for video in playlist[genre]:
        print(f"Title: {video['title']}")
        print(f"Tags: {video['tags']}")
        print(f"Link: {video['link']}\n")

csv_file = 'YouTube_Playlist.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'link', 'genre', 'tags'])
    for item in data:
        writer.writerow([item['title'], item['link'], item['genre'], ', '.join(item['tags'])])

driver.quit()
