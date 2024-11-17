---
draft: true
title: "Migrate MySQL Database to Elestio"
date: "2024-08-19"
description: "This migration document focuses on the migration of the applications supported by Elestio. Find the software list here

This document provides a step-by-step guide for migrating your existing MySQL database system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process,"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate MySQL Database to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by Elestio. Find the software list [here](https://elest.io/fully-managed-services?ref=blog.elest.io)

This document provides a step\-by\-step guide for migrating your existing MySQL database system to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Create an account on [Elestio](https://elest.io/?ref=blog.elest.io)
2. Log in to your MySQL admin dashboard account where your current site/pages are hosted
3. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail

### 2️⃣ Exporting the Data

1. Head over to your Phpmyadmin UI with Admin credentials and make sure you are logged in and can see your database, table, and data
2. For this example, we are going to migrate the Library Management database that has 2 tables: Books and Library

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/HHoimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/HHoimage.png?ref=blog.elest.io)3. This is the dummy data under the Books table to verify the migration

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/vopimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/vopimage.png?ref=blog.elest.io)4. Here, you can choose to migrate/export specific tables or entire databases. For this tutorial, I am going to export the entire database with all the tables
5. For this, click on your database so it shows the list of all the tables like below, and head over to the "Export" option from the above option panel

[![Screenshot 2023-11-13 at 12.33.47 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-13-at-12-33-47-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/HHoimage.png?ref=blog.elest.io)6. You can use the "Quick" Option like below or go to custom and tweak the setting for exports as you need

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/ebLimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/ebLimage.png?ref=blog.elest.io)7. Click on "Export" and save the file to your local machine. The file being downloaded will have `.sql` extension because we have selected the format as SQL from above. Feel free to change the format if required.
8. With this, your database is exported

### 3️⃣ Importing the Data

1. Login to your Elestio account
2. Go to Create Services and select "MySQL"
3. Select your service provider, region, and machine preferences

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/Bnpimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/Bnpimage.png?ref=blog.elest.io)4. Name your service, configurations, and support layer, and hit "Create Service"

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/SHqimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/SHqimage.png?ref=blog.elest.io)5. Once running, head over to the service and use the credentials provided under "Admin UI" to access the PhpMyAdmin UI

[![Screenshot 2023-11-13 at 12.47.14 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-13-at-12-47-14-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/M6Cimage.png?ref=blog.elest.io)6. Once you are in, head over to the UI you should go ahead and create your database. We will be creating a database with Name Migrated Library to see the difference after the migration

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/KHyimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/KHyimage.png?ref=blog.elest.io)7. Click on the database head over to the "Import" option from the top option bar, and choose the file from your local machine that you downloaded from the previous step.

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/OKbimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/OKbimage.png?ref=blog.elest.io)8. Remember that if you used the custom settings in the import section then you might want to change the options from the default while importing too, else it will raise an error
9. After uploading the essential .SQL file, scroll down and click on "Import"
10. The tables and data will get imported and can be seen under the database we created on Elestio instance

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/SAgimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/SAgimage.png?ref=blog.elest.io)Voila 🎉 you have successfully imported your tables and data to your new instance of MySQL.

### 4️⃣ Testing the Migration

1. You have successfully migrated to Elestio, now it's time for testing if your application is running as you intended
2. Head over to the tables and check if you can still see the data like your previous instance
3. Here as you can see, my new database has successfully imported the tables and the data as I showed during the import

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/t71image.png)](https://docs.elest.io/uploads/images/gallery/2023-11/t71image.png?ref=blog.elest.io)### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-mysql-database-to-elestio?ref=blog.elest.io)*on November 13, 2023\.*



