---
draft: true
title: "Superset Nginx timeout guide"
date: "2024-03-18"
description: "Discover troubleshooting tips to resolve Superset Nginx timeout issues effectively.


Understanding Superset and Nginx Timeout Issues

When running Apache Superset behind an Nginx reverse proxy, users might face 504 Gateway Timeout errors. These errors usually occur when Nginx doesn't get a timely response from the Superset server, often"
tags: []
categories: [Business Intelligence]
cover:
  image: images/cover.png
  caption: "Superset Nginx timeout guide"
ShowToc: true
TocOpen: true
---


Discover troubleshooting tips to resolve Superset Nginx timeout issues effectively.

## Understanding Superset and Nginx Timeout Issues

When running Apache Superset behind an Nginx reverse proxy, users might face `504 Gateway Timeout` errors. These errors usually occur when Nginx doesn't get a timely response from the Superset server, often due to the server handling long\-running queries. To address this, Superset includes a client\-side timeout limit that shows a warning message before the gateway timeout happens.

### Configuring Timeouts

Open your app on VS CODE using the tools tab, then locate the file `superset_config.py` and adjust the `SUPERSET_WEBSERVER_TIMEOUT` parameter to align with or exceed the timeout settings in Nginx.


```
SUPERSET_WEBSERVER_TIMEOUT = 60  # seconds

```
**SQL Lab Async Timeout:** Increase the `SQLLAB_ASYNC_TIME_LIMIT_SEC` parameter to accommodate longer\-running queries in SQL Lab.


```
SQLLAB_ASYNC_TIME_LIMIT_SEC = 60 * 60 * 6  # 6 hours
```
**Celery Configuration:** Adjust Celery's task time limit to ensure queries have ample time to complete before being terminated.


```
CELERYD_TASK_TIME_LIMIT = 60 * 60 * 6  # 6 hours
```
Properly configuring these settings will help manage long\-running queries effectively, preventing premature termination and ensuring smoother operation.

**Nginx Configuration:** Set the `proxy_read_timeout` directive in Nginx's configuration to a sufficiently high value to accommodate long\-running queries.


```
proxy_read_timeout 120s;

```
By ensuring these configurations are properly set, you can prevent timeout issues and improve the performance of Apache Superset when running behind an Nginx reverse proxy.

### Configuring Nginx for Improved Superset Performance

  
Optimizing Nginx for Superset involves several crucial configurations to ensure efficient handling of client requests and seamless communication with the Superset application. Below are the steps and settings to consider for enhancing Superset's performance when using Nginx as a reverse proxy.

### Timeout Settings

  
Adjust the proxy\_read\_timeout and proxy\_connect\_timeout directives in your Nginx configuration to prevent timeouts during long\-running Superset queries:


```
proxy_read_timeout 300;
proxy_connect_timeout 300;

```
### Client\-Side Timeout

  
Align the client\-side timeout in superset\_config.py with Nginx's timeout settings:


```
SUPERSET_WEBSERVER_TIMEOUT = 300

```
### Buffer Size

  
Increase buffer sizes to handle larger requests, especially beneficial for extensive dashboards or datasets:


```
proxy_buffers 16 32k;
proxy_buffer_size 64k;

```
### Web Server Workers

  
Optimize the number of Nginx worker processes to match the available CPU cores and adjust worker\_connections to handle multiple connections:


```
worker_processes auto;
worker_connections 1024;

```
### Static Asset Caching

  
Implement caching for static assets to reduce load times and enhance user experience:


```
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 365d;
    add_header Cache-Control "public, no-transform";
}

```
### SSL Configuration

  
Ensure SSL is correctly configured for secure connections. Refer to the official Nginx documentation for setting up SSL certificates and configurations.

### Health Checks

  
Set up health checks to monitor the Superset application's status:


```
location /health {
    proxy_pass http://superset_app_server/health;
}

```
## Addressing Superset Timeout Errors Behind Nginx

  
When Apache Superset is utilized behind an Nginx reverse proxy, encountering 504 Gateway Timeout errors is not uncommon. This issue typically arises when Nginx fails to receive a prompt response from the Superset server, often due to processing long\-running queries. To resolve this, consider the following steps:

**Increase Nginx Timeout:** Adjust the proxy\_read\_timeout and proxy\_connect\_timeout directives in your Nginx configuration to extend the waiting period for responses.

**Adjust Superset Configuration:** Modify the `SUPERSET_WEBSERVER_TIMEOUT` in superset\_config.py to match the extended timeout settings in Nginx.

**Client\-Side Timeout:** To prevent gateway timeout messages, adjust the `SQLLAB_ASYNC_TIME_LIMIT_SEC` in Superset to allow for longer query execution times.

**Health Check Endpoint:** Employ the /health endpoint to ensure that your load balancer accurately identifies the Superset instance's status.

**Proxy Headers:** If utilizing X\-Forwarded\-For/X\-Forwarded\-Proto headers, enable `ENABLE_PROXY_FIX = True` in superset\_config.py.

**WSGI Server Configuration:** If Gunicorn is not used, disable flask\-compress by setting `COMPRESS_REGISTER = False`.

**Database Considerations:** Opt for performance and reliability by configuring the metadata database, favoring PostgreSQL or MySQL over SQLite for production environments.

**Monitoring and Logging:** Implement comprehensive logging and monitoring mechanisms to pinpoint slow queries and performance bottlenecks effectively.

**Caching:** Employ caching strategies to alleviate the database load and enhance response times.

**Asynchronous Query Execution:** Utilize Celery workers for asynchronous query execution, mitigating timeouts during prolonged operations.

## Advanced Nginx Configuration for Large Superset Dashboards

  
When setting up Nginx for extensive Superset dashboards, prioritizing timeouts and resource allocation is essential for a seamless user experience. Here are some advanced configurations to consider:

### Increasing Timeouts

  
To prevent gateway timeouts (504 errors), adjust the proxy\_read\_timeout and proxy\_connect\_timeout in your Nginx configuration:


```
proxy_read_timeout 300;
proxy_connect_timeout 300;

```
### Optimizing Client Body Size

  
Tailor the client\_max\_body\_size to accommodate substantial dashboard payloads:


```
client_max_body_size 50M;

```
### Enabling WebSocket Support

  
For real\-time updates, verify that Nginx supports websockets:


```
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    ...
    location /ws {
        proxy_pass http://superset_app;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}

```
### Configuring Caching

  
Leverage Nginx's caching capabilities to enhance load times:


```
proxy_cache_path /path/to/cache levels=1:2 keys_zone=superset_cache:10m max_size=1g inactive=60m use_temp_path=off;

server {
    ...
    location /static/ {
        proxy_cache superset_cache;
        ...
    }
}

```
### Implementing Load Balancing

  
When managing multiple Superset workers, implement Nginx's load balancing:


```
upstream superset_app {
    server superset1.example.com;
    server superset2.example.com;
    ...
}

```
## **Thanks for reading ❤️**

Thank you so much for reading and do check out the Elestio resources and Official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.elest.io) to learn more about Superset. You can click the button below to create your service on [Elestio](https://elest.io/open-source/superset?ref=blog.elest.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/open-source/superset?ref=blog.elest.io)

