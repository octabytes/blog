import os
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

BASE_URL = "https://blog.elest.io"
OUTPUT_DIR = "./posts"
IMAGE_DIR = "./images"
SERVICE_DIR = "./services"
HEADERS = {"User-Agent": "Mozilla/5.0"}
PAGE_LIMIT = 9
ITEMS_PER_FILE = 20

# Create necessary directories
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# Load service data
service_data = {}
for file_name in os.listdir(SERVICE_DIR):
    if file_name.endswith(".json"):
        with open(os.path.join(SERVICE_DIR, file_name), "r") as f:
            data = json.load(f)
            for entry in data:
                service_data[entry["id"]] = entry

# Helper functions
def download_image(url, image_path):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded image: {image_path}")
    else:
        print(f"Failed to download image: {url}")

def find_service_id(title, tag):
    if ":" in title:
        possible_id = title.split(":")[0].lower()
    else:
        possible_id = tag.lower()

    possible_id.replace("'", "")
    possible_id.replace(" ", "-")
    
    # Check in service data
    for service_id, service in service_data.items():
        if service_id == possible_id or possible_id in service["id"]:
            return service_id
    return possible_id

# Main scraping function
def scrape_articles():
    articles = []
    file_index = 1

    for page_number in range(1, 2):
        print(f"Scraping page {page_number}...")
        url = f"{BASE_URL}/page/{page_number}/"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find article containers
        posts_feed = soup.select("#site-main > div > div .post-card")
        if not posts_feed:
            print(f"No articles found on page {page_number}")
            continue

        for article in posts_feed:
            # try:
                title = article.select_one(".post-card-title").text.strip()

                print(title)
                
                tag_element = article.select_one(".post-card-primary-tag")
                tag = tag_element.text.strip() if tag_element else ""
                description = article.select_one(".post-card-excerpt").text.strip()
                read_length = article.select_one(".post-card-meta-length").text.strip()
                link = article.select_one(".post-card-content-link")["href"]
                if not link.startswith(BASE_URL):
                    link = urljoin(BASE_URL, link)

                # Find matching service data
                service_id = find_service_id(title, tag)
                logo = service_data.get(service_id, {}).get("logo", "")
                category = service_data.get(service_id, {}).get("category", {})
                short_description = service_data.get(service_id, {}).get("description", "")

                # Extract image data
                image_tag = article.select_one(".post-card-image")
                srcset = image_tag["srcset"]
                alt = image_tag.get("alt", "")
                sizes = image_tag.get("sizes", "")

                # Prepare image folder structure: ./images/{id}/{timestamp}/
                timestamp = str(int(time.time()))
                image_dir = os.path.join(IMAGE_DIR, service_id or "unknown", timestamp)
                os.makedirs(image_dir, exist_ok=True)

                # Prepare image paths and download
                srcset_entries = []
                for entry in srcset.split(","):
                    image_url, size = entry.strip().split(" ")
                    image_url = urljoin(BASE_URL, image_url)
                    image_name = os.path.basename(image_url).replace("elestio-", "")
                    image_size = size.replace("w", "")
                    image_path = f"{image_dir}/{image_size}-{image_name}"
                    download_image(image_url, image_path)
                    srcset_entries.append({"size": size, "path": image_path})

                
                # Construct article entry
                article_entry = {
                    "id": service_id or "",
                    "tag": tag,
                    "title": title,
                    "logo": logo,
                    "category": category,
                    "short_description": short_description,
                    "link": link,
                    "description": description,
                    "read_length": read_length,
                    "image": {
                        "alt": alt,
                        "sizes": sizes,
                        "srcset": srcset_entries
                    }
                }

                articles.append(article_entry)

                # Save to JSON file every 20 items
                if len(articles) >= ITEMS_PER_FILE:
                    save_to_file(articles, file_index)
                    file_index += 1
                    articles = []

            # except Exception as e:
            #     print(f"Error processing article: {e}")

    # Save any remaining articles
    if articles:
        save_to_file(articles, file_index)

def save_to_file(articles, index):
    file_path = os.path.join(OUTPUT_DIR, f"{index}.json")
    with open(file_path, "w") as f:
        json.dump(articles, f, indent=4)
    print(f"Saved {len(articles)} articles to {file_path}")

if __name__ == "__main__":
    scrape_articles()
