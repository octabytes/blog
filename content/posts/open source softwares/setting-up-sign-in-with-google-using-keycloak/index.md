---
draft: true
title: "Integrating Google Sign-In with Keycloak"
date: "2024-08-31"
description: "Hey everyone, in this blog we will be setting up the 'Sign in with Google' option using Keycloak. We will be using a self-hosted Keycloak instance deployed on Elestio. So, to get started head over to Elestio Dashboard and deploy and login into the Keycloak instance to get"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Integrating Google Sign-In with Keycloak"
ShowToc: true
TocOpen: true
---


Hey everyone, in this blog we will be setting up the "Sign in with Google" option using Keycloak. We will be using a self\-hosted Keycloak instance deployed on Elestio. So, to get started head over to [Elestio Dashboard](https://elest.io/open-source/keycloak?ref=blog.elest.io) and deploy and login into the Keycloak instance to get started.

## Creating New Realm

According to the Keycloak documentation


> A realm manages a set of users, credentials, roles, and groups. A user belongs to and logs into a realm. Realms are isolated from one another and can only manage and authenticate the users that they control.

Once you are logged in, head over to the drop\-down menu on the top left hand. It is important to notice that there is a realm "***Keycloak master***" already available. This realm has higher privileges hence it is recommended to create a new realm. Click on "***Create realm***".

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713626443556/d64daa62-6e56-44c6-b13b-d8d2fde06116.jpeg)Now add the realm information such as Realm name. For eg: Here I have given it a name "***Google\-Auth***". Click on "***Create***" to create new realm.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625397867/06611951-3ea7-4034-981e-a9d1d7e4e316.jpeg)Next, head over to "***Identity Providers"*** in the left panel and click on "***Google"*** from other identity provider options.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625437800/a2ae3e2e-7dfd-46de-8023-8e0bf31e630b.jpeg)The link that is provided in "***Redirect URI"*** is important and will be required in the next steps. So make sure to keep this tab open. The link should be something like


```
https://YOUR_KEYCLOAK_DOMAIN/auth/realms/YOUR_REALM_NAME/broker/google/endpoint
```
Head over to next section to get the information to be filled out in this step.

## Create Google Application

Head over to [Google Console](https://console.developers.google.com/?ref=blog.elest.io), login in to the console using Google account and you will see Google Developer Console.

Once logged in, head over the top left drop\-down to create new project.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713633166601/030981e1-f79b-4934-9811-6fa42a90465d.jpeg)Click on "***New Project"*** to proceed.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625441069/569d4f66-d20c-4a8f-80ba-bae0414afec4.jpeg)Enter the project name of your choice and select the Organisation if you have multiple organisations. Once done click on "***Create"***

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625443743/2ac97758-0fc9-4be4-847d-90459f1c5635.jpeg)Once the project is created you will get a pop\-up suggesting to configure the consent screen. If not then head over to the *Dashboard* and head over to "***Explore and enable APIs"*** options. Then Click on "***Credentials"** \> "**Configure Consent Screen"*** and head over to the next step.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625445658/fafcafa6-11d2-4bb9-aa33-2f9c2b9c90dc.jpeg)Click on "***External"*** as we want to allow any Google account to be able to sign in to our application and hit "***Create"***.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625447813/a5921b3d-ce7a-49cb-bfea-a296b1afe579.jpeg)After this, we will be redirected to pages where we will have to configure different things

* Application type: Public
* Application name: Your application name
* Authorised domains: Your application top\-level domain name
* Application Homepage link: Your application homepage
* Application Privacy Policy link: Your application privacy policy link

Now head over to the *Create Credentials* option in the navbar and click on "***OAuth Client ID"**.*

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625449681/05f777af-bc2d-4fd3-b83c-ab707bde7878.jpeg)Select Application type as a "***Web application"*** and name the application according to your choice. Next, Add the link provided in the Keycloak tab under "***Authorized Redirect URIs"*** and click "***Create"***. The link should look something like this


```
https://YOUR_KEYCLOAK_DOMAIN/auth/realms/YOUR_REALM_NAME/broker/google/endpoint
```
![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625451391/c16f4aa8-395f-4e8f-9100-68bbd468cc2d.jpeg)As it is done, you will see a pop up with the information required in the next step. You will need to "***Client ID"*** and "***Client secret"*** in next step so make sure you make a safe copy of it.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713635522192/a92459fa-8f10-4ada-92ff-7510501d2f2f.jpeg)## Configuring Keycloak With Google Application Credentials

Add the copied credentials in the Keycloak Google provider section and click on the "***Add"*** button.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713635528769/c056697a-2ff6-440f-b172-b25b457b7af0.jpeg)And done! Now whenever you want to login with a Keycloak configured client you will find the option to login with Google Auth.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1713625454960/8fb72968-433a-4eb1-904d-7198a5d6e709.jpeg)## **Thanks for reading ❤️**

Thank you so much for reading and do check out the resources provided to learn more about the Keycloak. You can click the button below to create your service on [Elestio](https://elest.io/open-source/keycloak?ref=blog.elest.io) and implement this authentication method. See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/?ref=blog.elest.io)

