---
draft: false
title: "Generating PDFs with N8N using Gotenberg"
date: "2024-11-20"
description: "This tutorial explains how to create an N8N workflow to generate PDFs using Gotenberg. It covers the configuration of different components, including HTML generation, file conversion, and making an HTTP request to the Gotenberg API for PDF creation."
tags: [N8N, Gotenberg, PDF Generation, Workflow Automation, Open-Source, Tutorial, OctaByte, Self-Hosting, API, HTTP Request, Automation]
categories: [Applications, Automation]
cover:
  image: images/cover.png
  caption: "Generating PDFs with N8N using Gotenberg"
  relative: true
ShowToc: true
TocOpen: true
---


Let's see how you can create an application that can generate PDFs with [N8N](images/n8n) using [Gotenberg](https://octabyte.io/open-source/gotenberg?ref=blog.octabyte.io). During this tutorial, we will be building the workflow from scratch. You can choose to use different databases to perform similar actions. Before we start, make sure you have deployed N8N, we will be self\-hosting it on [OctaByte](images/n8n).

## What is N8N?

N8N is an open\-source workflow automation tool that allows you to automate tasks and workflows by connecting various applications, services, and APIs together. It provides a visual interface where users can create workflows using a node\-based system, similar to flowcharts, without needing to write any code. You can integrate n8n with a wide range of applications and services, including popular ones like Google Drive, Slack, GitHub, and more. This flexibility enables users to automate a variety of tasks, such as data synchronization, notifications, data processing, and more.

## What is Gotenberg?

Gotenberg is an open\-source API that converts web documents, including HTML and Markdown, to high\-quality PDFs using headless Chrome or Chromium. It also supports converting office documents (like DOCX) to PDF. Designed for integration, it offers a REST API for easy automation of document generation processes and is distributed as a Docker container, ensuring consistent deployment across environments. Gotenberg is a versatile tool for developers and businesses needing reliable and customizable PDF conversion within their applications.

## Configuring Manual Button

Once you get started, you will find a blank workflow canvas in the dashboard. Head over and click on the "\+" button as shown below to start with the first step of creating the workflow

![Add first step button](images/Screenshot-2024-05-08-at-7.48.01-PM.jpg)Next, you will see a pop\-up on the right side of the screen, Select the **Manually** component. This component runs the flow by clicking the button in N8N.

![Selecting manual component](images/Screenshot-2024-05-08-at-7.48.39-PM.jpg)## Setting up HTML component

Next, we will add the next component in the flow which is in **HTML**. In the HTML component, select **Generate HTML template**. 

![Selecting HTML Component](images/Screenshot-2024-05-08-at-8.08.35-PM.jpg)## Convert to File Component

Now we will attach the next component in the flow. The next component in the flow is **Convert to File**. In the component, select **Move base64 string to file**. 

![Selecting file component](images/Screenshot-2024-05-08-at-9.55.55-PM.jpg)Now set the parameters of these components as follows:

**Operation:** Move Base64 String to File

**Base64 Input Field:** HTML

**Put Output File in Field:** data

**Encoding:** utf8

**File Name:** index.html

**MIME Type**: text/HTML

![Configuring HTML Component](images/Screenshot-2024-05-08-at-10.08.23-PM.jpg)## Configuring HTTP Request

The next component we are going to configure is the **HTTP Request**. This component makes an HTTP request and returns the response data.

![Using HTTP Request component](images/Screenshot-2024-05-08-at-10.06.47-PM.jpg)## Setting Up Gotenberg

We will require a Gotenberg service that we are deploying it on OctaByte and you can do the same by clicking [here](https://octabyte.io/open-source/gotenberg?ref=blog.octabyte.io). Once the instance is deployed head over to the email you received on your email ID registered with OctaByte. Find the **Usage** section as we are going to use this information while configuring the Gotenberg in the flow.

![Post request](images/Screenshot-2024-05-08-at-10.32.59-PM.jpg)Now add the **User** and **Password** from elestio dashboard and add it under connection.

![Auth credential](images/Screenshot-2024-05-08-at-10.38.39-PM.jpg)Now set the other parameters similar to those found in the email.

**Method:** Post

**URL:** \<URL from the email or OctaByte dashboard\>

**Authentication:** Generic Credential Type

**Generic Auth Type:** Basic Auth

**Credential for Basic Auth**: User login

![Post request configuration in HTTP request component](images/Screenshot-2024-05-08-at-10.43.11-PM.jpg)Next, configure the Head and body of the request.

**Specify Headers:** Using Fields Below

**Name:** Gotenberg\-Ourput\-Filename

**Value:** result

**Body Content Type**: Form\-Data

**Parameter Type:** Form Data

**Name:** URL

**Value**: https://www.wikipedia.org/

This HTTP request is to send a request to the provided URL to fetch the HTML page and convert it into a PDF using Gotenberg.

![Setting Headers and Body in HTTP Component](images/Screenshot-2024-05-08-at-10.43.27-PM.jpg)Now we have to configure the Response. Set the **Response format** to **File** and **Put Output in Field** to data.

![Configuring response options](images/Screenshot-2024-05-08-at-10.43.38-PM.jpg)The final workflow looks something like this. Now we will test the workflow before we deploy it to production. Click on **Test workflow**. 

![Testing workflow](images/Screenshot-2024-05-08-at-10.44.15-PM.jpg)Once the button is clicked an output window will pop up where we can see our pdf ready. You can download or choose to print the PDF directly.

![Generated PDF](images/Screenshot-2024-05-08-at-10.55.40-PM.jpg)And done! You have successfully created a workflow that creates a pdf of the webpage provided using URL in HTTP request and Gotenberg. You can form multiple such workflows based on the request type.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.octabyte.io) to learn more about N8N. Click the button below to create your service on [OctaByte](images/n8n) and generate PDFs using Gotenberg. See you in the next one👋

[![](/images/octabyte-deploy.png)](images/n8n)

