---
draft: true
title: "Using Superset for Real-Time Data Analytics"
date: "2024-03-04"
description: "In this guide, we will walk you through setting up real-time analytics by integrating Apache Superset with ClickHouse, a database suited for analytical queries. This blog will cover each step, from deploying the necessary components to configuring Superset for optimal performance.


Deploying ClickHouse and Superset

The first step in setting"
tags: []
categories: [Business Intelligence]
cover:
  image: images/cover.png
  caption: "Using Superset for Real-Time Data Analytics"
ShowToc: true
TocOpen: true
---


In this guide, we will walk you through setting up real\-time analytics by integrating [Apache Superset](https://octabyte.io/open-source/superset?ref=blog.octabyte.io) with [ClickHouse](https://octabyte.io/open-source/clickhouse?ref=blog.octabyte.io), a database suited for analytical queries. This blog will cover each step, from deploying the necessary components to configuring Superset for optimal performance.

## Deploying ClickHouse and Superset

The first step in setting up real\-time data analytics is to deploy both Apache Superset and ClickHouse on OctaByte. On the OctaByte dashboard, you can create instances for both ClickHouse and Superset. Once the instances are deployed, you’ll have access to the necessary details, such as IP addresses, ports, and credentials, to proceed with the configuration. After deployment you can view both of the deployments under your project like the following

![Deployed ClickHouse and Superset on OctaByte](images/image-3.png)## Installing the ClickHouse Driver for Superset

To connect Superset to ClickHouse, you'll need the `clickhouse-sqlalchemy` driver, which facilitates communication between Superset and ClickHouse using SQLAlchemy, a common toolkit for database connections in Python. You can run this command in the terminal by accessing **VS Code** under the tools section from the dashboard. Add the `clickhouse-sqlalchemy` package to `reqiurements-local.txt` . This ensures that Superset can interface with ClickHouse and execute queries on real\-time data.

## Adding the ClickHouse Database in Superset

Before we add ClickHouse Database to Superset, we need to construct SQLAlchemy URI for our ClickHouse. Head over to the deployed service on your OctaByte Dashboard and click on **Database Admin** button to access the information required for the URI.

![Database admin infomation of ClickHouse](https://blog.octabyte.io/content/images/2024/10/Screenshot-2024-10-03-at-11.55.47-AM.jpg)You can use the above information to replace the information in the below URI


```
clickhouse+native://[user:password]@host[:port]/database[?options]

```
* Log in to your Superset instance.
* Navigate to the **Data** tab in the top menu and select **Databases**.
* Click on **\+ Add Database**.

![Connecting Database in Superset](https://blog.octabyte.io/content/images/2024/10/Screenshot-2024-10-03-at-12.01.34-PM.jpg)* In the **SQLAlchemy URI** field, paste the ClickHouse connection string.

![SQLAlchemy URI in Superset](https://blog.octabyte.io/content/images/2024/10/image-4.png)* Fill in any additional details, such as a display name, and click **Test Connection** to ensure everything works properly.

Once the connection is verified, the ClickHouse database will be available for use in Superset.

## Creating a Dataset in Superset

A **dataset** is a collection of structured data, often organized in rows and columns, that is used for analysis and visualization. In the context of tools like Apache Superset, a dataset typically represents a table or a view from a database, which can then be used to create charts, reports, and dashboards. With the ClickHouse database connected, the next step is to create a dataset in Superset. Datasets in Superset are essentially tables or views that you will use to build visualizations.

* Go to the **Data** tab and select **Datasets**.
* Click on **\+ Dataset**, and choose the ClickHouse database.
* Select the table or view you want to use and configure its fields.
* After saving, the dataset will be available for analysis and visualizations in Superset.

## Creating a Time Series Chart

A **time series chart** is a type of graph used to display data points at successive time intervals. It helps track changes, trends, or patterns over time, making it ideal for visualizing how certain metrics evolve. Time series charts are commonly used for real\-time data analytics, where the focus is on monitoring how data values change at regular time intervals, such as hourly, daily, or monthly. Now that the dataset is ready, you can start creating visualizations, including time series charts, which are particularly useful for real\-time data.

* Navigate to the **Charts** section.
* Click on **\+ Create a New Chart** and select **Time Series** (any of your choice) as the chart type.
* Choose the dataset you created from ClickHouse.
* Configure the time settings, metrics, and filters to suit your real\-time analytics requirements.

![Creating new chart in superset](https://blog.octabyte.io/content/images/2024/10/image-5.png)This chart will visualize how your data evolves over time, providing real\-time insights.

## Creating a ClickHouse Query in Superset

**SQL Lab** is an interactive SQL query editor, allowing users to write and execute SQL queries directly on their connected databases. It is a tool for exploring data, running complex queries, and generating datasets that can later be used for creating visualizations. Superset offers a SQL editor that allows you to write custom queries. You can leverage this to create optimized queries that fetch real\-time data from ClickHouse.

* Go to **SQL Lab** in Superset.
* Select the ClickHouse database, and write your custom SQL queries.
* Execute the queries to fetch real\-time data, which you can use for analysis or building additional visualizations.

![SQL Lab in Superset](https://blog.octabyte.io/content/images/2024/10/Screenshot-2024-10-03-at-1.23.21-PM.jpg)This flexibility in writing queries ensures that you can extract the precise insights needed for your business.

## Creating Dashboards in Superset

Once you have created your charts and visualizations, you can combine them into dashboards that provide a comprehensive view of your real\-time data.

* Navigate to the **Dashboards** section in Superset.
* Click on **\+ Create Dashboard**, and start adding the charts you've built.

![Creating dashboards in superset](https://blog.octabyte.io/content/images/2024/10/Screenshot-2024-10-03-at-1.29.08-PM.jpg)* Organize the layout, adjust filters, and ensure that the data updates in real time.

![Adding new chart to dashboard in superset](https://blog.octabyte.io/content/images/2024/10/Screenshot-2024-10-03-at-1.30.46-PM.jpg)These dashboards serve as a centralized view for monitoring live data, making them ideal for businesses that rely on up\-to\-the\-minute information.

## Caching and Clustering for Performance

To ensure that Superset performs efficiently when handling real\-time data, you should enable caching and clustering. Caching helps reduce the load on your database by storing query results temporarily, which is useful when dealing with large datasets.

Enable caching by configuring the **CACHE\_CONFIG** in Superset’s configuration file. You can also set up Redis or Memcached as a caching backend to handle frequent requests efficiently. Additionally, consider clustering Superset if you expect high traffic. Running multiple Superset instances behind a load balancer can distribute the load evenly, improving overall performance and reliability.

## **Thanks for reading ❤️**

By following these steps, you can set up Apache Superset to handle real\-time data analytics with ClickHouse. Thank you so much for reading and do check out the OctaByte resources and Official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.octabyte.io) to learn more about Superset. You can click the button below to create your service on [OctaByte](https://octabyte.io/open-source/superset?ref=blog.octabyte.io). See you in the next one👋




[![Deploy to OctaByte](https://octabyte.io/images/logos/deploy-to-elestio-btn.png)](https://octabyte.io/open-source/superset?ref=blog.octabyte.io)



