---
draft: false
title: "API Endpoint for GET method"
date: "2024-11-20"
description: "This blog post provides a step-by-step guide on how to create an API endpoint in N8N that responds to GET requests. It walks through using a template to build the workflow, setting up webhook components, and testing the endpoint."
tags: [N8N, API, GET request, Webhook, Workflow, Automation, Template, Self-hosting, OctaByte, Tutorial]
categories: [Applications, Automation]
cover:
  image: images/cover.png
  caption: "API Endpoint for GET method"
  relative: true
ShowToc: true
TocOpen: true
---


Hey everyone, In this blog we are going to see how you can create API Endpoints that responds to your GET requests using N8N. During this tutorial, we will be creating the workflow using a template. You can create the same from scratch too. Before we start, make sure you have deployed N8N, we will be self\-hosting it on [OctaByte](https://octabyte.io/applications/automation/n8n).

## What is N8N?

N8N is an open source workflow automation tool that allows you to automate tasks and workflows by connecting various applications, services, and APIs together. It provides a visual interface where users can create workflows using a node\-based system, similar to flowcharts, without needing to write any code. You can integrate n8n with a wide range of applications and services, including popular ones like Google Drive, Slack, GitHub, and more. This flexibility enables users to automate a variety of tasks, such as data synchronization, notifications, data processing, and more.

## Using Template

Once you log in into N8N you will land on the canvas page of N8N. To check out different templates and use one, head over to the templates section form the left side bar. 

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.04.47-PM.jpg)Then search for "Creating an API endpoint" template or simply click [here](https://n8n.io/workflows/1750-creating-an-api-endpoint/?ref=blog.octabyte.io). Next, click on **Use workflow**.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-1.58.17-PM.jpg) Select the N8N instance you want to use this template for. If you have multiple N8N instances running then you can choose the appropriate one.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-1.59.17-PM.jpg)## Creating API Workflow

Once you are redirected back to the workflow screen you will find components like below. To start with click on the first **Webhook** component. In this component we set up the endpoint URL, authentication mechanism etc for the API.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-8.08.13-PM.jpg)Once you click on **Webhook** you can copy **Test URL/Production URL**, Select the HTTP Method. Here we are trying to make a **GET** request so we have selected it from the drop down menu. Let's keep Authentication as none for the simplicity but make sure while in production you add the authentication to provide security to the endpoints. Additionally we will add the last webhook component in workflow under **Respond**.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.42.30-PM-1.jpg)This part of workflow enables us to work on the function we want to perform and the filtering of the object once the API endpoint is hit. This component takes in input from previous webhooks and passes on to the reponse webhook. Click on **Create URL string** component to configure it.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.39.19-PM-1.jpg)We will be taking the input from the query section provided with the endpoint. Add the value as `{{$json["query"]["name"]}}` under string name `product`

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.39.53-PM-1.jpg)Next we will configure the **Respond to Webhook** component. Click on this component as shown in the following images and move to the configuration part.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.40.54-PM-1.jpg)This is where we add the reponse we expect once someone performs `GET` request. For this example as we are expecting name as input in the query (`Joe`) and respond as `Hello Joe!`. Hence, we will add a placeholder in the response body as `Hello {{$json["product"]}}!`

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.41.16-PM.jpg)## Testing Workflow

For testing your workflow you will see **Test workflow** button. Click on it and paste the endpoint URL copied from the **Webhook** component in the earlier steps. Make sure you add the query property to it. In this case it will be `?name=Joe` so the final url will look something like


```
https://n8n-9f2ud-u7774.vm.elestio.app/webhook-test/6f7b288e-1efe-4504-a6fd-660931327269?name=Joe
```
![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-11.11.00-PM.jpg)And you should see output like below.

![](https://blog.elest.io/content/images/2024/04/Screenshot-2024-04-26-at-2.43.25-PM.jpg)And done! You have successfully created a simple API endpoint which reponds to **GET** request. You can form multiple such workflows based on the request type.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.octabyte.io) to learn more about N8N. You can click the button below to create your service on [OctaByte](https://octabyte.io/applications/automation/n8n) and retrieve weather information based on a zip code. See you in the next one👋

[![](/images/octabyte-deploy.png)](https://octabyte.io/applications/automation/n8n)

