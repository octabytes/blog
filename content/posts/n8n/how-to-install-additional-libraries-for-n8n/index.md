---
draft: true
title: "How to install additional libraries on N8N"
date: "2024-07-06"
description: "n8n is a popular open-source workflow automation tool that allows you to automate repetitive tasks and create custom workflows. However, sometimes you may need to install additional libraries to enhance its functionality. In this article, we'll walk you through the steps of how to install additional libraries for"
tags: []
categories: [Automation]
cover:
  image: images/cover.png
  caption: "How to install additional libraries on N8N"
ShowToc: true
TocOpen: true
---


[n8n](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io) is a popular open\-source workflow automation tool that allows you to automate repetitive tasks and create custom workflows. However, sometimes you may need to install additional libraries to enhance its functionality. In this article, we'll walk you through the steps of how to install additional libraries for n8n using the command line interface (CLI).

### Step 1: Add an Environment Variable

The first step is to add an environment variable. You can do this in the .env file in Visual Studio Code (VSCode) or from the OctaByte Dashboard \> Update config button. The environment variable you need to add is `NODE_FUNCTION_ALLOW_EXTERNAL=*`. This allows you to install additional libraries to n8n.

### Step 2: Create a Dockerfile

Next, in VSCode, create a file named `Dockerfile` (capital "D" is important) in the `/opt/app/` directory, near the `docker-compose.yml` file. The contents of the file should be as follows:


```
FROM n8nio/n8n:latest
USER root
RUN npm install -g bcrypt body-parser fcm-push
USER node

```

These two lines specify the base image and the additional libraries you want to install. In this case, we're installing the `bcrypt`, `body-parser`, and `fcm-push` libraries.

### Step 3: Modify the Docker Compose File

Next, modify the `docker-compose.yml` file by disabling the default image and instead using the build process. Your `docker-compose.yml` file should look like this:


```
# image: n8nio/n8n:${SOFTWARE_VERSION_TAG}
build:
  context: .

```

### Step 4: Run the Command

Finally, run the following command in the terminal to build and run the custom image:


```
cd /opt/app;
docker-compose down;
docker-compose build;
docker-compose up -d;

```

If you need to install more packages in the future, simply repeat Steps 2 and 4 to rebuild your custom image.

### Step 5: Update the Auto Update Script

To automatically rebuild the image when n8n releases an update, run the following command in the terminal:


```
sed -i 's/--debug;/--debug;\ncd \/opt\/app;\nsource .env;\ndocker-compose pull;\ndocker-compose up -d --build;/' /opt/elestio/watchtower/watchtower-upgrade.sh

```

In conclusion, installing additional libraries for n8n is a straightforward process that involves adding an environment variable, creating a Dockerfile, modifying the Docker Compose file, and running a few commands. With these steps, you'll be able to enhance the functionality of n8n and automate even more tasks with ease.

If you don't want to worry about maintenance .... of your N8N server... [deploy N8N on elest.io](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io) and get automated backups, reverse proxy with SSL termination, DOS protection, firewall, automated OS \& Software updates (So your instance of N8N stays always up to date), and a team of Linux experts and open source enthusiasts to ensure your services are always safe, UP and running.

Click on the button below to get a fully managed instance of N8N ready to use in less than 3 minutes. 

[Deploy N8N](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io)

