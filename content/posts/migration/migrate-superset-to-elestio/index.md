---
draft: true
title: "Migrate Superset to Elestio"
date: "2024-04-27"
description: "This migration document focuses on the migration of the applications supported by Elestio. Find the software list here

This document provides a step-by-step guide for migrating your existing Superset pipelines to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate Superset to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by Elestio. Find the software list [here](https://elest.io/fully-managed-services?ref=blog.elest.io)

This document provides a step\-by\-step guide for migrating your existing Superset pipelines to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Create an account on [Elestio](https://elest.io/?ref=blog.elest.io)
2. Log in to your Superset admin dashboard account on the server where your current Superset is deployed
3. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Exporting the Dashboards and Data

1. Head over to your original (source) dashboard of superset
2. Select all the dashboards you are planning on migrating and click on Export

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/NOnimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/NOnimage.png?ref=blog.elest.io)3. Similarly, head over to the charts section, select all the required charts, and click on Export

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/TU9image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/TU9image.png?ref=blog.elest.io)1. These exported files will be stored in your local machine in .zip format
2. You will have to reconfigure your connected database with Superset after the migration so you should make sure you have all the information required for configuration
3. If you have a database connected with the Superset then head over to [Elestio's Migration Docs](https://docs.elest.io/books/migrations?ref=blog.elest.io) similar to this for migration instructions for the specific database


> If you want to migrate the database to seamless integration with the Superset then head over to [Elestio's Migration Docs](https://docs.elest.io/books/migrations?ref=blog.elest.io) similar to this for migration instructions for the specific databases.

### 3️⃣ Importing the Dashboards and Data

1. Login to your Elestio account
2. Go to Create Services and select "Superset"
3. Select service provider, region, and service information

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/SA7image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/SA7image.png?ref=blog.elest.io)4. Name your service, configurations, and support layer, and hit "Create Service"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/hROimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/hROimage.png?ref=blog.elest.io)5. Once deployed, head over to the service details and use the credentials provided under "Admin UI" to access the Superset dashboard.

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/tz6image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/tz6image.png?ref=blog.elest.io)6. Once logged in, head over to the dashboard tab and click on the import button as shown in the image

[![Screenshot 2023-11-22 at 9.09.30 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-22-at-9-09-30-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-22-at-9-09-30-pm.png?ref=blog.elest.io)7. Click on "Select File" select the export (.zip) you exported from the previous step and click on "Import"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/asCimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/asCimage.png?ref=blog.elest.io)8. Additionally, you can add and configure your databases from the settings shown in the image below

[![Screenshot 2023-11-22 at 10.00.10 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-22-at-10-00-10-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-22-at-10-00-10-pm.png?ref=blog.elest.io)Woohoo 🎉 you have successfully imported all your dashboards and repeat the same to import the charts.

### 4️⃣ Testing the Migration

1. You have successfully migrated to Elestio, now it's time for testing if your application is running as you intended
2. Head over to the Dashboard and check if you can still see the dashboards like your previous instance
3. Here as you can see, my new dashboards have successfully been imported  as I showed during the import

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/fEcimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/fEcimage.png?ref=blog.elest.io)### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-superset-to-elestio?ref=blog.elest.io)*on November 22, 2023\.*



