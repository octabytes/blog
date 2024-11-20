---
draft: true
title: "Migrate to OctaByte's managed services"
date: "2024-09-10"
description: "This migration document focuses on the migration of the applications supported by OctaByte. Find the software list here

This document provides a step-by-step guide for migrating your existing system to OctaByte. OctaByte is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate to OctaByte's managed services"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by OctaByte. Find the software list [here](https://octabyte.io/fully-managed-services?ref=blog.octabyte.io)

This document provides a step\-by\-step guide for migrating your existing system to OctaByte. OctaByte is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Make sure the service you are trying to migrate from is being supported by OctaByte. You can find the entire software catalogue [here](https://octabyte.io/fully-managed-services?ref=blog.octabyte.io)
2. Create an account on [OctaByte](https://octabyte.io/?ref=blog.octabyte.io)
3. Deploy the service you want to migrate to. Follow the simple steps to deploy your preferred services on [OctaByte's blogs](https://blog.octabyte.io/)
4. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
5. When deploying the service on OctaByte, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Exporting the Data

1. Head over to the application you have deployed on the service
2. There will be either of two options \- Migrate or Export
3. If it's a migration option then most probably it will make use of the API keys so you can keep an eye on the use of the API keys
4. If it's exported then you will get a file downloaded on your local machine having the config information of the application
5. Note that you might need to export the mounted data if you are running the service in a Docker container or personal VM.


> Don't forget to add mounted data to `/opt/app` the directory inside OctaByte's file system

### 3️⃣ Importing the Data

1. After your service is deployed on OctaByte, you can access the dashboard using the URL, username, and password in the admin credentials. You will also receive an email containing all credentials and the necessary service settings.
2. Once you log into the application, you can head over to migration or import settings.
3. If it's the migration then either on the application dashboard or the OctaByte dashboard you will be asked to add the application ID, API keys etc. Provide all the keys wait for it to migrate and set your application on OctaByte
4. If it's import then click on the import option and select the exported file from the previous file, wait for some time and you will find it running on OctaByte!
5. If none of the settings are found then you have to manually download the data and upload it to `opt/app` directory of OctaByte instance using File Explorer, VScode, or Filezilla

### 4️⃣ Testing the Migration

1. You have successfully migrated to OctaByte, now it's time for testing if your application is running as you intended
2. Make use of integrated tools in OctaByte like File Explorer, VScode, or Filezilla to set the additional data and assets
3. If you find any issues with the migration, try to restart your instance and restart containers using the following commands


> docker\-compose down


> docker\-compose up \-d \-\-build

1. Checkout logs if something is failing. Note that there can be a version lapse between your currently hosted application and the running instance on OctaByte (Latest version) as mentioned in the Pre\-requisites section

### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.octabyte.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-to-elestio-managed-services?ref=blog.octabyte.io)*on November 3, 2023\.*



