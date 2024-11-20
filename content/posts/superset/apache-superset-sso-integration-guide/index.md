---
draft: true
title: "Apache Superset SSO integration guide"
date: "2024-04-05"
description: "Integrating Single Sign-On (SSO) with Apache Superset enhances both security and user experience by enabling users to authenticate with their existing credentials. This guide provides a step-by-step process to set up SSO with Superset.

Prerequisites

 * A Superset instance (v0.34.0 or later)
 * An SSO provider (e.g., Okta, Auth0)"
tags: []
categories: [Business Intelligence]
cover:
  image: images/cover.png
  caption: "Apache Superset SSO integration guide"
ShowToc: true
TocOpen: true
---


Integrating Single Sign\-On (SSO) with Apache Superset enhances both security and user experience by enabling users to authenticate with their existing credentials. This guide provides a step\-by\-step process to set up SSO with Superset.

#### Prerequisites

* A Superset instance (v0\.34\.0 or later)
* An SSO provider (e.g., Okta, Auth0\)

#### Configuration Steps

1. **Install Required Packages:**  
Ensure you have the necessary packages installed, such as `flask-appbuilder`.
2. **Configure Superset:**  
Open vs code from your Tools and Edit the `superset_config.py` file to include your SSO provider's details.
3. **Set Up OAuth:**  
Use the OAuth authentication backend to connect with your SSO provider.

#### Code Example

Here's an example configuration for integrating with Okta:


```
AUTH_TYPE = AUTH_OAUTH
OAUTH_PROVIDERS = [{
    'name':'okta',
    'token_key':'access_token',
    'icon':'fa-circle-o',
    'remote_app': {
        'client_id':'YOUR_CLIENT_ID',
        'client_secret':'YOUR_CLIENT_SECRET',
        'api_base_url':'https://<your-okta-domain>/oauth2/default',
        'client_kwargs':{
            'scope': 'openid profile email'
        },
    }
}]

```
#### Testing

After configuring, test the SSO integration to ensure users can log in seamlessly.

By following these steps and referring to the official documentation, you can successfully integrate SSO with Apache Superset. This integration provides a secure and efficient method for users to access the platform, streamlining the authentication process.

### Configuring SSO Authentication in Superset

To set up Single Sign\-On (SSO) authentication in Apache Superset, follow these steps:

1. **Client Configuration**: Provide the `client_id`, `client_secret`, and other client\-specific settings within the `remote_app` configuration.
2. **Additional Settings**: Adjust additional headers and parameters as needed for your OAuth provider.
3. **Test the Configuration**: Verify the SSO integration by logging into Superset through the configured OAuth provider.

**Define OAuth Providers**: Specify the OAuth providers in the `OAUTH_PROVIDERS` configuration. Include necessary details such as `name`, `token_key`, `icon`, `remote_app`, and endpoints like `access_token_url` and `authorize_url`.


```
OAUTH_PROVIDERS = [
    {
        'name': 'google',
        'token_key': 'access_token',
        'icon': 'fa-google',
        'remote_app': {
            'client_id': '<your-client-id>',
            'client_secret': '<your-client-secret>',
            'api_base_url': 'https://www.googleapis.com/oauth2/v2/',
            'client_kwargs': {
                'scope': 'email profile'
            },
            'access_token_url': 'https://oauth2.googleapis.com/token',
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        }
    }
]

```
**Modify `superset_config.py`**: Configure the authentication type by setting `AUTH_TYPE` to `AUTH_OAUTH`.


```
AUTH_TYPE = AUTH_OAUTH

```
### Managing SSO User Roles and Permissions in Apache Superset

Effectively managing Single Sign\-On (SSO) user roles and permissions in Apache Superset is essential for ensuring secure and appropriate access to data and dashboards. Here's how to manage these roles and permissions:

#### Understanding Permissions

1. **Model \& Action**: Assign permissions such as `can_edit` and `can_delete` on entities like Dashboards or Users to control what actions users can perform.
2. **Views**: Grant view permissions to allow users access to specific web pages within Superset.
3. **Data Source**: Create permissions for each data source to restrict access to those explicitly granted to users.
4. **Database**: Permissions to access a database allow users to query within that database and all its data sources, as long as they have SQL Lab permissions.

#### Role Management

1. **Admin Role**: Use sparingly as it has unrestricted access to everything in Superset.
2. **Alpha Role**: Users can access all data sources but cannot alter permissions.
3. **Gamma Role**: Users have limited access. Assign additional roles for specific data source access.
4. **Custom Roles**: Create custom roles tailored to different access needs. For example, a "Finance" role could be used for users needing access to finance\-related data sources.

#### SSO Integration

Implement a `CustomSsoSecurityManager` to map SSO user details to Superset roles and permissions. This involves extending the `SupersetSecurityManager` and overriding the `oauth_user_info` method.

#### Best Practices

1. **Base Roles**: Avoid altering the base roles provided by Superset.
2. **Custom Roles**: Create roles with specific permissions suited to different user groups.
3. **Regular Reviews**: Regularly review and update permissions to ensure they align with organizational changes.

### Troubleshooting Common SSO Issues in Superset

When integrating Single Sign\-On (SSO) with Apache Superset, you may encounter various challenges. Here are some tips for troubleshooting common problems:

#### Incorrect Redirect URI

* **Check Redirect URI**: Ensure that the redirect URI configured in your SSO provider matches the one set in Superset. Any mismatch can prevent successful authentication.

#### SSO Configuration Errors

* **Verify Configuration**: Double\-check the settings in your `superset_config.py`, including `AUTH_TYPE`, `OAUTH_PROVIDERS`, and related configurations to ensure they are correct.

#### User Role and Permissions

* **Role Assignment**: After SSO authentication, verify that the user has the appropriate role and permissions assigned in Superset to access the necessary resources.

#### SSL/TLS Certificate Issues

* **Certificate Validation**: If using HTTPS, ensure that your SSL/TLS certificates are valid and properly installed. Incomplete or invalid certificates can disrupt secure connections.

#### Debugging Logs

**Enable Debug Mode**: Activate debug mode in Superset to generate detailed logs that can help identify the issue. Add the following line to your configuration:


```
DEBUG = True

```
#### SSO Provider Downtime

* **Check Provider Status**: Ensure that your SSO provider is operational and not experiencing any outages or downtime. This can affect the authentication process.

## **Thanks for reading ❤️**

Thank you so much for reading and do check out the OctaByte resources and Official [Superset documentation](https://superset.apache.org/docs/intro/?ref=blog.octabyte.io) to learn more about Superset. You can click the button below to create your service on [OctaByte](https://octabyte.io/open-source/superset?ref=blog.octabyte.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://octabyte.io/open-source/superset?ref=blog.octabyte.io)

