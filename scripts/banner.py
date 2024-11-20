from PIL import Image

post_name = "content/posts/typebot/typebot-addressing-problem-1-ineffective-customer-support/images/cover.png"

post_name = post_name.replace("content/posts/", "")
post_name = post_name.replace("/images/cover.png", "")
post_name = post_name.replace("/images/cover.jpg", "")

# Paths to images
banner_path = "../static/images/octabyte-banner.png"
cover_path = f"../content/posts/{post_name}/images/cover.png"
output_path = f"../content/posts/{post_name}/images/cover.png"

# Open images
cover_image = Image.open(cover_path)
banner_image = Image.open(banner_path)

# Get dimensions of the images
cover_width, cover_height = cover_image.size
banner_width, banner_height = banner_image.size

# Calculate position for the banner
# Left side, a little above the bottom
x_position = 40  # Left side
y_position = cover_height - banner_height - 40  # 10 pixels above the bottom

# Ensure the banner fits within the cover image (optional resizing)
if banner_width > cover_width:
    banner_image = banner_image.resize((cover_width, int(banner_height * cover_width / banner_width)))
    banner_width, banner_height = banner_image.size

# Paste the banner onto the cover image
cover_image.paste(banner_image, (x_position, y_position), banner_image if banner_image.mode == 'RGBA' else None)

# Save the resulting image
cover_image.save(output_path)

print(f"Image saved with the banner at: {output_path}")
