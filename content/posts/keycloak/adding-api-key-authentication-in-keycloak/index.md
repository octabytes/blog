---
draft: true
title: "Adding API Key Authentication In Keycloak"
date: "2024-07-16"
description: "We will be extending Keycloak by adding API key authentication with Elestio using Keycloak. We will be using a self-hosted Keycloak instance deployed on Elestio. So, to get started head over to Elestio Dashboard and deploy and login into the Keycloak service to get started.


Background

API key authentication is"
tags: []
categories: [Identity and access management]
cover:
  image: images/cover.png
  caption: "Adding API Key Authentication In Keycloak"
ShowToc: true
TocOpen: true
---


We will be extending Keycloak by adding API key authentication with Elestio using [Keycloak](https://elest.io/open-source/keycloak?ref=blog.elest.io). We will be using a self\-hosted Keycloak instance deployed on Elestio. So, to get started head over to [Elestio Dashboard](https://elest.io/open-source/keycloak?ref=blog.elest.io) and deploy and login into the Keycloak service to get started.

### Background

API key authentication is among the most straightforward methods for securing access to resources and APIs. This method involves providing a static key, which must be kept secure and used to access protected APIs, typically via a special header or the Authentication header. If you're using Keycloak and want to incorporate API key authentication, continue reading. This guide demonstrates how to extend Keycloak by adding a simple API key authentication mechanism, beneficial for those working within a microservices architecture where different services authenticate differently.

### Design

Consider a system composed of two services: a Spring Boot application serving dashboard pages and a Node.js stateless REST API providing important weather forecast data. Access to these services is available separately through different URIs, but sign\-up via the dashboard is required. Users sign up to obtain an API key, which can be used to access the weather REST API anytime. This scenario is common in API\-as\-a\-service applications. Additionally, our system includes a Keycloak auth server for authentication and authorization. To secure the dashboard service, we use Keycloak’s SSO mechanism. To secure the REST API service, we introduce API key authentication: a random key generated and stored with user data during registration. An endpoint is also needed to verify the existence of the API key.

To implement this, we extend Keycloak with a module featuring:

1. Generation of a random key string and storage with user attributes during registration.
2. An endpoint to verify the validity of the key.

### Implementation

#### Key Generation

Keycloak’s extensibility allows for easy implementation of new features by utilizing its SPI interfaces or overriding providers. Here, we focus on the module implementation, starting with API key generation. This requires capturing the registration event to generate the key. Implementing EventListenerProvider helps capture various internal Keycloak events and take action.


```
public class RegisterEventListenerProvider implements EventListenerProvider {

    private KeycloakSession session;
    private RealmProvider model;
    private RandomString randomString;
    private EntityManager entityManager;

    public RegisterEventListenerProvider(KeycloakSession session) {
        this.session = session;
        this.model = session.realms();
        this.entityManager = session.getProvider(JpaConnectionProvider.class).getEntityManager();
        this.randomString = new RandomString(50);
    }

    public void onEvent(Event event) {
        if (event.getType().equals(EventType.REGISTER)) {
            RealmModel realm = model.getRealm(event.getRealmId());
            String userId = event.getUserId();
            addApiKeyAttribute(userId);
        }
    }

    public void onEvent(AdminEvent adminEvent, boolean includeRepresentation) {
        if (Objects.equals(adminEvent.getResourceType(), ResourceType.USER) && Objects.equals(adminEvent.getOperationType(), OperationType.CREATE)) {
            String userId = adminEvent.getResourcePath().split("/")[1];
            if (Objects.nonNull(userId)) {
                addApiKeyAttribute(userId);
            }
        }
    }

    public void addApiKeyAttribute(String userId) {
        String apiKey = randomString.nextString();
        UserEntity userEntity = entityManager.find(UserEntity.class, userId);
        UserAttributeEntity attributeEntity = new UserAttributeEntity();
        attributeEntity.setName("api-key");
        attributeEntity.setValue(apiKey);
        attributeEntity.setUser(userEntity);
        attributeEntity.setId(UUID.randomUUID().toString());
        entityManager.persist(attributeEntity);
    }

    public void close() {
        // Used for any necessary cleanup before destroying instances.
    }
}

```
In Keycloak, every provider has a corresponding factory responsible for creating instances. Thus, we need to implement the EventListenerProviderFactory:


```
public class RegisterEventListenerProviderFactory implements EventListenerProviderFactory {

    public EventListenerProvider create(KeycloakSession keycloakSession) {
        return new RegisterEventListenerProvider(keycloakSession);
    }

    public void init(Config.Scope scope) {
    }

    public void postInit(KeycloakSessionFactory keycloakSessionFactory) {
    }

    public void close() {
    }

    public String getId() {
        return "api-key-registration-generation";
    }
}

```
#### API Key Validation Endpoint

Next, we create an endpoint to check if an API key is valid:


```
public class ApiKeyResource {

    private KeycloakSession session;

    public ApiKeyResource(KeycloakSession session) {
        this.session = session;
    }

    @GET
    @Produces("application/json")
    public Response checkApiKey(@QueryParam("apiKey") String apiKey) {
        List<UserModel> result = session.userStorageManager().searchForUserByUserAttribute("api-key", apiKey, session.realms().getRealm("example"));
        return result.isEmpty() ? Response.status(401).build() : Response.ok().build();
    }
}

```
Keycloak uses Java (Jakarta) EE, so JAX\-RS annotations are used to create endpoints. To make Keycloak recognize our endpoint, we need to implement RealmResourceProvider and RealmResourceProviderFactory:


```
public class ApiKeyResourceProvider implements RealmResourceProvider {

    private KeycloakSession session;

    public ApiKeyResourceProvider(KeycloakSession session) {
        this.session = session;
    }

    public Object getResource() {
        return new ApiKeyResource(session);
    }

    public void close() {}
}
public class ApiKeyResourceProviderFactory implements RealmResourceProviderFactory {

    public RealmResourceProvider create(KeycloakSession session) {
        return new ApiKeyResourceProvider(session);
    }

    public void init(Config.Scope config) {}

    public void postInit(KeycloakSessionFactory factory) {}

    public void close() {}

    public String getId() {
        return "check";
    }
}

```
#### Provider Configuration

To inform Keycloak about the new providers, we create mappings under META\-INF/services:

**Filename: org.keycloak.events.EventListenerProviderFactory**


```
com.gwidgets.providers.RegisterEventListenerProviderFactory

```
**Filename: org.keycloak.services.resource.RealmResourceProviderFactory**


```
com.gwidgets.providers.ApiKeyResourceProviderFactory

```
#### Module Packaging

Keycloak, as a standalone web app running on Wildfly, allows modules to be installed as .ear or .jar files under standalone/deployments. More information is available in the official documentation. Our project structure is as follows:


```
api-key-ear
api-key-module
pom.xml

```
Full source code is available at [GitHub](https://github.com/zak905/keycloak-api-key-demo?ref=blog.elest.io).

#### Testing your API key

Use the API key to call the REST API service:


```
curl -H "X-API-KEY: YPqIeqhbxUcOgDd6ld2jl9txfDrHxAPme89WLMuC8e0oaYXeA7" https://[CNAME]

{"forecast": "weather is cool today"}

```
Access with an incorrect key results in a 401 response:


```
curl -v -H "X-API-KEY: wrongkey" https://[CNAME]

< HTTP/1.1 401 Unauthorized
< X-Powered-By: Express
< Date: Sun, 16 Jun 2019 18:41:34 GMT
< Connection: keep-alive
< Content-Length: 0
```
## **Thanks for reading ❤️**

Thank you so much for reading and do check out the Elestio resources and Official [Keycloak documentation](https://www.keycloak.org/documentation?ref=blog.elest.io) to learn more about Keycloak. You can click the button below to create your service on [Elestio](https://elest.io/open-source/keycloak?ref=blog.elest.io). See you in the next one👋

[![](https://pub-da36157c854648669813f3f76c526c2b.r2.dev/deploy-on-elestio-black.png)](https://elest.io/open-source/keycloak?ref=blog.elest.io)

