---
draft: true
title: "Building a BI Dashboard with Metabase"
date: "2024-02-26"
description: "Let's see how you can build a BI Dashboard with Metabase. During this tutorial, we will be creating a BI dashboard to analyse the provided data and visualize it in a dashboard. We are going to create this application from scratch. Before we start, make sure you have"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Building a BI Dashboard with Metabase"
ShowToc: true
TocOpen: true
---


Let's see how you can build a BI Dashboard with [Metabase](https://elest.io/open-source/metabase?ref=blog.elest.io). During this tutorial, we will be creating a BI dashboard to analyse the provided data and visualize it in a dashboard. We are going to create this application from scratch. Before we start, make sure you have deployed Metabase, we will be self\-hosting it on [Elestio](https://elest.io/open-source/metabase?ref=blog.elest.io).

## What is Metabase?

Metabase is an open\-source business intelligence (BI) tool that enables users to visualize and analyze data without requiring advanced technical skills. It allows users to create dashboards, run custom queries, and generate reports through a user\-friendly interface. Metabase connects to various databases and data sources, providing interactive visualizations and easy\-to\-understand insights.

## Creating Collection

Collection is a way to organize and manage related questions, dashboards, and other data\-related objects. Collections function like folders, allowing users to group and categorize their analytical content for easier access and collaboration. To create a new collection head over to **New** \> **Collection**. Add a name to your collection, and select the group you want to save your collection into. Optionally add a description to your collection and click on **Create**.

![Creating new collection window](images/Screenshot-2024-05-26-at-1.13.07-PM.jpg)## Creating Model

The next step is to create a model. Model is a curated representation of your data designed to make data exploration and analysis easier. Models abstract the underlying complexities of the database schema, providing a simplified view with meaningful names, descriptions, and categorizations for tables and fields. To create a model click on **New** \> **Model** and then click on **Use the notebook editor**. 

![Creating model window (Use the notebook editor)](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.13.55-PM.jpg)for this tutorial, we will use the already provided dataset model called **Feedback** add the filters and summarization matric if needed and click on the **Run** button to get the data into the model.

![Dataset window](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.14.18-PM.jpg)## Creating Dashboard

The dashboard is a visual interface that aggregates and displays multiple data visualizations, metrics, and interactive elements in one place, providing a comprehensive overview of key information and insights. Dashboards allow users to monitor and analyze performance, trends, and other critical data points at a glance. To create a new dashboard, click on **New** \> **Dashboard.** Add a name to your dashboard, add an optional description and choose the collection you want to build your dashboard upon.

![New dashboard window in metabase](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.14.58-PM.jpg)## Data Visualization Components

Apart from the Usual dashboard, you can choose to create visualised graphs on your data. Head over to **New** \> **Question**, select the data source as the feedback model and choose the basic matrics from the dropdown like below or provide **Custom Expression.**

![Basic metric window](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.30.55-PM.jpg)Now click on **Visualize** to start the visualization based on the parameter you provided.

![Visualization window](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.41.40-PM.jpg)For example, if the **Summerize** pattern was the **Standard deviation of Rating** then the visualized answer is **0\.81\.** To change the type of visualization from charts to graphs, click on the **Visualization** button on the left bottom section as shown below.

![Default visualization screen](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-1.59.23-PM-1.jpg)Here we have selected the Gauge type. Click on the **Save** button to save the chart. Once done you will be prompted with a pop\-up to add the created chart to your dashboard, you can choose to directly add it from here or do it manually afterwards.

![Chart window in Metabase](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-2.00.27-PM.jpg)## Adding To Dashboard

You can add your visualizations and data to the dashboard by clicking on the "**\+**" button in the dashboard navigation bar. You can add multiple such charts and create different layouts according to your preference.

![Creating custom dashboard](https://blog.elest.io/content/images/2024/05/Screenshot-2024-05-26-at-2.01.15-PM.jpg)And done! You have successfully created a BI dashboard for customer feedback. you can create such dashboards consisting of different data sources, and visualizations fitting your business need. 

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the Elestio resources and Official [Metabase documentation](https://www.metabase.com/docs/latest/?ref=blog.elest.io) to learn more about Metabase. You can click the button below to create your service on [Elestio](https://elest.io/open-source/metabase?ref=blog.elest.io) and build your BI dashboards. See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/open-source/metabase?ref=blog.elest.io)

