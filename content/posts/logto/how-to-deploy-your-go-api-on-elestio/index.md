---
draft: true
title: "How to Deploy Your Go API on Elestio"
date: "2024-07-01"
description: "As a developer, you might have built multiple APIs and integrated them with your web application. So, In today's tutorial, we are going to see how you can quickly build a simple Ping-Pong API and deploy it easily and quickly on Elestio.


Let's set it up!"
tags: []
categories: [Identity and access management]
cover:
  image: images/cover.png
  caption: "How to Deploy Your Go API on Elestio"
ShowToc: true
TocOpen: true
---


As a developer, you might have built multiple APIs and integrated them with your web application. So, In today's tutorial, we are going to see how you can quickly build a simple Ping\-Pong API and deploy it easily and quickly on Elestio.

## Let's set it up!

I presume you already have an API ready that you want to deploy. But for this tutorial, I will start you through the steps from the very beginning so feel free to skip some steps (But remember not all) as your codebase will need some changes to make your deployment successful. Let's start with creating a GitHub repository for your API

![Create new repository image](https://cdn.hashnode.com/res/hashnode/image/upload/v1697183826205/a1cb46c9-09a2-4800-a46c-e8dd301960b0.png)![Repository description](https://cdn.hashnode.com/res/hashnode/image/upload/v1697184196077/f3d3474d-2c0d-420b-ba77-daafa4fa6c70.png)Next, we will go ahead and open this newly created repository in GitHub Codespaces. As I said if you already have the repo I recommend you use GitHub Codespaces or the code editor where you have already set your project

![Creating a codespace](https://cdn.hashnode.com/res/hashnode/image/upload/v1697184355817/780a091c-c667-4064-b7f9-103872b23c63.png)## Building your Go API

This is an optional step, if you already have an API, please feel free to skip this

Once the codespaces are launched, head over to the terminal and enter the following command that will create a `.mod`folder in the repository


```
go mod init github.com/<username>/<repo-name>
```
![Initialize go module](https://cdn.hashnode.com/res/hashnode/image/upload/v1697184442941/e37d6b35-3227-4fea-b81b-0d461c051b26.png)Next, create `main.go` file in the root directory

![Creating additional files](https://cdn.hashnode.com/res/hashnode/image/upload/v1697184614177/0cdcd6e2-96a0-4f09-b5a8-0ebc33611c05.png)Inside `main.go` file add the following code. In this tutorial, I won't be explaining the code if you want that let me know in the comments and I will get you a dedicated tutorial on it.


```
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {

	fmt.Println("Welcome to the Ping-Pong API")

	//Initializing the gin package
	router := gin.Default()

	//Endpoint we are going to use today
	router.GET("/ping", handlePing)

	//Server runs on everywhere IP and on 8080 port
	router.Run("0.0.0.0:8080")
}

//Function to handle the /ping endpoint
func handlePing(g *gin.Context) {
	g.IndentedJSON(http.StatusOK, gin.H{"message": "Pong!"})
}
```
After you have added the code `main.go` file, head over to the terminal and run the following command. It will create a `.sum` file with all the required libraries mentioned in `.mod` the file


```
go get .
```
![Install the dependencies](https://cdn.hashnode.com/res/hashnode/image/upload/v1697186476988/788d2dfd-f18e-4eb3-8e4b-06eb822cb326.png)After this, you can try out running your API and testing the `/ping` endpoint using curl or the "Open in browser" option

![Starting the go server](https://cdn.hashnode.com/res/hashnode/image/upload/v1697186613394/8b5fc905-98b2-4d1e-850a-09a757901042.png)## Deploying your API

Go ahead and create another file called `elestio.yaml` in your root directory and add the following code to it


```
config:
  runTime: "GO"
  version: ""
  framework: "GO"
  buildCommand: "go build -o main"
  buildDir: "./"
  runCommand: "./main"
ports:
  - protocol: "HTTPS"
    targetProtocol: "HTTP"
    listeningPort: "443"
    targetPort: "8080"
    targetIP: "172.17.0.1"
    public: true
    path: "/"
    isAuth: false
    login: ""
    password: ""
exposedPorts:
  - protocol: "HTTP"
    hostPort: "8080"
    containerPort: "8080"
    interface: "172.17.0.1"
environments:
  - key: "ENV"
    value: "production"
webUI:
  - url: "https://[CI_CD_DOMAIN]/ping"
    label: "Website"
```
This file states the configurations for your applications like the build and run commands you want to run to start your go API, then ports. Here the reverse proxy configuration is listening to the port `443` of the public IP address and the port `8080` is the port exposed by the Docker containers. All the traffic to the port `443` will be redirected to the port `8080` . Environment variables are stated with the `webUI` link you want to show to quickly access the API from the Elestio dashboard.

After adding this file, commit your code to the repository.

Now go to [Elestio](https://elest.io/?ref=blog.elest.io), and login and set up the account if you don't already have one set up.

Click on the "CI/CD" section from the left panel select your repository host and the repository that has your Api and click on "Import"

![Creating a CI/CD pipeline with GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1697188471160/75796412-269c-4232-a3dd-995f7876511e.png)Now select your preferred cloud service provider

![Choose service cloud provider](https://cdn.hashnode.com/res/hashnode/image/upload/v1697189373127/18acfa85-bd9b-40ca-9cd9-f5b9dc2e5a31.png)Give the deployment a name of your choice (You can keep the default name too)

![Creating the service](https://cdn.hashnode.com/res/hashnode/image/upload/v1697189920163/0a511ccc-3c01-4004-8593-80d5c9df0c50.png)Add a name to your project and Create a CI/CD pipeline

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1697190442682/2aa16bc2-860a-4c81-8440-23508c62d52d.png)Awesome! You have successfully created a CI/CD pipeline that gets your API to the VMs.

Moving next, click on the "Services" Tab on the left and click on the service you just created.

![Checkout the service](https://cdn.hashnode.com/res/hashnode/image/upload/v1697190814193/e1f9be91-8c6a-4e3b-89ce-20e4b9f65ce4.png)Now check all the information on the overview if you want else head over to the Pipeline tab

![checkout the pipeline](https://cdn.hashnode.com/res/hashnode/image/upload/v1697191075496/602722f6-aaec-4873-9d24-a31998cce576.png)After heading inside you will find an option "Website" Click on it and head over to the link provided in it. It's the API endpoint.

![checkout the website](https://cdn.hashnode.com/res/hashnode/image/upload/v1697191476466/2f9c71f0-6233-47a4-8ef6-e75d3257dbe4.png)![Click on the url provided](https://cdn.hashnode.com/res/hashnode/image/upload/v1697191526854/34347d9c-7692-4cf7-9497-99b88f53b3db.png)Note that because we only had `/ping` endpoint, I appended it to the URL provided in the configs. In the general scenario as you have multiple endpoints you can choose the URL to not append `/ping` and change it to `/`

As mentioned above if you have multiple API endpoints then it's a bad idea to add them to the URL, you can remove the `/ping` to get displayed in the URL by updating the `elestio.yaml` in your code to the following


```
#Before
webUI:
  - url: "https://[CI_CD_DOMAIN]/ping"
    label: "Website"
#=======================================================
#After
webUI:
  - url: "https://[CI_CD_DOMAIN]/"
    label: "Website"
```
## Accessing your API

You can directly click on the link provided in the dashboard and you will see your response as follows

![API response](https://cdn.hashnode.com/res/hashnode/image/upload/v1697191774850/979da304-9361-4986-a974-9882a3aeac47.png)or you can make a curl request from the terminal in your local computer like


```
curl <url-from-the-dashboard>/ping
```
## Where to go from here?

You can now successfully go ahead and insert this URL into your frontend application and fetch the responses from the new hosted API endpoints. Additionally, you can integrate your Go API with a couple of other databases (again all of them are present on Elestio to easily configure).

More tutorials around the same will be published to help your Go API integrate seamlessly with different databases and effortlessly host them onto Elestio

## Thanks for reading ❤️

If you like the blog, then do try out creating your pipelines and if you want to support us then you can add the "Deploy on Elest.io" button to your open source project. Well, that's it for this blog, we will catch up with you in the next one 👋

![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)

