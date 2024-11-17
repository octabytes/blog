---
draft: true
title: "Migrate Jenkins Pipeline to Elestio"
date: "2024-03-06"
description: "This migration document focuses on the migration of the applications supported by Elestio. Find the software list here

This document provides a step-by-step guide for migrating your existing Jenkins pipelines to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Migrate Jenkins Pipeline to Elestio"
ShowToc: true
TocOpen: true
---



> This migration document focuses on the migration of the applications supported by Elestio. Find the software list [here](https://elest.io/fully-managed-services?ref=blog.elest.io)

This document provides a step\-by\-step guide for migrating your existing Jenkins pipelines to Elestio. Elestio is designed to enhance performance, scalability, and overall system efficiency. Before you begin the migration process, make sure to check the pre\-requisites

### 1️⃣ Pre\-requisites

1. Create an account on [Elestio](https://elest.io/?ref=blog.elest.io)
2. Log in to your Jenkins admin dashboard account on the server where your current Jenkins is deployed
3. Make sure the UI for the application is working fine and there are no critical errors detected in the application logs. If found otherwise please feel free to create a support ticket
4. When deploying the service on Elestio, use the same software version as your present service, or your data migration will fail.

### 2️⃣ Configuring Jenkins server on Elestio

1. Login to your Elestio account
2. Go to Create Services and select "Jenkins"
3. Select the Cloud Service provider, region, and service plan and click Next.
4. Select the service support, name your Jenkins instance on Elestio, and click on "Create service", this will create an instance of Jenkins on VMs on the cloud you chose.
5. After deployment is ready, head over to the email linked to your account or the one you added while setting up the instance.
6. The email should contain all the details including the dashboard link and the initial password required to access the admin UI.
7. The email should be something like this

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/a3Timage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/a3Timage.png?ref=blog.elest.io)8. Copy the password with the instructions given in the email and paste it into the dashboard window here

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/MYcimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/MYcimage.png?ref=blog.elest.io)### 3️⃣ Importing Data

1. For this tutorial, we are going to import two simple pipelines that are already created on a source server

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/wIuimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/wIuimage.png?ref=blog.elest.io)2. Head over to your Jenkins instance dashboard on Elestio. Click on "Manage Jenkins" and select "Plugins"

[![Screenshot 2023-11-19 at 1.12.54 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-12-54-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-12-54-pm.png?ref=blog.elest.io)3. Once you are in there install "Job import" plugin. Accordingly, you might want to restart the Jenkins too

[![Screenshot 2023-11-19 at 1.16.26 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-16-26-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-16-26-pm.png?ref=blog.elest.io)4. Now, head over to the "Manage Jenkins" and head over to "System" to update the configuration. Scroll down until you find the Job Import Plugin section and click on "add remote Jenkins"

[![Screenshot 2023-11-19 at 1.41.17 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-41-17-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-41-17-pm.png?ref=blog.elest.io)5. Add your original Jenkins server information as requested, you will have to add the credentials. Click on add credentials and add the credentials of your original Jenkins server

![Screenshot 2023-11-19 at 1.46.36 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-46-36-pm.png)6. Select that as credentials under the drop\-down and make sure you have the window looking similar to this

[![Screenshot 2023-11-19 at 1.47.09 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-47-09-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-47-09-pm.png?ref=blog.elest.io)7. Apply and save the remote Jenkins settings head over to the Jenkins dashboard and click on the new option you can see called "Job Import Plugin"

[![Screenshot 2023-11-19 at 1.49.28 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-49-28-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-49-28-pm.png?ref=blog.elest.io)8. Select your server from the drop\-down and click on Search into folders so you don't have to put it in the remote folder. Click on the Query button.

[![Screenshot 2023-11-19 at 1.49.51 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-49-51-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-49-51-pm.png?ref=blog.elest.io)9. Now you will be able to see all the pipelines available on your source server. You can select selective pipelines if you want to. Select the needed pipelines and hit the Import button

[![Screenshot 2023-11-19 at 1.50.10 PM.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/screenshot-2023-11-19-at-1-50-10-pm.png)](https://docs.elest.io/uploads/images/gallery/2023-11/screenshot-2023-11-19-at-1-50-10-pm.png?ref=blog.elest.io)10. Woohoo 🎉, You have successfully imported the pipelines from your source server.

### 4️⃣ Testing the Migration

1. You have successfully migrated to Elestio, now it's time for testing if your application is running as you intended
2. Head over to the Jenkins dashboard and see if all of your pipelines have been imported correctly. Additionally, try running the pipelines.

[![image.png](https://docs.elest.io/uploads/images/gallery/2023-11/scaled-1680-/wIuimage.png)](https://docs.elest.io/uploads/images/gallery/2023-11/wIuimage.png?ref=blog.elest.io)### 5️⃣ Need additional help?

Stuck somewhere? We are here to help you, go ahead and create a [support ticket](https://dash.elest.io/support/creation?ref=blog.elest.io) and we will get back to you in no time.


> *Originally published at*[*https://docs.elest.io*](https://docs.elest.io/books/migrations/page/migrate-jenkins-pipeline-to-elestio?ref=blog.elest.io)*on November 19, 2023\.*



