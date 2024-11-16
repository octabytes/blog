import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import markdownify
from tqdm import tqdm

# Define paths
POSTS_DIR = "./posts"
IMAGES_DIR = "./single-post-images"
OUTPUT_DIR = "./single-post"

# Create necessary directories
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_image(image_url, save_path):
    """Download image from URL and save it to specified path."""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded image: {save_path}")
        else:
            print(f"Failed to download image: {image_url}")
    except Exception as e:
        print(f"Error downloading image {image_url}: {e}")

def process_images(soup, post_id):
    """Download images from srcset and update image paths in the HTML content."""
    images = soup.select("img")
    for img in images:
        srcset = img.get("srcset")
        if srcset:
            srcset_urls = [url.split()[0] for url in srcset.split(",")]
            for image_url in srcset_urls:
                image_name = os.path.basename(urlparse(image_url).path)
                save_dir = os.path.join(IMAGES_DIR, post_id)
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, image_name)
                download_image(image_url, save_path)

                # Update img src in HTML
                img["src"] = f"../single-post-images/{post_id}/{image_name}"
    return soup

def get_last_part_of_link(link):
    """Extract the last part of the URL path for the filename."""
    last_part = link.replace("https://blog.elest.io/", "")
    last_part = last_part.replace("/", "")
    return last_part

def fetch_and_convert(post):
    """Fetch content from the link, download images, and convert to markdown."""
    post_id = post["id"]
    link = post["link"]

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

        # Process images and update their paths
        content_container = process_images(content_container, post_id)

        # Convert HTML content to Markdown
        markdown_content = markdownify.markdownify(str(content_container), heading_style="ATX")

        # Get the last part of the link for the filename
        filename = get_last_part_of_link(link)
        output_dir = os.path.join(OUTPUT_DIR, post_id)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{filename}.md")

        # Save Markdown file
        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
            print(f"Markdown saved: {output_path}")

    except Exception as e:
        print(f"Error processing link {link}: {e}")

def main():
    # Get list of all JSON files in POSTS_DIR
    json_files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".json")]

    for json_file in tqdm(json_files, desc="Processing JSON files"):
        json_path = os.path.join(POSTS_DIR, json_file)

        with open(json_path, "r", encoding="utf-8") as f:
            posts = json.load(f)

            for post in tqdm(posts, desc="Processing Posts", leave=False):
                fetch_and_convert(post)

if __name__ == "__main__":
    main()
