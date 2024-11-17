---
draft: true
title: "Migrate your customized application to Elestio"
date: "2024-03-03"
description: "This migration document is only for services that are not being supported by Elestio as a fully managed option. If you are unaware of the software supported, take a look here. If Elestio is supporting the software then you can follow this migration document


1️⃣ Pre-requisites

 1. Make sure the"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate your customized application to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document is only for services that are not being supported by Elestio as a fully managed option. If you are unaware of the software supported, take a look [here](https://elest.io/fully-managed-services?ref=blog.elest.io). If Elestio is supporting the software then you can follow [this migration document](https://docs.elest.io/books/migrations/page/migrate-to-elestio-managed-services?ref=blog.elest.io)

### 1️⃣ Pre\-requisites

1. Make sure the service you are trying to migrate from is being supported by Elestio. You can find the entire software catalogue [here](https://elest.io/fully-managed-services?ref=blog.elest.io)
2. Create an account on [Elestio](https://dash.elest.io/?ref=blog.elest.io)
3. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Using Git Repository

If your service/application is hosted on Git repositories (public \& private) you can follow the following steps to migrate easily to Elestio.

1. Head over to the CI/CD section and choose and import your Git repository

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698750434336/f6c2fdc5-4b48-4f8b-9df4-e3977f9c7343.png)2. Choose the cloud of your choice, region and service plan.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698750988823/7264c225-90d2-48af-9fd6-4077bc2a4af0.png)3. Select the tech\-stack or docker\-compose in case you have that on your git\-repository

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698751681320/64d9acc5-9fce-48d0-9067-f48e880b523c.png)4. You can add additional configurations to your application by going to the "Build and Deploy" option.
5. In case you need to add something that is not available on your git repository then you can add it manually with the given steps in the "Manual Migration" from below.

### 3️⃣ Containerized Migration

If your application is containerized and you want to use pre\-built docker images. If you have a git repository you use to build these images then you can directly use these git repositories to deploy your application to Elestio from the steps given above

1. Go to the Elestio dashboard and use the Docker Compose option in the CI/CD section choose a custom docker\-compose and click on Deploy.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698853208409/3e9cd64d-40df-4e70-8374-b4e7a4658bff.png)2. Choose the cloud service provider, region and service plan of your choice

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698853910731/a6aa8ef1-c91f-4b58-b8ef-91b92603ee5e.png)3\. Add your docker\-compose configuration code in the given area. Additionally, if you are using a private Docker repository then you can use the checkbox to indicate that.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1698854448643/53d614a9-cb7b-4fa7-8195-1d0540339a33.png)### 4️⃣ Manual Migration

If you don't use containerization then you will be guided to do a manual migration. Follow the following steps to effortlessly migrate to Elestio.

1. You should head over to the dashboard and select the template that works with your application tech stack

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1699025502080/62f7e054-b5c7-4970-8235-7bd9a2d93a7b.png)2. After the service is deployed, you can go ahead to the "Tools" tab and select any method of your choice to upload the assets and data

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1699026147062/c1c6fb11-86d6-490c-9c15-6f6a8c565f61.png)3. For example, the following image is from File Explorer. You should navigate to `/opt/app/PIPELINE_NAME` and upload your code files and other assets exactly like you have in your project directory

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1699026463232/8c124623-aae9-4ee6-9c5c-92f85aab5836.png)4. After successful upload, you can update the settings in the dashboard

### 5️⃣ Database Migration

If you are trying to migrate the database data then follow the instructions below to complete the migration without any data loss

1. If you are using a database that provides a UI option eg: phpMyAdmin or pgAdmin then you can go ahead with to export setting of the original database export the data in the file and import that data from the file inside the Elestio instance
2. If the database does not have UI or provide dedicated options for import and export in UI then follow the same above steps to manually add the exported data file to the VM and then restore the file in the database

### 6️⃣ Testing the Migration

1. You have successfully migrated to Elestio, now it's time for testing if your database is running as you intended
2. Make use of integrated tools in Elestio like File Explorer, VScode, or Filezilla to set the additional data and assets
3. If you find any issues with the migration, try to restart your instance and restart containers using the following commands


> docker\-compose down


> docker\-compose up \-d \-\-build

1. Checkout logs if something is failing. Note that there can be a version lapse between your currently hosted database and the running instance on Elestio (Latest version) as mentioned in the Pre\-requisites section

### 7️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-your-customized-application-to-elestio?ref=blog.elest.io)*on November 7, 2023\.*



