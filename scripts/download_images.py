import os
import re
import requests

post_name = "directus/importing-existing-projects-into-directus"

# Paths
markdown_file = f"../content/posts/{post_name}/index.md"
images_dir = f"../content/posts/{post_name}/images"

# Regular expression to match image URLs in Markdown
image_url_pattern = r"!\[.*?\]\((https?://[^\s]+)\)"

# Ensure the images directory exists
os.makedirs(images_dir, exist_ok=True)

# Read the Markdown file
with open(markdown_file, "r", encoding="utf-8") as file:
    content = file.read()

# Find all image URLs
image_urls = re.findall(image_url_pattern, content)

# Download each image
for url in image_urls:
    try:
        # Get the filename from the URL
        image_name = os.path.basename(url)
        image_path = os.path.join(images_dir, image_name)

        # Download the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Save the image
        with open(image_path, "wb") as image_file:
            for chunk in response.iter_content(1024):
                image_file.write(chunk)

        print(f"Downloaded: {image_name}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
