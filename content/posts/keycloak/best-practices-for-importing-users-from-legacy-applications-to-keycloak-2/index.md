---
draft: true
title: "Best Practices for Importing Users from Legacy Applications to Keycloak"
date: "2024-03-05"
description: "Migrating users from legacy applications into a modern identity and access management system like Keycloak can be a complex process. It requires careful planning and execution to ensure that existing users’ credentials, permissions, and data are securely transferred and that the transition causes minimal disruption. In this blog, we’ll"
tags: []
categories: [Identity and access management]
cover:
  image: images/cover.png
  caption: "Best Practices for Importing Users from Legacy Applications to Keycloak"
ShowToc: true
TocOpen: true
---


Migrating users from legacy applications into a modern identity and access management system like Keycloak can be a complex process. It requires careful planning and execution to ensure that existing users’ credentials, permissions, and data are securely transferred and that the transition causes minimal disruption. In this blog, we’ll discuss best practices for importing users from legacy systems into Keycloak, ensuring a smooth migration process while maintaining security and integrity.

### 1\. **Assess Legacy Systems and User Data**

Before starting the migration process, it’s essential to thoroughly assess the legacy system where the user data currently resides. Understanding the structure of the existing database, how user credentials are stored (e.g., hash algorithms used), and what kind of metadata is available is crucial.

For instance, if your legacy system stores passwords using bcrypt, as many systems do, you’ll need to take that into account. Keycloak doesn't natively support bcrypt, but third\-party plugins like [keycloak\-bcrypt](https://github.com/leroyguillaume/keycloak-bcrypt?ref=blog.elest.io) can be added to allow the use of bcrypt hashes. This allows Keycloak to verify user passwords without requiring them to change their credentials after migration.

### 2\. **Choose the Right Federation or Import Strategy**

Keycloak provides several options to bring users from a legacy system into its environment. These include **user federation** and **user import**.

* **User Federation**: This method allows you to connect Keycloak directly to an external user store, such as LDAP or a custom database. The user information remains in the legacy system, but users are authenticated via Keycloak. Over time, you can configure periodic syncs to migrate user data into Keycloak's internal database.
* **User Import**: If the legacy system is being decommissioned and you need to import users directly into Keycloak, you can use an import strategy where all users and their credentials are copied to Keycloak’s internal database. This is useful if you want to retire the legacy system completely.

When importing users, consider leveraging the **Keycloak Admin API** to automate the process. You can programmatically import user accounts in bulk using scripts that call the API, ensuring scalability and efficiency for large datasets.

### 3\. **Handle Password Migration Securely**

Password migration is one of the most critical aspects of user data import. As mentioned earlier, bcrypt\-hashed passwords will require either a custom provider or re\-hashing during the migration process. If it’s not possible to transfer passwords as\-is, consider the following options:

* **Re\-hash on Login**: You can configure the system so that user passwords are re\-hashed using Keycloak’s default hash method upon their first login. This way, when a user logs in with their existing password, the system accepts it, and then stores the password with a new hash algorithm supported by Keycloak.
* **Password Reset**: If re\-hashing isn’t an option, another approach is to trigger password resets for all users after the import. While this ensures a higher level of security, it may also cause friction for users and requires careful communication.

### 4\. **Sync Additional User Metadata**

When importing users, don't forget about the additional user attributes and metadata that might be stored in the legacy system. This includes information such as roles, permissions, profile data, and activity history. Make sure these details are included in the migration process, as they are critical for maintaining a seamless user experience post\-migration.

* **Custom User Attributes**: Keycloak allows for the creation of custom attributes, so if your legacy system has unique user data fields that don’t have an equivalent in Keycloak, you can easily add those fields.
* **Role Mapping**: Ensure that roles and permissions are correctly mapped from the legacy system to Keycloak. You may need to create new role definitions in Keycloak to match your legacy roles.

### 5\. **Test the Migration Process**

Before performing a full migration, you must test the process on a small subset of users. This allows you to troubleshoot any potential issues with data formats, authentication methods, and system performance. Ensure that both the user data and authentication methods are functioning as expected after the migration.

* **Staging Environment**: Always conduct a test migration in a staging environment that mirrors your production setup. This ensures that the process works as intended and minimizes the risk of disruptions during the actual migration.
* **User Experience Testing**: Once the migration is done, test the user experience by logging in with both newly imported users and existing Keycloak accounts. Ensure that all functionalities, such as password resets, role\-based access, and federated identities, work seamlessly.

### 6\. **Communicate with End Users**

If the migration process requires users to take action such as resetting their passwords or re\-authenticating make sure to communicate clearly and proactively with your user base. Provide step\-by\-step instructions and support resources to ensure users know what to expect and how to navigate the transition.

In some cases, users may not even notice the change if everything is handled behind the scenes, especially when user federation is in place and password migration is seamless. However, in instances where user intervention is needed, effective communication is key to minimizing confusion and dissatisfaction.

### 7\. **Monitor Post\-Migration**

After the migration is complete, continuously monitor the system to ensure everything is working as expected. Track authentication errors, user login trends, and any issues reported by users. If you detect any irregularities, troubleshoot and fix them immediately to avoid any negative impact on the user experience.

Additionally, consider setting up logging and analytics to track user behaviour and system performance. This helps in identifying any underlying issues early and allows for optimization of the authentication process.

## **Thanks for reading ❤️**

Following these best practices ensures that the migration process is efficient and user\-friendly, setting up Keycloak as an identity management solution for your organization. Thank you so much for reading and do check out the Elestio resources and official [Keycloak documentation](https://www.keycloak.org/documentation?ref=blog.elest.io) to learn more about Keycloak. You can click the button below to create your service on [Elestio](https://elest.io/open-source/keycloak?ref=blog.elest.io). See you in the next one👋




[![Deploy to Elestio](https://elest.io/images/logos/deploy-to-elestio-btn.png)](https://elest.io/open-source/keycloak?ref=blog.elest.io)



