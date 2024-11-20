---
draft: true
title: "Embedding Superset dashboards in your React application"
date: "2024-12-02"
description: "We will knowing more about embedding Superset dashboards in your react application.


Maximizing Data Insights: Integrating Superset's Image Export with External Applications

Apache Superset stands out as a powerful tool for data visualization, boasting a user-friendly interface for rapid chart creation across diverse databases. Among its extensive feature"
tags: []
categories: [Business Intelligence]
cover:
  image: images/cover.png
  caption: "Embedding Superset dashboards in your React application"
ShowToc: true
TocOpen: true
---


We will knowing more about embedding [Superset](https://octabyte.io/open-source/superset?ref=blog.octabyte.io) dashboards in your react application. 

### Maximizing Data Insights: Integrating Superset's Image Export with External Applications

Apache Superset stands out as a powerful tool for data visualization, boasting a user\-friendly interface for rapid chart creation across diverse databases. Among its extensive feature set, Superset facilitates the seamless export of visualizations as images, streamlining the sharing of insights without direct platform access. Furthermore, Superset empowers users to embed dashboards into external applications through iframes, facilitating the integration of data analytics directly into web environments.

#### Empowering Data Analytics with Embedded Dashboards

Embedded dashboards serve as a conduit, delivering profound data analytics directly into web applications. Leveraging Superset's Embedded SDK, users effortlessly integrate Superset dashboards into their applications, utilizing the app's authentication system. This embedding process entails inserting an iframe housing a Superset page into the host application, enabling users to access integrated dashboards seamlessly, provided they're logged into the host app.

#### Objectives

* Seamlessly access Superset graphs within React applications.
* Implement multi\-tenancy support for Embedded Dashboards.
* Employ Role\-Level Security (RLS) for robust access control.

#### Prerequisites

* Docker or Docker Compose.
* Functional React\-based app alongside its backend.

#### Superset Configuration

Ensure Superset is configured correctly, especially by enabling the EMBEDDED\_SUPERSET feature flag in `superset_config.py`.

#### Client App (React) Integration

Integrating Superset's embedded dashboard into React applications involves embedding the dashboard within an iframe. Here's a code snippet demonstrating the embedding process:


```
import { embedDashboard } from "@superset-ui/embedded-sdk";

const token = await fetchGuestTokenFromBackend(config);

embedDashboard({
    id: "abcede-ghifj-xyz", // Embedded Dashboard UUID
    supersetDomain: "https://[ELESTIO_CNAME]",
    mountPoint: document.getElementById("superset-container"), // HTML element to render iframe
    fetchGuestToken: () => token,
    dashboardUiConfig: { hideTitle: true }
});

```
## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.octabyte.io) to learn more about Superset. You can click the button below to create your service on [OctaByte](https://octabyte.io/open-source/superset?ref=blog.octabyte.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://octabyte.io/open-source/superset?ref=blog.octabyte.io)

