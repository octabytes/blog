---
draft: true
title: "Migrate Wordpress to Elestio"
date: "2024-01-24"
description: "This migration document focuses on the migration of the applications supported by Elestio. Find the software list here

This document provides a step-by-step guide for migrating your existing system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate Wordpress to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by Elestio. Find the software list [here](https://elest.io/fully-managed-services?ref=blog.elest.io)

This document provides a step\-by\-step guide for migrating your existing system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Create an account on [Elestio](https://elest.io/?ref=blog.elest.io)
2. Log in to your WordPress account where your current site/pages are hosted
3. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Exporting the Data

There are two primary ways to export your data from Wordpress, we will focus on the native one but you can consider using plugins like WPvivid to carry out the migration.

* Here we are going to migrate a simple kangaroo site with 2 pages as you can see in the image below

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/image.png?ref=blog.elest.io)* Head over to the dashboard of your WordPress go to the "Tools" option in the left panel and select the "Export" option

[![Screenshot 2023-11-08 at 5.28.23 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-08-at-5-28-23-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-08-at-5-28-23-pm.png?ref=blog.elest.io)* Click on "Download Export Files" as shown in the image above, here we are exporting all content but you can choose to export selectively if you want.
* The exported file will be saved on your local machine. The exported file will be in XML format.
* You can additionally make a copy of this exported data and store it as a backup on local disks. This is totally optional step if you want additional backup than what WordPress natively offers.

### 3️⃣ Setup Elestio

* Head over to the Elestio Dashboard and search for WordPress service

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/i98image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/i98image.png?ref=blog.elest.io)* Select the service and head over to the service provider, region and service plan. If you have no preferences, simply hit the next

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/vX3image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/vX3image.png?ref=blog.elest.io)* Name the service as you want and click "Create Service"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/46Fimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/46Fimage.png?ref=blog.elest.io)* Head over to this service, and head over to the link provided under the Admin UI button

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/tWZimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/tWZimage.png?ref=blog.elest.io)* Create your site with the details provided here and log in to the WordPress instance. You will see a similar dashboard below

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/dX1image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/dX1image.png?ref=blog.elest.io)### 3️⃣ Importing the Data

* Head over to the new instance of WordPress head over to "Tools" and click on the "Import" option.

[![Screenshot 2023-11-08 at 7.13.05 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-08-at-7-13-05-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-08-at-7-13-05-pm.png?ref=blog.elest.io)* Click on "Install Now" for WordPress as shown in the image above.
* Run importer after getting installed

[![Screenshot 2023-11-08 at 7.21.52 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-08-at-7-21-52-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-08-at-7-21-52-pm.png?ref=blog.elest.io)* Choose the XML file you exported from the previous step. and click on "Upload file and Import"

[![Screenshot 2023-11-08 at 7.26.23 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-08-at-7-26-23-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-08-at-7-26-23-pm.png?ref=blog.elest.io)* Fill out the author information and click on "Submit"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/JM4image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/JM4image.png?ref=blog.elest.io)* Voila! It's imported and your site is migrated safely. You can check if it's working from the options above.

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/LM7image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/LM7image.png?ref=blog.elest.io)### 4️⃣ Testing the Migration

* Go to the top left of the screen where you can see the site name, in this case, "Migrate to this". Upon clicking on the name, you should see the site as it was before the migration.

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/hHYimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/hHYimage.png?ref=blog.elest.io)* Enjoy your newly migrated WordPress site on Elestio 🎉

### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-wordpress-to-elestio?ref=blog.elest.io)*on November 9, 2023\.*



