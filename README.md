# YouTube Trending Playlist Scraper

This Python script uses Selenium to scrape video titles, links, genres, and tags from YouTube's Trending page. It categorizes the videos into genre-based playlists and exports the data to a CSV file.

## Features

- Extracts video title and link from the YouTube Trending page
- Automatically assigns a genre based on keywords in the title
- Generates basic tags from title words
- Categorizes videos by genre
- Saves data in a `YouTube_Playlist.csv` file

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (ensure it's compatible with your Chrome version)
- Selenium

## Installation

1. Clone the repository or download the script.
2. Install Selenium:

```bash
pip install selenium
