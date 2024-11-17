---
draft: true
title: "What is OpenTofu? - A quick introduction!"
date: "2024-04-21"
description: "Hello everyone, welcome to the introduction of a brand new open-source tool. Although the name sounds a bit abstract there is a good purpose behind it and that's exactly what I am going to tell you about today. So without any further due let's understand more"
tags: []
categories: [Other]
cover:
  image: images/cover.png
  caption: "What is OpenTofu? - A quick introduction!"
ShowToc: true
TocOpen: true
---


Hello everyone, welcome to the introduction of a brand new open\-source tool. Although the name sounds a bit abstract there is a good purpose behind it and that's exactly what I am going to tell you about today. So without any further due let's understand more about OpenTofu and how is it trying to create a difference in the Infrastructure as code (IaC) segment of cloud infrastructure development.

![OpenTofu Logo](https://www.linuxfoundation.org/hs-fs/hubfs/OpenTofu.png?width=1640&height=924&name=OpenTofu.png)## A little background story!

Terraform was opensourced in 2014 under Mozilla Public License (v2\.0 MPL). For over 9 years a community was built with contributors, customers, vendors, practitioners etc. But on August 10 2023, HashiCorp switched the license of Terraform from MPL to a Business Source License (v1\.1 BUSL) which is a non\-open source license.

![OpenTofu is public fork of Terraform](https://cdn.hashnode.com/res/hashnode/image/upload/v1699363293928/18e13a5b-cb64-4842-a12f-4542d9649eef.webp)## What is OpenTofu?

OpenTofu is a fully open\-source fork of Terraform. OpenTofu will be managed under a Linux foundation similar to how Linux is managed with the help of multiple companies and contributors. OpenTofu was announced at [Open Source Summit Europe 2023](https://youtu.be/_-9LhcPgoaY?list=PLbzoR-pLrL6pDxQxPguJTiqVC31JtMgxd&ref=blog.elest.io) and on 14th August 2023 published an [OpenTofu manifesto](https://opentofu.org/manifesto/?ref=blog.elest.io) followed by officially launching as a Linux Foundation project on 20th August 2023\. OpenTofu has crossed over 15K public stars on GitHub and is being supported by multiple organisations. Some organisations have even pledged software engineers over a period of time to work on OpenTofu and contribute to its engineering.

![OpenTofu announcement image](https://cdn.hashnode.com/res/hashnode/image/upload/v1699363433423/28d16e90-1c40-45c5-a97b-d5b08c103639.png)## Why do we need OpenTofu?

Terraform's main value proposition was its ecosystem with providers and modules around it. Many providers created their modules so that consumers can use them with their cloud service providers. OpenTofu mainly desires to maintain this open\-source spirit of the tool and keep providing that.

OpenTofu provides drop\-in migration that is compatible with Terraform `1.5.7` and `1.6` to help organisations and users effortlessly migrate from Terraform to OpenTofu. OpenTofu will be open\-sourced forever and won't be subject to the whims of a single vendor. OpenTofu envisions becoming a community\-driven project where the community governs the project for the community and contributions will be regularly reviewed and accepted fostering innovation.

OpenTofu includes some of its ideas which the community requested heavily for some time including state encryption and support for OCI registries

![OpenTofu image](https://cdn.hashnode.com/res/hashnode/image/upload/v1699363319096/de808443-8cdd-4d32-9635-9672113ab7f0.png)## Question of hidden implications

The known bugs and issues from the Hashicorp repository are being opened by the community members on the OpenTofu repository to incorporate them moving forward. There are also different providers with Terraform, so the question arises if there are any provisions to make those providers available for OpenTofu, so the answer is yes, OpenTofu registry adapts the GitHub redirected and enables you to use all those providers without any action taken.

OpenTofu plans to remain compatible with the newer releases of Terraform as long as possible but the project is still under planning out the specifics and encourages contributors to submit an issue or pull request if they feel support for a specific thing is missing in OpenTofu. For now, OpenTofu doesn't plan on changing anything in API and rerouting. The project is prioritising compatibility so the only major thing for the switch would be the CLI commands.

## Resources

* [OpenTofu Project Overview \- Open Source Summit Europe 2023](https://youtu.be/_-9LhcPgoaY?si=PsFTCWadVyDOircv&ref=blog.elest.io)
* [OpenTofu Blogs](https://opentofu.org/blog?ref=blog.elest.io)
* [OpenTofu Documentation](https://opentofu.org/docs/intro/?ref=blog.elest.io)
* [OpenTofu Manifesto](https://opentofu.org/manifesto?ref=blog.elest.io)
* [Elestio Terraform Registry](https://registry.terraform.io/providers/elestio/elestio/latest?ref=blog.elest.io)

## Thanks for reading ❤️

And that's it for this blog, thank you so much for reading. Do check out the resources provided to learn more about the OpenTofu project. You can click the button below to create your service on [Elestio](https://elest.io/?ref=blog.elest.io) and copy the terraform config of your service to try out OpenTofu. We will see how to set up and use OpenTofu in upcoming blogs 👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](http://dash.elest.io/?ref=blog.elest.io)

