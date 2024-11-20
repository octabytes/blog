---
draft: true
title: "Performing SQL query on MySQL server"
date: "2024-07-30"
description: "Let's see how you can create API Endpoints that perform SQL query on MySQL server. During this tutorial, we will be creating the workflow from scratch. You can choose to use different databases to perform similar actions. Before we start, make sure you have deployed N8N, we will"
tags: []
categories: [Automation]
cover:
  image: images/cover.png
  caption: "Performing SQL query on MySQL server"
ShowToc: true
TocOpen: true
---


Let's see how you can create API Endpoints that perform SQL query on MySQL server. During this tutorial, we will be creating the workflow from scratch. You can choose to use different databases to perform similar actions. Before we start, make sure you have deployed N8N, we will be self\-hosting it on [OctaByte](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io).

## What is N8N?

N8N is an open\-source workflow automation tool that allows you to automate tasks and workflows by connecting various applications, services, and APIs together. It provides a visual interface where users can create workflows using a node\-based system, similar to flowcharts, without needing to write any code. You can integrate n8n with a wide range of applications and services, including popular ones like Google Drive, Slack, GitHub, and more. This flexibility enables users to automate a variety of tasks, such as data synchronization, notifications, data processing, and more.

This application is a simple workflow that takes `id` as input and returns a record with the ID after querying the SQL server. The end of the workflow should look something similar to:

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.25.40-PM.jpg)## Configuring Webhook

When you are starting, click on the "\+" button and add the following **Webhook** and **MySQL** components. After that click on the **Webhook** component to configure it to accept the incoming request.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.25.40-PM-2.jpg)Once you click on **Webhook** you can copy the **Test URL/Production URL**, Select the HTTP Method. Here we are trying to make a **GET** request so we have selected it from the drop\-down menu. Let's keep Authentication as none for simplicity but make sure while in production you add the authentication to provide security to the endpoints. Additionally, we will configure the response to be made **When Last Node Finishes** under **Respond**.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.26.09-PM.jpg)## Configuring MySQL Server

Now it's time to configure the **MySQL** component. In this configuration, we connect this component with our MySQL server that is hosted on the cloud. Here we have already deployed MySQL Server on OctaByte and you can too by heading over to [OctaByte Dashboard](https://octabyte.io/open-source/mysql?ref=blog.octabyte.io).

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.25.52-PM.jpg)Once you click on **Credential to connect with** section and click on **Create New Credential**. 

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.26.58-PM.jpg)Now head over to your deployed MySQL service and copy all the information as it will be required to configure your N8N MySQL service.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.27.47-PM.jpg)This is a test database and table that is created for this blog. This will be useful when you write the query you want to run once the component is running.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.32.19-PM.jpg)Now, paste all the information copied before into the connection settings of the **MySQL** component. 

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.28.17-PM.jpg)Once the MySQL server is connected, head over to **Table** switch the criteria to **Name** and select the table name of your choice. Like in this case it is **student**. Now, under **Select Rows** set it up as

**Column:** Id

**Operator:** Equal

**Value:** `{{$json.query.id.toInt()}}`

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.26.31-PM.jpg)## Testing Workflow

For testing your workflow you will see the **Test workflow** button. Click on it and paste the endpoint URL copied from the **Webhook** component in the earlier steps. Make sure you add the query property to it. In this case, it will be `?id=<Id from table>` so the final URL will look something like:


```
https://n8n-ygblb-u7774.vm.elestio.app/webhook-test/8b6ac879-866b-4048-bcba-b04b4efa3ee7?id=1
```
![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-11.45.19-PM.jpg)You should see output like below.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-30-at-9.33.44-PM.jpg)And done! You have successfully created an application that queries the SQL server and responds with the row data adjacent to the ID provided. You can form multiple such workflows based on the request type.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.octabyte.io) to learn more about N8N. You can click the button below to create your service on [OctaByte](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io) and perform queries on your SQL server. See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io)

