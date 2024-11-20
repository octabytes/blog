---
draft: false
title: "Connecting Apache Superset to Popular Databases"
date: "2024-11-20"
description: "This guide walks users through connecting a PostgreSQL database to Apache Superset on OctaByte, setting it up for data analysis and creating visualizations. It includes step-by-step instructions on configuring database connections and using Superset’s features."
tags: ["Apache Superset", "PostgreSQL", "Database Connection", "Data Analysis", "Visualization", "OctaByte", "Business Intelligence"]
categories: [Applications, Business Intelligence]
cover:
  image: images/cover.png
  caption: "Connecting Apache Superset to Popular Databases"
  relative: true
ShowToc: true
TocOpen: true
---


This guide is for users running an instance of [Apache Superset](https://octabyte.io/applications/business-intelligence/superset) looking to explore and analyze data. In this tutorial, we’ll walk you through how to connect Superset to a new database, set it up for data analysis, and create visualizations. This step\-by\-step guide will help you get hands\-on experience with Superset’s features for data exploration.

## Connecting Database

For this tutorial, we will connect [PostgreSQL](https://octabyte.io/open-source/postgresql?ref=blog.octabyte.io) as the database but you can implement the same steps to connect any supporting database by Superset. So, log in to the Superset service with the credentials provided in the OctaByte dashboard. Once you are in click on **Settings** and head over to **Database Connections** under the **Data** section.

![Database connection button in superset](images/Screenshot-2024-09-25-at-11.37.01-AM.jpg)This will lead you to the dashboard where you can manage all of your database connections. Here click on the **Database** button on the top right corner.

![Databse button in superset](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.35.54-AM.jpg)This is another option to quickly do the exact same steps as above, this following step will save you time in future to access the database configuration settings sooner. To quickly add a database connection, click on **\+** \> **Data** \> **Connect database**. 

![Quick connect database setting](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.38.36-AM.jpg)Now you will be prompted with a window to select the database you want to use. We will select PostgreSQL. You can choose to select from the option either from the cards or under supported databases.

![Selecting postgreSQL as database in supereset.](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.41.08-AM.jpg)For the next step, we will require PostgreSQL server details. For this, head over to your deployed service of Postgres on OctaByte and click on **Show DB Credentials**. We will copy these details and use them in the next steps.

![PostgreSQL database details in OctaByte](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.51.33-AM.jpg)Enter the details you got from the OctaByte dashboard here and give a database name that already exists in the PostgreSQL database. This data in this mentioned database can be used moving forward in Superset. After adding the details click on **Connect** button.

![Database details in Superset database connection](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.53.26-AM.jpg)You can choose to configure your database connection further with performance, security and other things as required, once done click on **Finish.**

![Last step of database connection in superset](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.55.02-AM.jpg)Once added, you can see the added databases in the dashboard. This helps you keep track of your database connections along with their configurations.

![All database connections in superset](https://blog.elest.io/content/images/2024/09/Screenshot-2024-09-25-at-11.56.03-AM.jpg)## **Thanks for reading ❤️**

By following this guide, you’ve successfully connected your databases with Apache Superset on OctaByte. Learn more about it through official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.octabyte.io). Click below to start exploring with Superset on [OctaByte](https://octabyte.io/applications/business-intelligence/superset). See you in the next guide! 👋




[![Deploy to OctaByte](/images/octabyte-deploy.png)](https://octabyte.io/applications/business-intelligence/superset)



