---
draft: true
title: "How to build a Telegram AI bot with N8N"
date: "2024-04-24"
description: "Let's see how you can create a Telegram AI bot with N8N open-source. During this tutorial, we will be creating the workflow using a template. You can create the same from scratch too. Before we start, ensure you have deployed N8N, we will be self-hosting it on OctaByte."
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "How to build a Telegram AI bot with N8N"
ShowToc: true
TocOpen: true
---


Let's see how you can create a Telegram AI bot with [N8N](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io) open\-source. During this tutorial, we will be creating the workflow using a template. You can create the same from scratch too. Before we start, ensure you have deployed N8N, we will be self\-hosting it on [OctaByte](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io).

## What is N8N?

N8N is an open\-source workflow automation tool that allows you to automate tasks and workflows by connecting various applications, services, and APIs together. It provides a visual interface where users can create workflows using a node\-based system, similar to flowcharts, without needing to write any code. You can integrate n8n with a wide range of applications and services, including popular ones like Google Drive, Slack, GitHub, and more. This flexibility enables users to automate various tasks, such as data synchronization, notifications, data processing, and more.

## Using Template

Once you log in to N8N you will land on the canvas page of N8N. To check out different templates and use one, head over to the templates section from the left sidebar. 

![N8N template section](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.39.21-PM.jpg)Then search for the "Telegram AI bot with LangChain nodes" template or simply click [here](https://arc.net/l/quote/edawurcd?ref=blog.octabyte.io). Next, click on **Use Workflow**pop\-up.

![Template selection screen](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.43.08-PM.jpg)Select the N8N instance you want to use this template for. If you have multiple N8N instances running then you can choose the appropriate one.

## Configuring Telegram Credentials

Now as you move ahead in the process you will be prompted with apop\-up to configure Telegram credentials. Click on **Create New** your  **Telegram credential** 

![Setting up Telegram credential](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.44.51-PM.jpg)Now first let's create the token required for Telegram integration. Head over to your telegram account search for **BotFather** account and put in a command `/newbot` this will ask you to give your name for your application. Once you provide the name you will be provided with the token to access the HTTP API as shown in the image below. If you want additional configuration or information, head over to the [Telegram N8N docs](https://docs.n8n.io/integrations/builtin/credentials/telegram/?ref=blog.octabyte.io).

![Telegram BotFather window](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-28-at-12.04.39-AM-1.jpg)Copy the access token from the bot and paste it into the configuration section provided.

![Access token of telegram](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.54.59-PM-1.jpg)## Configuring OpenAI Chat Model Credentials

Next, we will configure the OpenAI Chat Model. Click on **Create new OpenAI Chat Model credential** 

![OpenAI chat model credentials window](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.45.26-PM-1.jpg)For this head over to the [OpenAi API Keys](https://platform.openai.com/api-keys?ref=blog.octabyte.io) dashboard and create a new API key for this application. Once created, add the key to the **API Key** section, add the optional organization ID and head to the next step.

![Setup OpenAI API key ](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-27-at-11.55.11-PM.jpg)Here is the map that will work as a workflow. To test out this workflow, you can click on **Test Workflow**. This workflow listens for incoming events from telegram, his request is forwarded to AI agent (OpenAI) and after processing the output image is sent back to telegram.

![Testing the workflow](https://blog.octabyte.io/content/images/2024/05/Screenshot-2024-05-28-at-12.02.01-AM.jpg)The following webhook command can be found from the starting components and can be used to trigger the webhooks and provide the prompts required by the application to create images using OpenAI. You will find similar


```
https://<OctaByte Domain>/webhook-test/<Your N8N Service Id>/webhook
```
And done! You have successfully created atelegram AI bot that takes inputs and responds with the image related to the prompt given. You can form multiple such workflows based on the OpenAI function type.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.octabyte.io) to learn more about N8N. You can click the button below to create your service on [OctaByte](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io) and start building your Telegram AI bot that generates images as requested in the chats. See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://octabyte.io/open-source/n8n?ref=blog.octabyte.io)

