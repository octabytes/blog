---
draft: true
title: "Apache Superset CLI guide"
date: "2024-10-28"
description: "Hey everyone, In this blog we will be knowing more about Superset CLI. The Apache Superset CLI (Command Line Interface) is a tool that enhances the management, configuration, and usage of Superset, eliminating the need for direct web interface interaction. This guide provides a detailed overview of how to leverage"
tags: []
categories: [Business Intelligence]
cover:
  image: images/cover.png
  caption: "Apache Superset CLI guide"
ShowToc: true
TocOpen: true
---


Hey everyone, In this blog we will be knowing more about [Superset](https://elest.io/open-source/superset?ref=blog.elest.io) CLI. The Apache Superset CLI (Command Line Interface) is a tool that enhances the management, configuration, and usage of Superset, eliminating the need for direct web interface interaction. This guide provides a detailed overview of how to leverage the Superset CLI effectively.

#### Installation

To start using the CLI, first install Superset via pip:


```
pip install apache-superset

```
#### Database Initialization

After installation, initialize the database with the following command:


```
superset db upgrade

```
#### Creating an Admin User

Set up an admin user by configuring the `FLASK_APP` environment variable and running the create\-admin command:


```
export FLASK_APP=superset
superset fab create-admin

```
#### Loading Examples

To load sample data into Superset:


```
superset load_examples

```
#### Initializing Superset

Initialize Superset to set up roles and permissions:


```
superset init

```
#### Starting the Server

Launch the server on a custom port with development features enabled:


```
superset run -p 8088 --with-threads --reload --debugger

```
#### Upgrading Superset

To upgrade Superset to a newer version, use the following commands:


```
pip install apache-superset --upgrade
superset db upgrade
superset init

```
#### Custom Configuration

For production environments, ensure you set a `SECRET_KEY` in your configuration, as specified in the official documentation.

#### Additional Commands

The Superset CLI supports various other commands for tasks such as importing/exporting dashboards, managing security, and more. Refer to the official documentation for a complete list of commands and their detailed usage.

By mastering the Apache Superset CLI, you can efficiently manage and configure your Superset instance, streamlining the process of creating and maintaining data visualizations.

## Installing Apache Superset via Command Line Interface (CLI)

logging  
To install Apache Superset using the command line interface (CLI), adhere to the following steps:

1. Install apache\-superset:


```
pip install apache-superset

```
1. Initialize the database:


```
superset db upgrade

```
1. Ensure that you have a SECRET\_KEY set in your configuration for production instances.
2. Create an admin user:


```
export FLASK_APP=superset
superset fab create-admin

```
1. Load example data:


```
superset load_examples

```
1. Create default roles and permissions:


```
superset init

```
1. Build frontend assets: Go to the superset\-frontend directory and execute:


```
npm ci
npm run build

```
1. Start the development server:


```
superset run -p 8088 --with-threads --reload --debugger

```
1. Access Superset by visiting [http://localhost:8088](http://localhost:8088/?ref=blog.elest.io) and logging in with the credentials you created.

## Initializing the Superset Database

  
To set up the Apache Superset database, follow these guidelines:

1. Install Apache Superset: Utilize pip, the Python package manager, to install Superset.


```
pip install apache-superset

```
1. Database Initialization: Execute the following command to upgrade the database to the latest version.


```
superset db upgrade

```
1. Admin User Creation: Define the FLASK\_APP environment variable and create an admin user.


```
export FLASK_APP=superset
superset fab create-admin

```
1. Load Examples: If desired, load example data using the following command:


```
superset load_examples

```
1. Initialize Superset: Establish default roles and permissions with the superset init command.
2. Build Assets: Navigate to the superset\-frontend directory, install dependencies, and build the frontend assets.


```
cd superset-frontend
npm ci
npm run build
cd ..

```
1. Run Development Server: Start the development server on port 8088 or any preferred port.


```
superset run -p 8088 --with-threads --reload --debugger

```
Following these steps ensures Superset's database is set up correctly. Access Superset by visiting [http://localhost:8088](http://localhost:8088/?ref=blog.elest.io) in your browser and logging in with the credentials you created.

## Creating an Admin User via Superset CLI

  
To create an admin user in Apache Superset using the command line interface (CLI), follow these steps after you have Superset installed:

1. Set the FLASK\_APP environment variable to superset:


```
export FLASK_APP=superset

```
1. Use the superset fab create\-admin command to start the process:


```
superset fab create-admin

```
You will be prompted to enter the admin's username, first and last name, email, and password.

1. After creating the admin user, you should initialize the database with the default roles and permissions by running:


```
superset init

```
This process registers the admin user in the metadata database, allowing them to log in to the Superset instance. Remember to follow best practices for securing your admin credentials.

## Loading Example Data with Superset CLI

  
Apache Superset offers a convenient command\-line interface (CLI) for loading example data, aiding users in familiarizing themselves with the platform's capabilities. Below are the steps to load CSV data and example datasets using the Superset CLI:

1. **Load CSV Data:**
	* Download the CSV dataset from the provided GitHub link.
	* In Superset, navigate to Data ‣ Upload a CSV.
	* Specify the Table Name as "tutorial\_flights" and select the downloaded CSV file.
	* Enter "Travel Date" in the Parse Dates field.
	* Keep other options as default and click Save.
2. **Load Example Data and Dashboards:**
	* Create a file named "my\_values.yaml".
	* Deploy the configuration as instructed in the Configure your setting overrides section.
3. **Log in to Superset:**
	* Access your local Superset instance at [http://localhost:8088](http://localhost:8088/?ref=blog.elest.io).
	* Log in using the default credentials:
		+ Username: admin
		+ Password: admin

Add the following configuration to enable loading examples:


```
init:
  loadExamples: true

```
Following these steps allows users to efficiently import data into Superset and begin exploring its features. The CLI commands simplify the setup process, facilitating a smoother start to data analysis.

## Configuring Superset with the CLI

  
Apache Superset's command\-line interface (CLI) provides an efficient way to configure the platform, preparing it for seamless data exploration. Follow these steps to configure Superset using the CLI:

1. **Accessing Superset:**
	* Navigate to [http://localhost:8088](http://localhost:8088/?ref=blog.elest.io) and log in with the admin credentials you created.
2. **Configuration File:**
	* Customize your Superset instance by creating a superset\_config.py file.
	* Set the SECRET\_KEY and any other desired configurations.
	* Refer to the official documentation for a comprehensive list of available settings.
3. **Security:**
	* Ensure that the SECRET\_KEY is set to a secure, randomly generated value, especially for production environments.
	* Follow additional security measures outlined in the official documentation for enhanced security posture.

Start the development server:


```
superset run -p 8088 --with-threads --reload --debugger

```
Build the frontend assets:


```
cd superset-frontend
npm ci
npm run build
cd ..

```
Initialize Superset:


```
superset init

```
Optionally, load example data:


```
superset load_examples

```
Create an admin user:


```
export FLASK_APP=superset
superset fab create-admin

```
Upgrade the database:


```
superset db upgrade

```
Install the apache\-superset package:


```
pip install apache-superset

```
## Running the Superset Web Server Using the CLI

  
To initiate the Apache Superset web server via the command\-line interface (CLI), follow these steps post the installation and initialization of Superset:

1. Set the `FLASK_APP` environment variable:


```
export FLASK_APP=superset

```
1. Create an admin user:


```
superset fab create-admin

```
1. Optionally, load example data:


```
superset load_examples

```
1. Initialize Superset with default roles and permissions:


```
superset init

```
1. If frontend assets have been built, navigate to the superset\-frontend directory and execute:


```
npm ci
npm run build

```
1. To launch the development server on port 8088 (or an alternative port using the \-p option):


```
superset run -p 8088 --with-threads --reload --debugger

```
1. Access Superset by opening [http://localhost:8088](http://localhost:8088/?ref=blog.elest.io) in your web browser. Log in using the admin credentials established earlier. For production environments, ensure the SECRET\_KEY is properly configured following official guidelines.

## Cloning the Superset Repository via Command Line

  
To clone the Apache Superset repository using the command line, follow these steps:

1. Open your terminal application.
2. Navigate to the directory where you want to clone the repository using the cd command:


```
cd /path/to/parent/directory

```
1. Execute the following command to clone the repository:


```
git clone https://github.com/apache/superset.git

```
1. Wait for the cloning process to finish. Once completed, you will find a new directory named "superset" in your current working directory, containing the cloned repository.

Ensure that Git is installed on your system before running the clone command. You should also be familiar with basic command\-line operations to navigate directories and execute commands.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the Elestio resources and Official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.elest.io) to learn more about Superset. You can click the button below to create your service on [Elestio](https://elest.io/open-source/superset?ref=blog.elest.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/open-source/superset?ref=blog.elest.io)

