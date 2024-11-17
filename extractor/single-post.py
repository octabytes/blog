import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import markdownify
import random
from datetime import datetime

# Define paths
POSTS_DIR = "./posts"
IMAGES_DIR = "../content/posts"
CATEGORIES_DIR = "./categories"
OUTPUT_DIR = "../content/posts"

# Create necessary directories
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load categories into a dictionary for quick lookup
def load_categories():
    categories = {}
    for filename in os.listdir(CATEGORIES_DIR):
        if filename.endswith(".json"):
            category_path = os.path.join(CATEGORIES_DIR, filename)
            with open(category_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    categories[item["id"]] = item["name"]
    return categories

categories_dict = load_categories()

def download_high_res_image(srcset, post_id, post_name):
    """Download only the highest resolution image from srcset."""
    try:
        # Get the highest resolution image (last one in the srcset)
        srcset_urls = [url.split()[0] for url in srcset.split(",")]
        high_res_url = srcset_urls[-1]
        image_name = os.path.basename(urlparse(high_res_url).path)
        save_dir = os.path.join(IMAGES_DIR, post_id, post_name, "images")
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, image_name)

        print(f"Downloading high-resolution image: {high_res_url}")
        response = requests.get(high_res_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Saved image to: {save_path}")
            return f"images/{image_name}"
        else:
            print(f"Failed to download image: {high_res_url}")
    except Exception as e:
        print(f"Error downloading image {high_res_url}: {e}")
    return ""

def get_post_name(link):
    """Extract the post name from the link."""
    return link.replace("https://blog.elest.io", "").replace("/", "-").strip("-")

def get_random_date():
    """Generate a random date in 2024."""
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d")

def get_category_names(category_ids):
    """Fetch category names using category IDs."""
    return [categories_dict.get(cat_id, "Other") for cat_id in category_ids]

def fetch_and_convert(post):
    """Fetch content from the link, download the high-res image, and convert to markdown."""
    post_id = post["id"]
    link = post["link"]
    post_name = get_post_name(link)
    title = post["title"]
    title = title.replace('"', "'")
    description = post["description"]
    description = description.replace('"', "'")
    category_ids = post.get("category", {}).get("ids", ["other"])
    category_names = get_category_names(category_ids)
    cover_caption = post["image"].get("alt", "")
    cover_caption = cover_caption.replace('"', "'")

    print(f"Fetching content for link: {link}")

    try:
        response = requests.get(link)
        if response.status_code != 200:
            print(f"Failed to fetch content for link: {link}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        content_container = soup.select_one("#site-main > article > section")

        if not content_container:
            print(f"Content container not found for link: {link}")
            return

        # Process the high-res image and update its path
        img_tag = content_container.find("img")
        if img_tag and img_tag.get("srcset"):
            image_path = download_high_res_image(img_tag["srcset"], post_id, post_name)
            img_tag["src"] = image_path

        # Convert HTML content to Markdown
        markdown_content = markdownify.markdownify(str(content_container), heading_style="ATX")

        # YAML front matter
        yaml_content = f"""---
draft: true
title: "{title}"
date: "{get_random_date()}"
description: "{description}"
tags: []
categories: [{', '.join(category_names)}]
cover:
  image: images/cover.png
  caption: "{cover_caption}"
ShowToc: true
TocOpen: true
---

{markdown_content}
"""

        # Save Markdown file
        output_dir = os.path.join(OUTPUT_DIR, post_id, post_name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "index.md")

        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(yaml_content)
            print(f"Markdown saved: {output_path}")

    except Exception as e:
        print(f"Error processing link {link}: {e}")

def main():
    # Get list of all JSON files in POSTS_DIR
    json_files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".json")]

    for json_file in json_files:
        json_path = os.path.join(POSTS_DIR, json_file)

        with open(json_path, "r", encoding="utf-8") as f:
            posts = json.load(f)

            for post in posts:
                fetch_and_convert(post)

if __name__ == "__main__":
    main()
