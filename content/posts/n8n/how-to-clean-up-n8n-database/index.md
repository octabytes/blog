---
draft: true
title: "How to clean up the N8N database"
date: "2024-12-29"
description: "During this tutorial, we are going to use a self-hosted version of N8N deployed on Elestio. So before we start, ensure you have deployed the N8N service and have a connected database that is used to store the logs and execution records.


What is N8N?

N8N is an open-source workflow"
tags: []
categories: [Automation]
cover:
  image: images/cover.png
  caption: "How to clean up the N8N database"
ShowToc: true
TocOpen: true
---


During this tutorial, we are going to use a self\-hosted version of N8N deployed on [Elestio](https://elest.io/open-source/n8n?ref=blog.elest.io). So before we start, ensure you have deployed the N8N service and have a connected database that is used to store the logs and execution records.

## What is N8N?

N8N is an open\-source workflow automation tool that allows you to automate tasks and workflows by connecting various applications, services, and APIs together. It provides a visual interface where users can create workflows using a node\-based system, similar to flowcharts, without needing to write any code. You can integrate n8n with a wide range of applications and services, including popular ones like Google Drive, Slack, GitHub, and more. This flexibility enables users to automate various tasks, such as data synchronization, notifications, data processing, and more.

## Executions Environment Variables

Enabling the `EXECUTIONS_DATA_PRUNE` setting in N8N is a way to manage database storage by automatically deleting past execution data on a rolling basis. To enable this feature, set `EXECUTIONS_DATA_PRUNE` to `true` in your n8n configuration file and restart your instance. This automated cleanup helps maintain a lean database, improving performance and reducing the need for manual maintenance. However, consider your data retention needs to ensure you retain necessary historical data for auditing or debugging purposes. Check out the following documentation to learn about more such variables and how to use them.

[Environment Variables Overview \| n8n DocsAn overview of configuration environment variables for self\-hosted n8n.![](https://docs.n8n.io/_images/favicon.ico)logo![](https://docs.n8n.io/_images/n8n-docs-icon.svg)](https://docs.n8n.io/hosting/environment-variables/?ref=blog.elest.io#executions)## Setting Variable In Configuration File

One of the ways to clean the database in N8N is to set a Variable `EXECUTIONS_DATA_PRUNE` as mentioned above. Now that you know about the variables and have decided on what you want to use we will set the variables in this section. Head over to your N8N service deployed on Elestio and click on **Update config** under the **Software** section in the **Overview** window. 

![Update config option in elestio dashboard](https://blog.elest.io/content/images/2024/06/Screenshot-2024-06-05-at-4.28.54-PM.jpg)Now you will be able to see all the variables configured under **Docker Compose**. Change or add the required variables and click on **Update \& Restart** to implement these variables into the service. You can monitor and keep track of all the used variables here.

![Setting the environment variables in docker compnse](https://blog.elest.io/content/images/2024/06/Screenshot-2024-06-05-at-4.29.38-PM.jpg)For more information on different ways of setting this variable, head over to the official N8N documentation by clicking below.

[Configuration methods \| n8n DocsHow to set environment variables for n8n.![](https://docs.n8n.io/_images/favicon.ico)logo![](https://docs.n8n.io/_images/n8n-docs-icon.svg)](https://docs.n8n.io/hosting/configuration/configuration-methods/?ref=blog.elest.io)## Creating a workflow for pruning

Another method can be creating a workflow for pruning and cleaning the unnecessary logs from the database. To do so, head over to the workflow section in N8N and create a workflow like below. Under the **MySQL** component configure the database information and set up the **Cron** component with the schedule information. 

![N8N database cleaning workflow](https://blog.elest.io/content/images/2024/06/Screenshot-2024-06-05-at-3.26.30-PM.jpg)And done! You have successfully cleaned the database in N8N. Just note that it's always preferred to clean up the data periodically and if the log data is required frequently then you can choose to make backups as required.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the Elestio resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.elest.io) to learn more about N8N. You can click the button below to create your service on [Elestio](https://elest.io/open-source/n8n?ref=blog.elest.io) start cleaning your N8N database and have a smooth running service again. See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/open-source/n8n?ref=blog.elest.io)

