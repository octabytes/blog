---
draft: true
title: "Deploy examples & apps on Elestio using the 'Import Third-Party Git Repository' feature"
date: "2024-04-19"
description: "This tutorial will walk you through the process of deploying GitHub, GitLab, or Bitbucket public repositories in CI/CD using our Import Third-Party Git Repository feature. In our example, we'll use a Simple JavaScript web application public repository, but you can deploy it, in the same way, using"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "Deploy examples & apps on Elestio using the 'Import Third-Party Git Repository' feature"
ShowToc: true
TocOpen: true
---


This tutorial will walk you through the process of deploying GitHub, GitLab, or Bitbucket public repositories in CI/CD using our **Import Third\-Party Git Repository** feature. In our example, we'll use a Simple JavaScript web application public repository, but you can deploy it, in the same way, using any public repository from ***GitHub***, ***GitLab***, or ***Bitbucket***. 🚀

#### What is the Import Third\-Party Git Repository?

A feature of Elestio's CI/CD **Import Third\-Party Git Repository** lets you deploy any type of public git repository from *GitHub*, *GitLab*, or *Bitbucket* in the Elestio cloud.

#### What is the difference between Import Git Repository And Import Third\-Party Git Repository?

Only public or private repositories that are already in your own git account can be deployed using the ***Import Git Repository*** feature. Depending on the deployment method you select—for example if you choose GITHUB—you can only deploy repositories that are already in your github account. On the other hand, you can deploy any only public repository from your or anyone else's account from github, gitlab, or bitbucket using the **Import Third\-Party Git Repository** feature.


> In these **Import Third\-Party Git Repository** features, Elestio will create a repository from your entered repository URL in your git account and deploy it to the cloud.

You probably heard about Kubernetes (and all its complexity) or various options to deploy your apps like Heroku, Render Fly, or Railways. They all have something in common, those products are building your own source code on every commit from your GIT repository.

Elestio is doing the same ...  **but different!** Instead of deploying your app to a shared cluster, we deploy to dedicated VMs.


> To learn more about the elestio CI/CD, go *[**here**](https://docs.elest.io/books/cicd-pipelines/page/overview?ref=blog.elest.io).*

If you're new, sign up for *[Elestio](https://dash.elest.io/?ref=blog.elest.io)*, otherwise, login to your existing account.

#### **Deploy Any Public repository Apps to the cloud using the CI/CD Import Third\-Party Git Repository feature.**

#### Step 1:

Go to CI/CD from the left sidebar.

#### Step 2:

Now, select the deployment source.

[![Screenshot 2022-11-02 185434.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-185434.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-185434.png?ref=blog.elest.io)In this tutorial, I'm deploying using GITHUB, but you can also use GITLAB if you want to deploy your repository there.

#### Step 3:

Click the Import a Third\-Party Git Repository

[![Screenshot 2022-11-16 202720.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-16-202720.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-16-202720.png?ref=blog.elest.io)The URL of the public repository you want to deploy should now be entered here.

Now click the ***Continue*** button to proceed.


> If you have already authenticated your GITHUB or GITLAB account in CI/CD for repository access, you can fill up the below details directly. Otherwise, you must first authenticate your GIT account with elestio CI/CD for repository creation into your account.

We require GIT authentication in order to create these example template repositories in your GIT account.

[![Screenshot 2022-11-16 202936.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-16-202936.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-16-202936.png?ref=blog.elest.io)Here you can check the checkbox ***Create private Git Repository*** if you want to make these repo private otherwise leave it unchecked and click the ***Next button*** for further steps.

#### Step 4:

Choose Deployment Targets

[![Screenshot 2022-11-02 191657.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-191657.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-191657.png?ref=blog.elest.io)Elestio offers two types of deployment targets "**Deploy on a  new VM**" and "**Deploy on an existing VM**".

You are allowed to set up n pipelines on each elestio CI/CD target/VM. According to the project configuration you select and the project you're deploying, the number of pipelines varies.

If you want to deploy these projects as a pipeline on a new Target/VM or don't have any installed targets, choose "Deploy on a new VM." If you already have any installed or previously configured CI/CD targets/VMs, choose "Deploy on an existing VM," and then choose the existing target from the targets dropdown.

Follow the steps below only if you select "**Deploy on a new VM**," otherwise click the next button to proceed.

CI/CD Pipelines by Elestio are available with our 5 cloud partners (AWS Lightsail, Digital Ocean, Vultr, Linode \& Hetzner) in 85 locations over 27 countries but also on any cloud (AWS, Azure, Google, Oracle, ...) and on\-premise with [BYOVM.](https://doc.elest.io/books/cloud-providers/page/byovm-bring-your-own-vm?ref=blog.elest.io)

* Select Service Cloud Provider

[![Screenshot 2022-11-02 194154.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-194154.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-194154.png?ref=blog.elest.io)* Select Service Cloud Region

[![Screenshot 2022-11-02 194242.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-194242.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-194242.png?ref=blog.elest.io)* Select Service Plan

[![Screenshot 2022-11-02 194721.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-194721.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-194721.png?ref=blog.elest.io)* Now Customize the target name and project (where the CICD Target will be created).

[![Screenshot 2022-11-02 194857.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-194857.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-194857.png?ref=blog.elest.io)
> If you want to deploy it with a different name and a different project, you can customize it. By default, we configure it with a dynamic target name and the current project.

#### Step 5:

Configure your Project

[![Screenshot 2022-11-04 200938.png](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-04-200938.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-195655.png?ref=blog.elest.io)You can configure the project details by filling up the project name, branch, run time, version, framework, and root directory.

[![Screenshot 2022-11-04 201013.png](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-04-201013.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-200718.png?ref=blog.elest.io)You can configure your project install, run, and build commands in the Build and output setting.

[![Screenshot 2022-11-02 201628.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-201628.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-201628.png?ref=blog.elest.io)The configuration of life cycle scripts is always optional; they should only be used if you want to execute a specific command before and after building your project. Otherwise, leave them empty.

[![Screenshot 2022-11-02 201356.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-201356.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-201356.png?ref=blog.elest.io)You can list all of your project's API keys and secrets here if they were saved in ENV

[![Screenshot 2022-11-04 201102.png](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-04-201102.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-202142.png?ref=blog.elest.io)[![Screenshot 2022-11-02 202154.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-202154.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-202154.png?ref=blog.elest.io)The final step is to configure the exposed port and reverse proxy settings. You can specify the port on which your project will run here.


> If your project includes **elestio.yml**, Elestio will auto\-fill all of these fields. As in this tutorial, we're using our Simple Javascript web application elestio example repository, so you can see in the above images that all of our fields are auto\-filled.

Refer to these links to learn how to create our own ***[elestio.yml](https://docs.elest.io/books/cicd-pipelines/page/create-your-own-template-elestioyml?ref=blog.elest.io)*** for the project.

A sample elestio.yml for our deploying Simple Javascript web application is shown below. check it out on ***[github](https://github.com/elestio-examples/static/blob/main/elestio.yml?ref=blog.elest.io)***


```
config:
  runTime: "static"
  version: ""
  framework: ""
  buildCommand: ""
  buildDir: ""
  runCommand: ""
ports:
  - protocol: "HTTPS"
    targetProtocol: "HTTP"
    listeningPort: "443"
    targetPort: "3000"
    targetIP: "172.17.0.1"
    public: true
    path: "/"
    isAuth: false
    login: ""
    password: ""
exposedPorts:
  - protocol: "HTTP"
    hostPort: "3000"
    containerPort: "80"
    interface: "172.17.0.1"
```
#### Step 6:

Click the ***Create CI/CD pipeline*** button to deploy your pipeline.

[![Screenshot 2022-11-02 203203.png](https://docs.elest.io/uploads/images/gallery/2022-11/scaled-1680-/screenshot-2022-11-02-203203.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-203203.png?ref=blog.elest.io)*In a couple of moments, your application was successfully deployed on elestio 🚀.*

[![Screenshot 2022-11-04 202011.png](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-04-202011.png)](https://docs.elest.io/uploads/images/gallery/2022-11/screenshot-2022-11-02-205451.png?ref=blog.elest.io)[![Untitled-video-Made-with-Clipcha (3).gif](https://docs.elest.io/uploads/images/gallery/2022-11/untitled-video-made-with-clipcha-3.gif)](https://docs.elest.io/uploads/images/gallery/2022-11/untitled-video-made-with-clipcha-2.gif?ref=blog.elest.io)You can now view your deployed URL and access your application by going to desired application pipeline details.

Please let us know by contacting our support [***email***](mailto:support@elest.io) or ***[ticketing](https://dash.elest.io/support/creation?ref=blog.elest.io)*** system if you give it a shot and encounter any problems or if anything goes wrong.

Join us on [***discord***](https://discord.gg/4T4JGaMYrD?ref=blog.elest.io) to know more.



