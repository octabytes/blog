---
draft: false
title: "immudb & Minio: immutable ledger database instead connected to an object storage. A fast and safe alternative to blockchains."
date: "2024-11-20"
description: "immudb is an immutable database that offers a high-performance alternative to blockchains and centralized systems like AWS QLDB. It provides versioned, timestamped, and cryptographically verifiable data storage, making it ideal for secure and tamper-proof applications. It supports both SQL and NoSQL and can be integrated with storage solutions like MinIO for scalability. Additionally, it offers SDKs, REST API, and a web UI for easy interaction."
tags: [immutable, database, open-source, blockchain, ledger, SQL, NoSQL, MinIO, cloud, storage, security, audit, compliance, supply chain, finance, identity management, Prometheus, SDK, REST API, web UI]
categories: [Databases, Specialized databases]
cover:
  image: images/cover.png
  caption: "immudb & Minio: immutable ledger database instead connected to an object storage. A fast and safe alternative to blockchains."
  relative: true
ShowToc: true
TocOpen: true
---


Traditional database transactions and logs are mutable, and therefore there is no way to know for sure if your data has been compromised. immudb is immutable. You can add new versions of existing records, but never change or delete records. 

This lets you store critical data without fear of it being tampered as immudb automatically stores the data versioned, timestamped and cryptographically verifiable..

In some situations it’s not possible or cost effective to use blockchains because of high latencies, high transaction fees or data size limits. Same is true for AWS QLDB, that is centralized, too slow for many applications and with a full vendor lock\-in.

immudb is a great **open\-source alternative to blockchains** and other ledger technologies. Unlike these, immudb can handle millions of transactions per second, supports KV and SQL as well as BLOBs.  


**Use cases**

* Bank / Finance / Insurance
* Regulatory Compliance and Audit
* Supply Chain Management
* Identity Management

**SQL and/or NoSQL** 

Immudb can operate both as a key\-value store, and/or as a relational database (SQL). 

**Separating compute and storage**

Immudb can store its data in an AWS S3 bucket or a compatible alternative. Here we are going to use Minio to deploy an object storage with low latency close to the immudb instance. That way the increased storage space usage over time is easy to manage and the performance much better than AWS S3\. On OctaByte It’s possible to resize network disks up to 10 TB per volume. You can also create a cluster of several MinIO instances to enable high availability and increase the global storage size.  


**SDK, REST API and Web UI**

SDKs are available for Java, Go, .NET, Python and Node.js. A REST API is available for all other languages. A web UI (Port 8080\) is available, it provides some metrics and allows to browse the db and execute queries. When using Prometheus to monitor applications you can leverage the built\-in metrics export running on port 9497 on /metrics.

![](images/trqsvyC1fyj-foiyXTUjR1ZyFFTYT8hZKQIrwmpv1dgzOQpJZDPvKeg0kXUfFEw1WZ4gbNZ62usrLmq3dh6Jq6KWFEaEZldgkdsWVNChnemE7Fjkk_2CNEt64Hgb9MHoVTtwVYRfc_vCiMph-w)  
**Get a running instance of immudb in few minutes**  
OctaByte makes it easy to deploy a dedicated instance of immudb on any cloud, we take care of providing the cloud resources (except if you prefer to [BYOVM](https://docs.elest.io/books/cloud-providers/page/byovm-bring-your-own-vm?ref=blog.octabyte.io) or deploy on\-premise) and doing all the devOps part including security, reverse proxy with SSL configuration, monitoring/alerts, backups, updates and migrations.   
  


## Quickstart

**Step 1: deploy a dedicated immudb instance**  
click here: [https://octabyte.io/databases/specialized-databases/immudb](https://octabyte.io/databases/specialized-databases/immudb)

![OctaByte dashboard > Services > New](images/623C2wihgsCCfKctGqYum9wvoIIKnBmXyLQNv3gmMhvOlmGn4FbBtx62XCTIt7APxypIzDUoCMGSsBGvIM-i8kVoIuRDskz0zEmXWU3HaPDffV_RZpgZURIcaK1wJHnzjrGw_AnSHLXqo8I6Dw)

OctaByte dashboard \> Services \> New

  
There you can select your prefered cloud provider or use [BYOVM](https://docs.elest.io/books/cloud-providers/page/byovm-bring-your-own-vm?ref=blog.octabyte.io) to deploy on your own cloud or on\-premise. Then select your prefered region, it should be as close as possible to your users. We have a selection of 80 datacenters in 27 countries.

Then choose the instance size from 1 CPU/1GB RAM up to 32 CPU/128GB RAM

Finally click on the “Create service” button. Few minutes later your immudb instance will be ready to use. You will receive by email a quickstart with few samples.  


![OctaByte dashboard > Services > Overview of immudb instance](images/TWvZzWuypSpiLNNQN-yBxsfG2J9y0ZZPpbeaKgamXkagVez02dskW6Jmu2Fg2MK8vwTEfLQopbEjS6fb5YwQ-kRLUhfshgl7lDT3fkFsu4uVRmjM6e5YonOYjA7RC-eK4iFho85AV2jSKy5SKw)

OctaByte dashboard \> Services \> Overview of immudb instance

  
  
**Step 2: deploy a dedicated MinIO instance**  
Click here: [https://dash.elest.io/deploy?soft\=MinIO\&id\=63](https://dash.elest.io/deploy?soft=MinIO&id=63&ref=blog.octabyte.io)

The MinIO instance should be deployed in the same dc to reduce latency. You should choose the instance size based on your needs. you can start with the smallest one and increase as needed.

Once deployed, click on the “Admin UI” button to get the endpoint and credentials for your MinIO instance:   


![OctaByte dashboard > Services > Overview of MinIO instance](images/IWPkBRUVZkf9ap609yLGD9K5vtEU-YkYG7_R_8ScTS79tlPESGAOumwCvLWoxDwUu0XUd1LoZqEXGVUYmeuNLlZ0fiRL6LBLAYnxbLls0LTRBpCCYQkM0XEmFwDbhcGjMBPQSdzsXYPpAN-V7g)

OctaByte dashboard \> Services \> Overview of MinIO instance

  


Log into MinIO with the credentials then create a new S3 bucket for immudb (my\-immudb)

![MinIO web UI > Create Bucket](images/SiZxT3h5BPBCFEZvCUh-mXpM1vfQ8XscIMp8g0lhzbYcQ0LecUOV71c2ouul91NL4lcIzkzNfIuuhVzFnjEdKYiHlC2EoiU-qSg9u9lGRZbj6DaXfttZnQ5iBXvKcDul6hLsX_b2AHXVFiOvvw)

MinIO web UI \> Create Bucket

**Step 3: Configure immudb to store data in our new bucket**  
Go back to OctaByte dashboard \> your deployed immudb instance \> there click on “Update config” button \> Env tab \> add those env variables there: 




```

IMMUDB_S3_STORAGE=true
IMMUDB_S3_ENDPOINT=https://xxxxxxxx.vm.elestio.app
IMMUDB_S3_ACCESS_KEY_ID=root
IMMUDB_S3_SECRET_KEY=MINIO_PASSWORD_YOU_GOT_ABOVE
IMMUDB_S3_BUCKET_NAME=my-immudb
IMMUDB_S3_PATH_PREFIX=data

```


Finally click on the Update \& Restart button, few seconds after your immudb instance will have restarted and is configured to use your S3 bucket.  
  


**Step 4: Check the console output (Server Logs)**  
After the restart immudb automatically starts storing the databases on the configured S3 bucket. You can see the configuration in the console output (Server Logs) and that the S3 storage endpoint is used. 

![](images/dZw75EL0A1czF8QLmir4lq3tP1ITsQYixvQcor23Fs1fuqNg8VtBsKj-9QoH4Pc1vdXrHXT_yc_UkaizEk6V90YO3t5N6aEHfDPnfXNQ3_LD9g5mXnQq2mv4xdmpwQSLyDhoiMPPSWPRWwsy_A)  
The Prometheus metrics exporter comes in handy to track the current state of the S3 sync, you can test it with this curl command:




```

curl -s https://xxxxxxxx.vm.elestio.app:9497/metrics | grep immudb_remoteapp_chunk_count 

```


and by database:


```
curl -s https://xxxxxxxx.vm.elestio.app:9497/metrics | grep remote | grep kind

```
You should see an output similar to this:




```

# HELP immudb_remote_storage_kind Set to 1 for remote storage kind for given database
# TYPE immudb_remote_storage_kind gauge
immudb_remote_storage_kind{db="defaultdb",kind="s3"} 1
immudb_remote_storage_kind{db="rand27584",kind="s3"} 1
immudb_remote_storage_kind{db="systemdb",kind="s3"} 1
immudb_remote_storage_kind{db="testdb",kind="s3"} 1

```


**Hint**: The data is first stored locally and then transferred to S3 whenever the chunks reach a certain size (1MB default) or immudb is shutting down (i. e. maintenance, restart). Therefore don’t worry if you don’t see real data on S3 within the first minutes of operations.  


**Step 5: use immudb in your applications**  
You can find many examples how to use immudb in your applications 

in the online manual:  

[https://docs.immudb.io/master/](https://docs.immudb.io/master/?ref=blog.octabyte.io)


or in the SDK examples repository:  

[https://github.com/codenotary/immudb\-client\-examples](https://github.com/codenotary/immudb-client-examples?ref=blog.octabyte.io)


If you want automated backups, reverse proxy with SSL termination, DOS protection, firewall, automated OS \& Software updates (So your instance of immudb stays always up to date), and a team of Linux experts and open source enthusiasts to ensure your services are always safe, and functional.

Click on the button below to get a fully managed instance of immudb ready to use in less than 3 minutes. 

[Deploy immudb](https://octabyte.io/databases/specialized-databases/immudb)

