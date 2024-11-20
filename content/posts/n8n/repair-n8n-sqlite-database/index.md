---
draft: false
title: "Repair N8N SQLite database"
date: "2024-11-20"
description: "This post guides you through the process of recovering a corrupt SQLite database in N8N, a self-hosted automation tool on OctaByte. It provides step-by-step instructions to repair the database using the CLI."
tags: [N8N, OctaByte, SQLite, Database Recovery, Self-Hosting, Automation, CLI, Repair]
categories: [Applications, Automation]
cover:
  image: images/cover.png
  caption: "Repair N8N SQLite database"
  relative: true
ShowToc: true
TocOpen: true
---


We are going to use a self\-hosted version of N8N deployed on OctaByte. So before we start, ensure you have deployed N8N, we will be self\-hosting it on [OctaByte](https://octabyte.io/applications/automation/n8n).

## Go to your N8N data folder

Open terminal and go to your N8N data folder, on elestio it's located on /opt/app/n8n/database.sqlite

## Repair using the ".repair" command in CLI

 **Step 1:** Open the Command Line Interface and ensure you can access the SQLite CLI, the program named "SQLite3".

**Step 2:** Generate SQL Text from the Corrupt Database and use the following command to recover your corrupt database and generate SQL text:


```
sqlite3 database.sqlite .recover >recover.sqlite
```
This command will create a file named "recover.sqlite" containing the SQL text necessary to reconstruct the original database.

**Step 3:** Rename the corrupt database and use the cleaned database:


```
mv database.sqlite database-old.sqlite
mv recover.sqlite database.sqlite
```
By following these steps, you can effectively recover data from a corrupt SQLite database using the CLI.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [N8N documentation](https://docs.n8n.io/?ref=blog.octabyte.io) to learn more about N8N. You can click the button below to create your service on [OctaByte](https://octabyte.io/applications/automation/n8n) and start building a robust database for SQLite and recover the databases if corrupt. See you in the next one👋

[![](/images/octabyte-deploy.png)](https://octabyte.io/applications/automation/n8n)

