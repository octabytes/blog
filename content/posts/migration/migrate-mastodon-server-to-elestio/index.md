---
draft: true
title: "Migrate Mastodon server to Elestio"
date: "2024-04-01"
description: "This migration document focuses on the migration of the applications supported by Elestio. Find the software list here

This document provides a step-by-step guide for migrating your existing Mastodon database system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process,"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate Mastodon server to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by Elestio. Find the software list [here](https://elest.io/fully-managed-services?ref=blog.elest.io)

This document provides a step\-by\-step guide for migrating your existing Mastodon database system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Create an account on [Elestio](https://elest.io/?ref=blog.elest.io)
2. Log in to your Mastodon admin dashboard account where your current server is hosted
3. Ensure the UI for the application is working fine and no critical errors are detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Exporting the Data

1. Log into your Mastodon server that has been originally hosted.
2. Head over to the preferences settings

![](https://i.imgur.com/bzt53zf.png)3. Head over to the "Import and Export" and click on the Data Export option

![](https://i.imgur.com/jcQ7CfP.png)4. Click on the "CSV" file section to download the data you want to migrate. The CSV files will be stored in your local machines

![](https://imgur.com/2jv7con.png)
> For exporting the additional data you should export the underlying Postgres database and also your media storage.

### 3️⃣ Importing the Data

1. Login to your Elestio account
2. Go to Create Services and select "Mastodon"
3. Select your service provider, region, and machine preferences

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/7UXimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/7UXimage.png?ref=blog.elest.io)4. Name your service, configurations, and support layer, and hit "Create Service"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/qIJimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/qIJimage.png?ref=blog.elest.io)5. Once deployed, head over to the service details URL provided under "Admin UI" to access the Mastodon Server UI

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/qakimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/qakimage.png?ref=blog.elest.io)6. Once you are in, head over to the UI you should head over and log in with the credentials on the server.

![](https://i.imgur.com/bzt53zf.png)7. Head over to the "Import and Export" and click on the import

![](https://i.imgur.com/FDRKR5r.png)8. Now click the "Choose file" option under the data section and the "Import type" from the drop\-down menu. Select the file according to the import type you have selected.
9. Confirm your imports by clicking on the confirm button

![](https://i.imgur.com/crMpWQm.png)
> If you imported the Postgres database in the previous step then make sure to import the database in the Elestio instance by using the Postgres credentials provided on the Elestio dashboard and also import the media storage.

10. Woohoo! Your data is successfully migrated to Elestio, wait for a couple of minutes for the data to be imported. You can check the progress for the same on the same tab

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/cbfimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/cbfimage.png?ref=blog.elest.io)### 4️⃣ Testing the Migration

1. You have successfully migrated to Elestio, now it's time for testing if your application is running as you intended
2. Head over to the Mastodon server and check the bookmarks, posts, and list you have imported in their respective tabs and you will notice the mention of your previous server to set the differentiations
3. Here as you can see, my bookmarks were successfully imported into the new instance of Elestio

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/76Oimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/76Oimage.png?ref=blog.elest.io)### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-mastodon-server-to-elestio?ref=blog.elest.io)*on November 25, 2023\.*



