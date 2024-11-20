import os
import re
import requests

def download_images(post_name):
    post_name = post_name.replace("content/posts/", "")
    post_name = post_name.replace("/index.md", "")

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

    # Download each image and replace URLs in the Markdown content
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

            # Replace the URL in the Markdown content
            local_image_path = f"images/{image_name}"
            content = content.replace(url, local_image_path)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Write the updated content back to the Markdown file
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write(content)

    print("Markdown file updated successfully.")


posts = ["content/posts/getting started/building-a-bi-dashboard-with-metabase/index.md",
         "content/posts/getting started/building-a-customer-support-dashboard-with-baserow/index.md",
         "content/posts/getting started/how-to-build-a-telegram-ai-bot-with-n8n/index.md",
         "content/posts/grafana/create-users-and-teams/index.md",
         "content/posts/grafana/grafana-create-mysql-data-source/index.md",
         "content/posts/grafana/grafana-install-prometheus-dashboard/index.md",
         "content/posts/grafana/grafana-integrating-alert-with-email-and-slack-2/index.md",
         "content/posts/immudb & minio/immudb-s3-bucket-minio/index.md",
         "content/posts/keycloak/keycloack-cluster-with-elestio/index.md",
         "content/posts/keycloak session configuration/configure-keycloak-with-saml/index.md",
         "content/posts/keycloak token management/keycloak-token-management-expiration-revocation-and-renewal/index.md",
         "content/posts/logto/how-to-customise-your-keycloak-ui-with-react-keycloakify/index.md",
         "content/posts/logto/how-to-expose-meetrics-endpoint-from-keycloak/index.md",
         "content/posts/logto/publish-keycloak-events-to-rabbitmq/index.md",
         "content/posts/logto/setup-sso-with-keycloak-and-multiple-services-2/index.md",
         "content/posts/mastodon/scaling-up-down-mastodon/index.md",
         "content/posts/migration/migrate-jenkins-pipeline-to-elestio/index.md",
         "content/posts/migration/migrate-mastodon-server-to-elestio/index.md",
         "content/posts/migration/migrate-mysql-database-to-elestio/index.md",
         "content/posts/migration/migrate-superset-to-elestio/index.md",
         "content/posts/migration/migrate-wordpress-to-elestio/index.md",
         "content/posts/minio/minio-cloud-agnostic-object-storage/index.md",
         "content/posts/moodle/moodle-free-open-source-learning-management-system-lms/index.md",
         "content/posts/mysql/easy-mysql-database-migration-with-elestio-a-step-by-step-guide/index.md",
         "content/posts/n8n/how-to-clean-up-n8n-database/index.md",
         "content/posts/n8n/how-to-install-a-community-node-on-n8n/index.md",
         "content/posts/n8n/n8n/index.md",
         "content/posts/n8n/n8n-api-endpoint-for-get-response/index.md",
         "content/posts/n8n/n8n-generating-pdfs-with-n8n-using-gotenberg/index.md",
         "content/posts/n8n/n8n-retrieves-weather-information-based-on-a-zip-code/index.md",
         "content/posts/softwares/uptime-kuma/index.md",
         "content/posts/softwares/vaultwarden-migrate-to-vaultwarden/index.md",
         "content/posts/superset/connecting-apache-superset-to-popular-databases/index.md",
         "content/posts/superset/how-to-build-a-marketing-campaign-dashboard-in-superset/index.md",
         "content/posts/superset/how-to-install-prophet-in-superset/index.md",
         "content/posts/superset/how-to-secure-apache-superset-with-saml/index.md",
         "content/posts/superset/superset-creating-your-first-dashboard-2/index.md",
         "content/posts/superset/using-superset-for-real-time-data-analytics/index.md",
         "content/posts/typebot/typebot-addressing-problem-1-ineffective-customer-support/index.md"]

for post in posts:
    download_images(post)