---
draft: true
title: "BaaS Showdown: A Comprehensive Look at 5 Top Open Source Solutions"
date: "2024-02-25"
description: "Backend as a Service is the solution for developers who want to focus on building web and mobile apps without worrying about the backend infrastructure.


BaaS providers offer a set of tools and services that help developers build apps faster and easier.


It generally includes Database, Authentication, File Storage, Cloud"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "BaaS Showdown: A Comprehensive Look at 5 Top Open Source Solutions"
ShowToc: true
TocOpen: true
---


Backend as a Service is the solution for developers who want to focus on building web and mobile apps without worrying about the backend infrastructure.


BaaS providers offer a set of tools and services that help developers build apps faster and easier.


It generally includes Database, Authentication, File Storage, Cloud Functions, Push Notifications, and more.


Features that we need in most of the apps we build. Instead of building these features again and again, we can use BaaS solutions to save time without compromising on the quality of the app. (As a large number of developers are using these services, they are well tested and maintained)


Now, the question is which BaaS solution is the best for your app?


Today we will compare 5 Open Source Backend as a Service solutions and find out which one is the best for your app:  

[Appwrite](https://elest.io/open-source/appwrite?ref=blog.elest.io), [Directus](https://elest.io/open-source/directus?ref=blog.elest.io), [Parse](https://elest.io/open-source/parse?ref=blog.elest.io), [PocketBase](https://elest.io/open-source/pocketbase?ref=blog.elest.io), and [Supabase](https://elest.io/open-source/appwrite?ref=blog.elest.io).




Watch our comparison video



## Authentication \& Authorization


Authentication is the process of creating and verifying the identity of a user, in simple words, it is the login, signup, and forgot password functionality.


Authorization on the other hand is the process of verifying if a user has access to a specific resource or not.




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| Authentication | ✅ | ✅ | ✅ | ✅ | ✅ |
| Authorization | ✅ Roles | ✅ Roles | ✅ ACL / Roles | ✅ Rules | ✅ Row Level Security |


They all support authentication, including classic email/password and social login (Google, Facebook, Github, etc) and roles and permissions to control precisely what users can do: read, write, update, delete, etc.


The approach varies from one solution to another, one might fit your needs better than the others. But they all support the basic features to build a secure app. That shouldn't be the key factor to choose one over the other.


## Database \& Realtime


Storing data is the core of any app, and the database is the most important part of the backend. Having a database that is easy to use and scale is crucial for the success of your app.




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| Database | ✅ | ✅ | ✅ | ✅ | ✅ |
| Type | NoSQL | SQL | ✅ NoSQL | ✅ SQLite | ✅ PostgreSQL |
| Admin UI | ✅ | ✅ 🏆 | ✅ | ✅ | ✅ |
| SDK | ✅ | ✅ | ✅ | ✅ | ✅ |
| Rest | ✅ | ✅ | ✅ | ✅ | ✅ |
| GraphQL | ✅ | ✅ | ✅ | ❌ | ✅ |
| Realtime | ✅ WebSocket | ✅ WebSockets \& GraphQL Subscriptions | ❌ | ✅ SSE (Server\-Sent Events) | ✅ Postgres Changes |


Of course, all of them support the basic CRUD operations, but the type of database and the way you interact with it is different.


Appwrite and Parse use NoSQL databases, while Directus, PocketBase, and Supabase use SQL databases. Depending on your app, your needs, and your experience, you might prefer one over the other.


To view and manage your data, they all provide an admin UI but with completely different approaches. Directus provide a full\-featured admin UI, allowing to create custom views and forms for your data. It's a real No\-Code solution.


While Appwrite, Parse, PocketBase, and Supabase provide a more traditional database admin UI.


About the access to the data, they all have SDKs that we will compare later. You can also perform direct REST or GraphQL requests. (Except for PocketBase that doesn't support GraphQL)


Finally, about realtime, they all have the ability to listen to changes in the database and push them to the client in different ways. That allows you to reflect changes in realtime in your app, ideal for chat apps, collaborative apps, and more. Only Parse which is a bit older than the others doesn't support realtime.


Again, there is no clear winner here, it depends on your needs and preferences. If you plan to move to a custom backend later, you might prefer a solution that uses a SQL database. If you know you will have to create a lot of custom views and forms, Directus might be the best choice. If you need realtime, you might eliminate Parse from your list.


## File Storage


File storage is another important feature that you will need in most of your apps. It allows you to store files like images, videos, and documents.




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| File Storage | ✅ | ✅ | ✅ | ✅ | ✅ |
| Permissions | ✅ | ✅ | ❌ | ❌ | ✅ |
| Admin UI | ✅ | ✅ | ❌ | ❌ | ✅ |
| Image Resizing API | ✅ | ✅ | ❌ | ✅ | ✅ |
| S3 compatible | ✅ | ✅ | ✅ | ✅ | ✅ |


All our contenders support file storage with useful features like permissions, an admin UI, and image resizing API. They all support S3 compatible storage, which means you can use any S3 compatible storage provider like AWS S3, Cloudflare R2, or Minio if you want to host your files on a separate server. (Useful for scaling and cost optimization)


Parse and PocketBase are the weakest in this category, they don't have an admin UI and permissions for files. I wouldn't recomment them if your project is essentially based on complex and secure file features.


## Functions, Webhooks, and Cron Jobs


Sometimes you will need to go beyond the basic CRUD operations and add custom logic to your app. You might need to send an email after a purchase, process payments to give access to a premium feature, or send a push notification every day at a specific time.  

That's where functions, webhooks, and cron jobs come in handy.




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| Functions | ✅ | ✅ 🏆 | ✅ | ✅ | ✅ ⚠️ |
| Webhooks | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cron Jobs | ✅ | ✅ | ✅ | ✅ | ✅ |


They all support functions, webhooks, and cron jobs but in very different ways. Directus has the most advanced no\-code/low\-code solution, allowing you to create custom flows with a visual interface. It's a great solution if you want to build a custom backend without writing code.


Appwrite and Supabase both have the possibility to create and view functions from the admin UI while PocketBase and Parse require you to write your functions' code directly on your server. Which is a bit more complicated but also more flexible.


A small note about Supabase, their cloud version supports functions out of the box, but their self\-hosted version doesn't. Still, recently they made their Edge Runtime open source, so with a medium effort, you can add functions to your self\-hosted Supabase instance.


Overall they all allow you to create custom logic for your app, but based on your workflow and preferences, you might prefer one over the other.


## Push Notifications \& Emails


Most of the apps we build need to send emails and/or push notifications. It's a must\-have feature for any app. BUT, there are many services that provide this feature, so it's not a big deal if your BaaS solution doesn't support it. Still, it's nice to have it in the same place.




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| Push Notifications | ❌ | ❌ | ✅ | ❌ | ❌ |
| Emails | ✅ | ✅ | ❌ | ✅ | ✅ |


Except for Parse, they all support emails out of the box such as welcome emails, password reset, and more. Parse is the only one that doesn't support emails, but you can easily integrate a third\-party service like Sendgrid or Mailgun.


What makes Parse unique is the support for push notifications and its dashboard to send them. It's been a reason for its wide adoption in the past.  

But again, you can integrate a third\-party service like OneSignal or Firebase Cloud Messaging with the others with a few extra lines of code.


## Integrations (SDK)


We have seen that all our BaaS solutions support the essential features to build a web or mobile app. But how easy is it to integrate them into your app?




| Feature | Appwrite | Directus | Parse | PocketBase | Supabase |
| --- | --- | --- | --- | --- | --- |
| Client SDK | Swift, Kotlin, Flutter, JS/TS | JS/TS | iOS (Swift, Objective\-C), Android (Java), JS, Php, Flutter, Dart, .NET, Unity, Arduino | JS/TS, Dart | JS/TS, Flutter, Python, C\#, Swift, Kotlin |
| Server SDK | Node.js, Dart, Python, PHP, Ruby, .NET, Deno, Kotlin | Flows Operations in JS/TS | Node.js | JS/TS, Go | Edge Functions in TS/JS |


If you are building for the JavaScript ecosystem, you will be well served by all of them. But when it comes to native mobile apps, Appwrite, Parse, and Supabase are the best options with support for iOS and Android. But remember that you can always use the REST or GraphQL APIs to integrate them in any language.


## Final Words


The moment of truth, which one is the best BaaS solution for your app? 🥁🥁🥁


Well... It depends on your projects and preferences. They all have their pros and cons, I can confirm that they are all great solutions and you can't go wrong with any of them. They are also all able to handle a large number of users and requests and scale with your app.


While there is not one clear winner, I can give you some recommendations based on your needs:


* If you are building an app with the need to create custom views/forms based on different roles and permissions, if you need to give your clients access to manage their data, Directus is the best choice. With its no\-code/low\-code approach, it will save you a lot of time and effort.
* If you have a lot of custom logic and need to create custom functions, webhooks, and cron jobs, Appwrite and Supabase are the best options. But as Supabase require custom setup for functions, Appwrite is the easiest to get started with.
* If you want a lightweight, simple, and high performance solution, PocketBase is your go\-to solution.


I would put Parse slightly behind the others, it's a great solution but it's a bit outdated, which reflects on its features and UI. Still, if push notifications is a must\-have feature for your app, it might be the best option.


Our biggest recommendation is to try them before making a decision. They are all open source and free to use, so you can try them and see which one fits your needs better.


Each are available as fully managed services on our platform Elestio, which means we take care of the setup, backups, updates, maintenance, and hosting for you.


[Give it a try on Elestio](https://elest.io/?ref=blog.elest.io)



