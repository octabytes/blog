---
draft: true
title: "Adding Persistent Themes to Keycloak"
date: "2024-12-08"
description: "We will see how you can add persistent theme to Keycloak. Before we start, make sure you have deployed Keycloak, we will be self-hosting it on OctaByte. Keycloak offers robust theme support for its web pages and emails, allowing you to tailor the look and feel of end-user-facing pages to"
tags: []
categories: [Identity and access management]
cover:
  image: images/cover.png
  caption: "Adding Persistent Themes to Keycloak"
ShowToc: true
TocOpen: true
---


We will see how you can add persistent theme to [Keycloak](https://octabyte.io/open-source/keycloak?ref=blog.octabyte.io). Before we start, make sure you have deployed Keycloak, we will be self\-hosting it on [OctaByte](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io). Keycloak offers robust theme support for its web pages and emails, allowing you to tailor the look and feel of end\-user\-facing pages to seamlessly integrate with your applications.

### Persistent Themes

Keycloak supports mounting themes from a persistent volume, making it easier to manage themes across deployments. By default, the volume mount for themes is at `/opt/keycloack/themes`. Here’s how to configure it:

1. Access your Keycloak service on [OctaByte Dashboard](https://dash.elest.io/8766/break-and-build/?ref=blog.octabyte.io).
2. Navigate to **Service Overview**.
3. Click the **UPDATE CONFIG** button.
4. Add the following configuration to the Keycloak container:


```
volumes:
   - ./themes:/opt/keycloak/themes

```
1. Click **Apply \& Restart**.

You can copy your theme to the `/opt/app/themes` directory using various methods, such as:

* Using the file explorer available in the service dashboard.
* Utilizing VSCode in the browser (available in the tools tab of the service overview).
* Using SFTP over SSH.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [Keycloak documentation](https://www.keycloak.org/documentation?ref=blog.octabyte.io) to learn more about Keycloak. Click the button below to create your service on [OctaByte](https://octabyte.io/open-source/keycloak?ref=blog.octabyte.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io)

