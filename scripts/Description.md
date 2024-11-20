# Updated Overview to check Markdown file
Updated This platform delivers Needs a requirement a consolidated, contextualized, and reliable connection to portfolio-wide building systems for data-driven decision making and customized digital services via its developer-friendly APIs. Internal Demo on 1st Aug.

# Documentation

## Building Data Platform Introduction Added

Building Data Platform is an independent data layer, providing centralized API access to application ready BMS and IoT data. 

The data platform interfaces with existing BMS solutions to extract real-time operational data. This integration will encompass HVAC, lighting, security, room control, metering, and other systems. The data platform accommodates an array of IoT devices, including sensors and actuators. These devices generate data related to occupancy, temperature, air quality, and more. By integrating IoT data, the layer enhances real-time monitoring and analysis capabilities, enabling proactive decision-making for building management. The data platform is built in a scalable and system-agnostic manner where additional device types can be flexibly configured within the data model.

The data platform offers robust IT interoperability, supporting industry-standard cloud communication protocols such as MQTT, HTTPS, Web Socket, Web Hook RESTful APIs. The data platform is supplemented with native integrations to Schneider Electric's edge servers via MQTT. The SpaceLogic AS-P and Enterprise Server supports standard protocols including BACnet, LonWorks, Modbus, Web Services, and MQTT.

Building Data Platform contextualizes incoming source data with Brick semantic tags for devices and locations. Devices can represent physical equipment and sensors or represent virtualized systems such as a room scene control. By leveraging Brick schema, the data platform makes all the information collected on the sites available in a standard format, ensuring application-ready consumption and interoperability between disparate equipment and systems.

Building Data Platform's Access & Control API is a REST API which provide consumers with pro-grammatic access to building data. The API enables reading of data values and actuation of commands when applicable systems contain writable properties. The Building Access & Control API also provides access to historical data values. This API facilitates integration with third-party applications, custom dashboards, and analytics platforms. By offering standardized endpoints, the layer promotes data-driven decision-making across a variety of use cases.

Building Data Platform's Data Streaming API is implemented on Azure Event Hub providing access to real-time data streams. The data layer will ingest, process, and distribute real-time data, enabling immediate insights and proactive responses to critical events. The streaming interface is also equipped with change notifications. Consumers can register for change notifications on the event hub stream which will result in notifications at change of value (CoV) events.

## Authentication

Once you have your portal access you can obtain an API Token using the OAuth 2.0 Client Credentials workflow with your consumer credential information. For more information on getting access to the portal and consumer credentials please refer to our document _Portal User Guide – Partner Viewer User_

Your token endpoint is found at the following address where the {tenantId} is unique to the tenant you use in the Building Data Platform: `https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token`

Building Data Platform is backed by Microsoft Entra ID. Token generation follows standard application development practices. 
See [Microsoft identity platform and the OAuth 2.0 client credentials flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow#get-a-token) for more information on the OAuth 2.0 Client Credentials workflow or [Get a Token](#get-a-token) for a detail of obtaining a token for use with our APIs.

### Get a token

After you've acquired the necessary authorization for your application, proceed with acquiring access tokens for our APIs. To get a token by using the client credentials grant, send a POST request to the `/token` Microsoft identity platform. 

### Access token request with a shared secret
```
POST /{tenantId}/oauth2/v2.0/token HTTP/1.1           //Line breaks for clarity
Host: login.microsoftonline.com:443
Content-Type: application/x-www-form-urlencoded

client_id=b5a043d1-69da-4b81-9b76-dbd6a03b1461
&scope=api%3A%2F%2F4d72d298-0401-4918-aa0c-6c768cbc42e3%2F.default
&client_secret=sampleCredentials
&grant_type=client_credentials
```

| Parameter | Condition | Description |
| --- | --- | --- |
| `tenant` | Required | The directory tenant the application plans to operate against, in GUID format. |
| `client_id` | Required | The application ID that's assigned to your consumer credential. You can find this information in the Building Data Platform portal where you registered your consumer credential. |
| `scope` | Required | The scope that's assigned to your consumer credential. You can find this information in the Building Data Platform portal where you registered your consumer credential. |
| `client_secret` | Required | The client secret that was generated for your app in the Building Data Platform portal. The client secret must be URL-encoded before being sent. |
| `grant_type` | Required | Must be set to `client_credentials`. |

### Token Validity

The JWT (JSON Web Token) obtained using the process above has limited validity. After expiry you may create a new token by repeating the create token flow. The JWT itself, as well as the response of the create token request provides information about the expiry time. In the JWT there is a `exp`\-claim and in the response there is a `expires_in` property.

The `exp` (expiration time) claim identifies the expiration time on or after which the JWT MUST NOT be accepted for processing. It's important to note that a resource may reject the token before this time as well - if for example a change in authentication is required or a token revocation has been detected.

## Building Data Platform API Endpoint Basics

For production applications, the base endpoint is:  
`https://ecostruxure-building-platform-api.se.app`   

For UAT applications during development the base endpoint is:  
`https://ecostruxure-building-platform-api-uat.se.app`  

The UAT instance of our Building Data Platform contains a [Swagger](https://ecostruxure-building-platform-api-uat.se.app/swagger) page for API developers. Swagger (OpenAPI) is a language-agnostic specification for describing REST APIs. It allows both computers and humans to understand the capabilities of a REST API without direct access to the source code. 

Developers may use Swagger to make sample requests and download an Open API specification JSON document. 

[Building Data Platform OpenAPI Specification](https://ecostruxure-building-platform-api-uat.se.app/swagger/v1/swagger.json)

[OpenAPI](https://www.openapis.org/)


### Date and Time
All date time values used in `POST`, `PATCH`, and `GET` filters are in Coordinated Universal Time (UTC).

Date time is in ISO 8601 format. This standard is used to represent date and time in a format that is easily understood across different countries and cultures. The T separates the date and time components, and the Z indicates that the time is in Coordinated Universal Time (UTC)


### Filtering

Many API Routes support filtering. Filters are provided as URL query parameters and in all API routes filters are optional.

#### Example

Filter all spaces in a building with `OntologyType` of value `Office`.

```
GET /api/Buildings/3e171897-48c7-4079-883d-3f6964afba9f/Spaces?ontologyType=Office
```

Filter all MeasurementValues in a floor to values which were `updatedAfter` February 24th, 2024 at 10:00:00 UTC.

```
GET /api/Floors/ef69d3a6-91ce-455b-8380-06e5c3238f51/MeasurementValues?updatedAfter=2024-02-24T10%3A00%3A00.000Z
```

### Changing the number of items per page

Page size is controlled by using the `take` parameter.

All API Routes have a default take value of 1000. The maximum take size that can be requested is 5000.

To know if your response has additional data, or to know how many records are available, pay attention to the response header ` x-total-count` which will indicate the total number of records available.

#### Example

Set the maximum number of records to receive in the response to `10`.

```
GET /api/Buildings/3e171897-48c7-4079-883d-3f6964afba9f/Spaces?ontologytype=Office&take=10
```

### Using `link` headers

When a response is paginated, the response headers will include a `link` header. If the endpoint does not support pagination, or if all results fit on a single page, the `link` header will be omitted.

The `link` header contains URLs that you can use to fetch additional pages of results. For example, the previous, next, first, and last page of results. 
```
link: <https://environment.name/api/Buildings/3e171897-48c7-4079-883d-3f6964afba9f/Spaces?ontologytype=Office&take=10>; rel="First" 
```
### API Versions
Over time, newer versions of our API can be introduced. The latest version of our API will become the default version after it has been in production for 1 minor version update unless explicitly stated in the request header. Use the `X-Api-Version` header to set the version of API you require.

Version 1 API
``` 'X-Api-Version: 1.0' ```

Version 2 API
``` 'X-Api-Version: 2.0' ```

> :exclamation: Advanced notice 
The 2024.5 release of Building Data Platform will add Version 3 of the API. At the same time, Version 1 of the API will move to deprecated status and will be removed in the 2024.6 release of the platform. Developers and application consumers should ensure that they are planning migration from API Version 1.0 as soon as possible.
>
> The 2024.5 release will also introduce additional headers returned to API calls to indicate supported and deprecated API versions.
- `api-supported-versions` shall contain an array of supported API versions
- `api-deprecated-version` shall contain an array of deprecated API versions

## Common HTTP Status Codes

### [Successful responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses)

[`200 OK`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)

The request succeeded. The result meaning of "success" depends on the HTTP method:

-   `GET`: The resource has been fetched and transmitted in the message body.
-   `HEAD`: The representation headers are included in the response without any message body.
-   `PUT` or `POST`: The resource describing the result of the action is transmitted in the message body.
-   `TRACE`: The message body contains the request message as received by the server.

[`201 Created`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)

The request succeeded, and a new resource was created as a result. This is typically the response sent after `POST` requests, or some `PUT` requests.

[`202 Accepted`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202)

The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.


### [Client error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses)

[`400 Bad Request`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)

The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

[`401 Unauthorized`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401)

Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

[`403 Forbidden`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)

The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike `401 Unauthorized`, the client's identity is known to the server.

[`404 Not Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)

The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of `403 Forbidden` to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.

### [Server error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses)

[`500 Internal Server Error`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)

The server has encountered a situation it does not know how to handle.

## Standards & Formats 

Building Data Platform standardizes on [Brick Schema](https://brickschema.org/) for data contextualization.

Brick is an ontology-based metadata schema that captures the entities and relationships necessary for effective representations of buildings and their subsystems. Brick describes buildings in a machine readable format to enable programmatic exploration of different operational, structural and functional facets of a building.

A Brick model is a digital representation of a building that adheres to the Brick schema. Entities in a Brick model are classified according to the classes defined by Brick, and are connected using the relationships defined by Brick.

Brick can be extended to meet requirements not modeled within the standard. Extending Brick may include adding new classes, new relationships, new entity properties, new documentation or ontology rules.

## Policies

### Compatibility Policy

Our APIs will evolve over time by the introduction of new properties and endpoints. Prepare your parsers for new properties, so that they are allowed in order not to break the client.

As long as possible we strive not to change the behavior of existing properties and breaking changes are introduced under new versions of our APIs. However, the behavior of an API may change without warning if the existing behavior is incorrect or constitutes a security vulnerability.

See [API Versions](#api-versions)

### Deprecation

We reserve the right to deprecate APIs in full or in part. Care will be taken to ensure this is only done after introducing improved ways to achieve the same outcomes or transition paths are clear to newer versions of our APIs.

To allow application developers time to update their implementations, when deprecating we will provide 3 months' notice to all registered consumers.


## Building Data Platform's Access & Control API

## Tenants (API V1 Only)
```
GET /api/Tenants
GET /api/Tenants/{tenantId}
```
Returns tenant information available to your consumer or to the tenant id provided.  
>Tenants are the top level of the Building Data Platform system hierarchy. Tenants represent a logical collection of sites that typically represent an organization registered in the Building Data Platform.

Example Response:
``` json
[
  {
    "name": "SE BDP Demo",
    "siteCount": 1,
    "id": "e3aa120e-824d-4e43-91a9-5924690934d0"
  }
]
```

## Organizations (API V2 Only)
```
GET /api/Organizations
GET /api/Organizations/{organizationId}
```
Returns organization information available to your consumer or to the organization id provided.  
>Organizations are the top level of the Building Data Platform system hierarchy. Organizations represent a logical collection of sites that typically represent an organization registered in the Building Data Platform.

## Spatial Routes

Building Data Platform adopts a strict relationship for spatial mapping of buildings. The requirements are that there must be at least one building in a `Site`, at least one floor in a `Building`, and at least one `Space` in a `Floor`. The relationship is:

<img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/mermaid-1.png" style="zoom:60%;" /> 

><img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/bulb.png" style="zoom:60%;" /> To retrieve spatial data from our APIs, your consumer subscription must include one or more space with a device. In the event that your subscription does not net any  devices you will not be able to retrieve spaces such as `Site`, `Building`, and `Floor` from the spatial APIs. Not all spaces require devices, you will be able to obtain spatial data from a building with no devices providing your subscription includes one or more device from another building.

### Sites
```
GET /api/Sites
GET /api/Tenants/{tenantId}/Sites (API V1 Only)
GET /api/Organizations/{organizationId}/Sites (API V2 Only)
GET /api/Sites/{siteId}
```
Returns site information available to your consumer, or to the tenant/organization id provided.

V2 API adds the metadata object and changes *tenantId* to *organizationId*

Example Response:
``` json
V1 API
[
  {
    "name": "Schneider Electric London",
    "tenantId": "e3aa120e-824d-4e43-91a9-5924690934d0",
    "version": 1.5,
    "referenceId": "BDP-Demo",
    "area": 0,
    "buildingCount": 2,
    "address": "80 Victoria Street",
    "city": "London",
    "state": null,
    "country": "England",
    "postalCode": "SW1E 5JL",
    "timezone": "Europe/London",
    "timeSeriesRetentionSpan": "30.00:00:00",
    "id": "005056b3-144c-43e7-931a-1a9c38ac1b04"
  }
]

V2 API
[
  {
    "organizationId": "e3aa120e-824d-4e43-91a9-5924690934d0",
    "name": "Schneider Electric London",
    "version": 1.5,
    "area": 0,
    "buildingCount": 2,
    "address": "80 Victoria Street",
    "city": "London",
    "state": null,
    "country": "England",
    "postalCode": "SW1E 5JL",
    "timezone": "Europe/London",
    "timeSeriesRetentionSpan": "30.00:00:00",
    "metadata": [],
    "id": "005056b3-144c-43e7-931a-1a9c38ac1b04"
  }
]
```

### Buildings
```
GET /api/Buildings
GET /api/Tenants/{tenantId}/Buildings (API V1 Only)
GET /api/Organizations/{organizationId}/Buildings (API V2 Only)
GET /api/Sites/{siteId}/Buildings
GET /api/Buildings/{buildingId}
```
Returns building information available to your consumer, or to the tenant id or site id provided.

V2 API adds the metadata object

Example Response:
``` json
V1 API
[
  {
    "name": "Schneider Electric London 1",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "referenceId": "Demo-1",
    "floorCount": 1,
    "spaceCount": 5,
    "deviceCount": 0,
    "measurementCount": 0,
    "area": 0,
    "id": "4bbd692d-e3ef-4208-b57e-13db252907c3"
  },
  {
    "name": "Schneider Electric London 2",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "referenceId": "Demo-2",
    "floorCount": 8,
    "spaceCount": 47,
    "deviceCount": 417,
    "measurementCount": 1167,
    "area": 0,
    "id": "3e171897-48c7-4079-883d-3f6964afba9f"
  }
]

V2 API
[
  {
    "name": "Schneider Electric Boston",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "referenceId": "Planon-Demo",
    "floorCount": 1,
    "spaceCount": 5,
    "deviceCount": 0,
    "measurementCount": 0,
    "area": 0,
    "metadata": [],
    "id": "4bbd692d-e3ef-4208-b57e-13db252907c3"
  },
  {
    "name": "Schneider Electric London",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "referenceId": "BDP-Demo",
    "floorCount": 8,
    "spaceCount": 47,
    "deviceCount": 417,
    "measurementCount": 1161,
    "area": 0,
    "metadata": [],
    "id": "3e171897-48c7-4079-883d-3f6964afba9f"
  }
]
```

### Floors
```
GET /api/Buildings/{buildingId}/Floors
GET /api/Floors/{floorId}
```
Returns floor information for the building or floor id provided.

V2 API adds the metadata object

Example Response:
``` json
V1 API
[
  {
    "name": "Level 0",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "referenceId": "Level-0",
    "spaceCount": 7,
    "deviceCount": 7,
    "measurementCount": 141,
    "area": 0,
    "id": "dad4e267-5924-4b2d-847c-4ebd4c0c4ff2"
  },
  {
    "name": "Level 1",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "referenceId": "Level-1",
    "spaceCount": 7,
    "deviceCount": 7,
    "measurementCount": 118,
    "area": 0,
    "id": "d2f87591-91e7-4ee6-ab68-d7421026c05a"
  }
]

V2 API
[
  {
    "name": "Level 0",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "referenceId": "Level-0",
    "spaceCount": 7,
    "deviceCount": 7,
    "measurementCount": 138,
    "area": 0,
    "metadata": [],
    "id": "dad4e267-5924-4b2d-847c-4ebd4c0c4ff2"
  },
  {
    "name": "Level 1",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "referenceId": "Level-1",
    "spaceCount": 7,
    "deviceCount": 7,
    "measurementCount": 118,
    "area": 0,
    "metadata": [],
    "id": "d2f87591-91e7-4ee6-ab68-d7421026c05a"
  }
]
```

### Spaces
```
GET /api/Buildings/{buildingId}/Spaces
GET /api/Floors/{floorId}/Spaces
GET /api/Spaces/{spaceId}
```

Returns a list of spaces that belong to the building id or floor id provided. Or when calling the spaces route directly, the space information for the given space id.

V2 API adds the metadata object

Example Response:
``` json
v1 API
[
  {
    "name": "Bathrooms",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "e7de8004-50ab-41ee-967a-7476b958f944",
    "referenceId": "B1-004",
    "deviceCount": 2,
    "measurementCount": 4,
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-06T09:09:35+00:00",
    "decommissionedOn": null,
    "area": 200,
    "ontologyType": "Bathroom",
    "id": "0e056104-3638-4841-aa8f-b532492ea5a8"
  },
  {
    "name": "Bathrooms",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "dad4e267-5924-4b2d-847c-4ebd4c0c4ff2",
    "referenceId": "00-004",
    "deviceCount": 3,
    "measurementCount": 7,
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-06T09:09:34+00:00",
    "decommissionedOn": null,
    "area": 215,
    "ontologyType": "Bathroom",
    "id": "10321efa-94d2-4115-85a0-5f245401bca6"
  }
]

v2 API
[
  {
    "name": "Bathrooms",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "e7de8004-50ab-41ee-967a-7476b958f944",
    "referenceId": "B1-004",
    "deviceCount": 2,
    "measurementCount": 4,
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-06T09:09:35+00:00",
    "decommissionedOn": null,
    "area": 0,
    "ontologyType": "Bathroom",
    "metadata": [],
    "id": "0e056104-3638-4841-aa8f-b532492ea5a8"
  },
  {
    "name": "Cleaners",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "e7de8004-50ab-41ee-967a-7476b958f944",
    "referenceId": "B1-003",
    "deviceCount": 1,
    "measurementCount": 7,
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-06T09:09:34+00:00",
    "decommissionedOn": null,
    "area": 0,
    "ontologyType": "JanitorRoom",
    "metadata": [],
    "id": "9da1cc6c-8c04-441a-b2b4-78083414e63b"
  }
]

```

## Data Routes

All data belongs to MeasurementValues. In the system hierarchy MeasurementValues belong to Devices, and Devices belong to DeviceGroups.

DeviceGroups are connected to Buildings.

During the onboarding process, MeasurementValues are given the spatial `context` by being assigned to a `Space`. Measurement values inherits the Space property of the parent `Device`.

For example, an occupancy count sensor may be given the context of `Building` if it measure all occupants in a building at the entry. It likewise could also have been given the context of `Floor` if it measure the occupants on a floor of the building. But it would always need to have a `Space` assigned such as _Ground Floor Entry Hall_

A temperature sensor may be given the context of `Space` when it measures a room.

The `Measures` value will be the relationship to the spatial object such as the `Building`, `Floor`, or `Space`

An example could be:

<img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/mermaid-2.png" style="zoom:60%;" /> 

### DeviceGroups
```
GET /api/Buildings/{buildingId}/DeviceGroups
GET /api/DeviceGroups/{deviceGroupId}
```

Returns device group information for the building or device group id provided.

Example Response:
```json
[
  {
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "source": 32,
    "referenceId": "GraphUAT-A5F7D88496D647455ED508DBB8644C5C-94FCE49A70604B3A93EC8411A74558B3",
    "commissionedStatus": 1,
    "commissionedOn": "2024-02-15T11:25:40.7259502+00:00",
    "decommissionedOn": null,
    "deviceCount": 96,
    "metadata": [
      {
        "name": "ServerName",
        "value": "AS-P"
      },
      {
        "name": "ServerGuid",
        "value": "15e0caa3-9a29-48be-82cf-456d5552057f"
      },
      {
        "name": "ServerType",
        "value": "server.AS-P"
      },
      {
        "name": "ServerVersion",
        "value": "6.0.1.93"
      }
    ],
    "id": "53c2304a-5f8e-474b-ab21-96b83af19774"
  }
]
```

EcoStruxure Building Operation Servers also support a Direct Method to get or set values, see the section [On Demand API](#on-demand-api) for more information.

### Devices
```
GET /api/Buildings/{buildingId}/Devices
GET /api/Floors/{floorId}/Devices
GET /api/Spaces/{spaceId}/Devices
GET /api/Devices/{deviceId}
```

Devices are the physical or logical representation of a piece of equipment, such as an IoT Sensor or a Light. Devices can be queried by their relationship to Buildings, Floors, and Spaces. Calling the Devices route explicitly with a device id returns the device information for the single device. When a device is returned, information pertaining to all its associated measurements are also returned.

V2 API changes the property *type* to *ontologyType* and now aligns to Brick Classes

Example Response:
```json
[
  {
    "type": "Indoor_Air_Quality_Sensor_Equipment",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "dad4e267-5924-4b2d-847c-4ebd4c0c4ff2",
    "spaceId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
    "deviceGroupId": "6ca78a6d-8329-4ee4-bef4-dbf7307b0ed9",
    "source": 32,
    "referenceId": "00-000 IAQ Sensor",
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-28T23:00:00+00:00",
    "decommissionedOn": null,
    "name": "00-000 IAQ Sensor - Indoor_Air_Quality_Sensor_Equipment",
    "coordinates": {
      "latitude": 0,
      "longitude": 0
    },
    "measurements": [
      {
        "id": "bd2f8341-d2d4-4727-9d30-dbb205b2e593",
        "name": "AirQualityIndexSensor",
        "type": "Air_Quality_Index_Sensor",
        "unit": "no unit",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "9df78bb6-5376-44bf-b61e-5be20a0cebc8",
        "name": "AirTemperatureSensor",
        "type": "Air_Temperature_Sensor",
        "unit": "°C",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "329c3064-c1e9-4059-9ea2-4e3e1ad6dc35",
        "name": "AtmosphericPressureSensor",
        "type": "Atmospheric_Pressure_Sensor",
        "unit": "hPa",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "69fe16ba-619c-4921-aa67-9f381bde1164",
        "name": "CO2Sensor",
        "type": "CO2_Sensor",
        "unit": "ppm",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "97ec4055-836e-4d09-b584-59e7b39f307c",
        "name": "HumiditySensor",
        "type": "Relative_Humidity_Sensor",
        "unit": "%",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "0c3f42cf-3ac0-404c-abe7-94cbd7a05f26",
        "name": "IlluminanceSensor",
        "type": "Illuminance_Sensor",
        "unit": "lux",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "ddeec410-b20f-40bd-94df-7f0054928137",
        "name": "PM10Sensor",
        "type": "PM10_Sensor",
        "unit": "µg/m3",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "e9dbbe3a-d63c-4a9e-bcb2-c8a83d68ce03",
        "name": "PM1Sensor",
        "type": "PM1_Sensor",
        "unit": "µg/m3",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "c2efa48c-02fd-46c5-aa49-666198bdefae",
        "name": "PM2.5Sensor",
        "type": "PM2.5_Sensor",
        "unit": "µg/m3",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "6540ed0c-d80b-4647-b2c7-028af872a03a",
        "name": "PM4Sensor",
        "type": "PM4_Sensor",
        "unit": "µg/m3",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "623ab7b8-a3fe-49c2-a454-959eeb4b1644",
        "name": "SoundPressureLevelSensor",
        "type": "Sound_Pressure_Level_Sensor",
        "unit": "dBA",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      },
      {
        "id": "63410bb4-14e0-43bd-a432-3a4e7336b548",
        "name": "VOCSensor",
        "type": "TVOC_Sensor",
        "unit": "ppb",
        "context": 0,
        "measuredId": "4e4c1013-edc8-4059-ab19-e47515eafc1f",
        "isWriteable": false
      }
    ],
    "metadata": [],
    "id": "3186a5fb-971c-4031-ab67-434c382e7eaf"
  },
  {
    "type": "Room_Control_Equipment",
    "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
    "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
    "floorId": "dad4e267-5924-4b2d-847c-4ebd4c0c4ff2",
    "spaceId": "ea70d417-f856-48cd-a890-77dec40e9518",
    "deviceGroupId": "6ca78a6d-8329-4ee4-bef4-dbf7307b0ed9",
    "source": 32,
    "referenceId": "00-001 Insight Sensor",
    "commissionedStatus": 1,
    "commissionedOn": "2023-09-18T23:00:00+00:00",
    "decommissionedOn": null,
    "name": "00-001 Insight Sensor - Room_Control_Equipment",
    "coordinates": {
      "latitude": 0,
      "longitude": 0
    },
    "measurements": [
      {
        "id": "dad26574-b578-4c92-816a-b8b075c3dfc3",
        "name": "AirTemperatureSensor",
        "type": "Air_Temperature_Sensor",
        "unit": "°C",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "2c859a0e-018c-491d-958b-d300ffbe8ad6",
        "name": "HumiditySensor",
        "type": "Relative_Humidity_Sensor",
        "unit": "%",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "e10c49b1-6ef3-4b34-9192-ae0d9a0dc4b3",
        "name": "IlluminanceSensor",
        "type": "Illuminance_Sensor",
        "unit": "lux",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "81a7c2fd-012f-4347-9c17-6d343acdee7c",
        "name": "MotionSensor",
        "type": "Motion_Sensor",
        "unit": "no unit",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "99d43cd7-81b2-4f8c-872b-36a07dddbf02",
        "name": "OccupancyCountSensor",
        "type": "Occupancy_Count_Sensor",
        "unit": "no unit",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "1c62cc5c-b498-4c86-8e7c-34f499a5496f",
        "name": "SoundPressureLevelSensor",
        "type": "Sound_Pressure_Level_Sensor",
        "unit": "dBA",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      },
      {
        "id": "c3492ea1-05b6-473e-b096-d83e8de2cd95",
        "name": "RelativeHumiditySensor",
        "type": "Relative_Humidity_Sensor",
        "unit": "%",
        "context": 0,
        "measuredId": "ea70d417-f856-48cd-a890-77dec40e9518",
        "isWriteable": false
      }
    ],
    "metadata": [],
    "id": "924c6a47-281d-4d95-a009-69bf7c73dfa0"
  }
]
```

### MeasurementValues
> <img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/exclamation.png" style="zoom:60%;" /> Requires your consumer to be enabled for type `Current Value API`
```
GET   /api/Buildings/{buildingId}/MeasurementValues
GET   /api/Devices/{deviceId}/MeasurementValues
GET   /api/Floors/{floorId}/MeasurementValues
GET   /api/DataSets/{dataSetId}/MeasurementValues
GET   /api/DeviceGroups/{deviceGroupId}/MeasurementValues
PATCH /api/DeviceGroups/{deviceGroupId}/MeasurementValues
GET   /api/Spaces/{spaceId}/MeasurementValues
GET   /api/MeasurementValues/{measurementId}
PATCH /api/MeasurementValues/{measurementId}
```

`GET` Verbs for the `MeasurementValues` routes allow retrieval of measurement values across the context of `Building`, `Floor`, `Spaces`, `Devices` as well as individual measurement ids.

It also allows the retrieval of `MeasurementValues` using a `DataSet`. The concept and application of DataSets are covered in the [DataSets](#DataSets) section of this guide.

`PATCH` Verbs for the `MeasurementValues` API also allow for the update of values in the source system where the object is writeable. Not all objects are writeable and a measurement value property of `isWriteable` declares if the value may be written from a remote application.

V2 API changes the property *type* to *ontologyType* and now aligns to Brick Classes

Example Get Response:
`GET /api/MeasurementValues/35f97940-ceee-43d7-ab1c-0a1b24cfa33c`
```json
V1 API
{
  "type": "Temperature_Setpoint",
  "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
  "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
  "floorId": "c5217595-14e8-4a66-ab26-3ee88e8123fd",
  "spaceId": "277cceb9-8caf-4e15-9cd9-1e4c90dc26b3",
  "deviceId": "85cf978e-0dc0-49f4-8468-4e897ea169c6",
  "deviceGroupId": "6ca78a6d-8329-4ee4-bef4-dbf7307b0ed9",
  "referenceId": "nspg:lNPqAN1s9U+WyWOwrNFUSQ.2LPKodosAk2x50YjrDJGAg//Value",
  "context": 0,
  "measuredId": "277cceb9-8caf-4e15-9cd9-1e4c90dc26b3",
  "name": "TemperatureSetpoint",
  "unit": "°C",
  "value": 23.5,
  "timestamp": "2024-02-23T18:51:31.514094+00:00",
  "metadata": [
    {
      "name": "EcoStruxure Building OperationPropertyPath",
      "value": "/Server 1/BDP Demo/Building Overview/Level-02/02-005 Conference Room/02-Space Logic Sensor/04-Variables BDP/01-Writeable Variables/Space Temperature Setpoint/Value"
    }
  ],
  "isWriteable": true,
  "source": 32,
  "commissionedStatus": 1,
  "commissionedOn": "2023-09-19T11:52:41+00:00",
  "decommissionedOn": null,
  "id": "35f97940-ceee-43d7-ab1c-0a1b24cfa33c"
}

V2 API
{
  "ontologyType": "Air_Temperature_Setpoint",
  "siteId": "005056b3-144c-43e7-931a-1a9c38ac1b04",
  "buildingId": "3e171897-48c7-4079-883d-3f6964afba9f",
  "floorId": "c5217595-14e8-4a66-ab26-3ee88e8123fd",
  "spaceId": "277cceb9-8caf-4e15-9cd9-1e4c90dc26b3",
  "deviceId": "85cf978e-0dc0-49f4-8468-4e897ea169c6",
  "deviceGroupId": "6ca78a6d-8329-4ee4-bef4-dbf7307b0ed9",
  "referenceId": "nspg:lNPqAN1s9U+WyWOwrNFUSQ.2LPKodosAk2x50YjrDJGAg//Value",
  "context": 0,
  "measuredId": "277cceb9-8caf-4e15-9cd9-1e4c90dc26b3",
  "name": "AirTemperatureSetpoint",
  "unit": "°C",
  "value": 22,
  "timestamp": "2024-06-03T17:18:03.833362+00:00",
  "metadata": [
    {
      "name": "EboPropertyPath",
      "value": "/Server 1/BDP Demo/Building Overview/Level-02/02-005 Conference Room/02-Space Logic Sensor/04-Variables BDP/01-Writeable Variables/Space Temperature Setpoint/Value"
    }
  ],
  "isWriteable": true,
  "source": 32,
  "commissionedStatus": 1,
  "commissionedOn": "2023-09-19T11:52:41+00:00",
  "decommissionedOn": null,
  "id": "35f97940-ceee-43d7-ab1c-0a1b24cfa33c"
}
```

As an example, to modify the value of the Temperature Setpoint to 16.3, a `PATCH` can be made to the `MeasurementValue` by id with the following body.

Example Write Request:
`PATCH /api/MeasurementValues/35f97940-ceee-43d7-ab1c-0a1b24cfa33c`
```json
[
  { 
    "op": "replace",
    "path": "/value",
    "value": 16.3
  }
]
```

A successful write request will get an empty 200 response.


### DataSets
`DataSets` are designed to give client applications the ability to create logical groups of data which can be tracked and requested through the `MeasurementValue` API route.

Application developers can create and manage `DataSets` using the `GET`, `POST`, `PATCH`, and `DELETE` Verbs available below.

`DataSets` contain an array of `Building`, `Floor`, and `Space` identifiers. A `DataSet` may contain a mix of types. For example, a data set can contain all measurement values from:
1. Building A
1. Floor 1 of Building B
1. Floor 2 of Building B 
1. All meeting rooms from Building C   
   

Alternatively a DataSet could contain:
1. All Occupancy Sensors from Floor 2 Building B

It is possible to manage multiple datasets for your client and you can use a dataset to manage measurement values which meet application specific criteria after discovering the measurement values of interest.

Data can then be retrieved from the `DataSet` whilst it remains active. Take note of the `expiresOn` property during the lifecycle of the `DataSet`.

```
GET     /api/DataSets
POST    /api/DataSets
GET     /api/DataSets/{dataSetId}
PATCH   /api/DataSets/{dataSetId}
DELETE  /api/DataSets/{dataSetId}

```

Example Respose to `GET /api/DataSets`
```json
[
  {
    "name": "Demo Building DataSet 1",
    "expiresOn": "2024-02-23T20:37:14.59+00:00",
    "members": {
      "buildings": [
        "3e171897-48c7-4079-883d-3f6964afba9f"
      ],
      "floors": [],
      "spaces": []
    },
    "id": "596079e2-22a2-4999-9ba2-08dc32e00a41"
  }
    {
    "name": "Demo Building DataSet 2",
    "expiresOn": "2024-02-24T00:00:00.00+00:00",
    "members": {
      "buildings": [],
      "floors": [],
      "spaces": [
        "0e056104-3638-4841-aa8f-b532492ea5a8",
        "10321efa-94d2-4115-85a0-5f245401bca6",
        "8ebb67d0-f7d9-454e-b348-3d0ca40b6a10",        
      ]
    },
    "id": "596079e2-22a2-4999-9ba2-08dc32e00a41"
  }
]
```

Example Request to `POST /api/DataSets`
```json
{
  "name": "Demo Building DataSet 1",
  "expiresOn": "2024-02-23T19:37:14.590Z",
  "members": {
    "buildings": [
      "3e171897-48c7-4079-883d-3f6964afba9f"    
    ]
  }
}
```

Successful requests to POST returns a 200 response with the following body.
```json
{
  "name": "Demo Building DataSet 1",
  "expiresOn": "2024-02-23T19:37:14.59+00:00",
  "members": {
    "buildings": [
      "3e171897-48c7-4079-883d-3f6964afba9f"
    ],
    "floors": null,
    "spaces": null
  },
  "id": "b80c5333-0d4d-4546-c0d5-08dc32e02c39"
}
```

## On Demand API

### Device Groups
><img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/exclamation.png" style="zoom:60%;" /> Requires your consumer to be enabled for type `On Demand API`
```
POST /api/DeviceGroups/{deviceGroupId}/GetOnDemand
POST /api/DeviceGroups/{deviceGroupId}/SetOnDemand
```
The `POST` Body contains either the full EcoStruxure Building Operation Server path to the object, or an encoded string representing the EcoStruxure Building Operation GUID values of the server and object, the property name should always be provided at the end of the path and is typically `/Value`.

For example using nspg server guid:
``` json
    "id": "nspg:QfYqlHpaROeShMIcVsuMew.zCN7mG+8ScGjx6H9DZlMNA//Value"
```
or using EcoStruxure Building Operation server path:
``` json
    "path":"/Server 1/Demo/Analog Value/Value"
```

When reading or writing values to EcoStruxure Building Operation, all activity is logged in the Building Management System under the context of the authorizing user which is part of the setup of the Building Data Platform MQTT Interface. Only values which can be read or written by that authorizing user are accessible to the On Demand API, but the values do not need to be configured as part of the MQTT Data Group telemetry feed.
 
#### GetOnDemand
One or more id's may be passed in the array to retrieve values directly from source.
``` json
[
  {
    "id": "nspg:QfYqlHpaROeShMIcVsuMew.zCN7mG+8ScGjx6H9DZlMNA//Value"
  },
  {
    "id": "nspg:QfYqlHpaROeShMIcVsuMew.OwjdjYZmTMmVSOxsw/mQ+A//Value"
  }
]
```
One or more paths may be passed in the array to retrieve values directly from source.
``` json
[
  {
    "path": "/Server 1/Demo/Analog Value/Value"
  },
  {
    "path": "/Server 1/Demo/Digital Value/Value"
  }
]
```
Example Response:
``` json
[
  {
    "identity": {
      "id": "nspg:SeA3mCmkSYifIOF36cvz/Q.alavXinSQw+cRvRmnUiUwA//Value"
    },
    "statusCode": 200,
    "value": "21",
    "timeStamp": "2024-02-23T04:48:12+00:00",
    "metadata": {
      "Status": "Normal",
      "ValueType": "Double",
      "Unit": "NoUnit",
      "ResponseCode": "Success"
    }
  }
]
```

#### SetOnDemand
One or more id or path and value pairs may be passed in the array to set the value directly to the source system where the object is writeable.
``` json
[
    {
      "identity": {
        "id": "nspg:QfYqlHpaROeShMIcVsuMew.zCN7mG+8ScGjx6H9DZlMNA//Value"
      },
      "value": "10"
    }
]
```
```json
[
    {
      "identity": {
        "path": "/Server 1/Demo/Analog Value/Value"
      },
      "value": "20"
    }
]
```

Successful response will be an empty `200` response body.

## Historical API
### HistoricalValues
> <img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/exclamation.png" style="zoom:60%;" /> Requires your consumer to be enabled for type `Historical API`
```
GET /api/Buildings/{buildingId}/HistoricalValues
GET /api/Floors/{floorId}/HistoricalValues
GET /api/Spaces/{spaceId}/HistoricalValues
GET /api/DeviceGroups/{deviceGroupId}/HistoricalValues
GET /api/Devices/{deviceId}/HistoricalValues
GET /api/MeasurementValue/{measurementValueId}/HistoricalValues

```

`HistoricalValues` API Routes allow application developers to make historical data requests from the Building Data Platform time series data store. Building Data Platform offers different site data retention policies. Historical Data requests will only be honored for requests made for data within the sites data retention policy.

Example Response:
```json
[
  {
    "measurementValueId": "fbde9301-1f5e-4b9e-85a2-0a13489fa1e3",
    "value": "19",
    "timestamp": "2024-02-22T13:10:32.156622+00:00"
  },
  {
    "measurementValueId": "fbde9301-1f5e-4b9e-85a2-0a13489fa1e3",
    "value": "19.5",
    "timestamp": "2024-02-22T14:10:32.157308+00:00"
  },
  {
    "measurementValueId": "fbde9301-1f5e-4b9e-85a2-0a13489fa1e3",
    "value": "19",
    "timestamp": "2024-02-22T15:10:32.160758+00:00"
  },
  {
    "measurementValueId": "fbde9301-1f5e-4b9e-85a2-0a13489fa1e3",
    "value": "18",
    "timestamp": "2024-02-22T16:10:32.233397+00:00"
  },
  {
    "measurementValueId": "fbde9301-1f5e-4b9e-85a2-0a13489fa1e3",
    "value": "21",
    "timestamp": "2024-02-22T17:10:32.161203+00:00"
  }
]
```

><img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/bulb.png" style="zoom:60%;" /> Overall performance of Historical API calls is generally quicker if you make multiple requests with a shorter time range, such as one day, rather than to retrieve multiple pages for a long-time range, such as one month. The difference is more pronounced for buildings with larger data sets than for those with small data sets.


## Data Streaming API

### EventHubs
><img src="https://raw.githubusercontent.com/ecostruxure-openapi/public-images/main/bdp/exclamation.png" style="zoom:60%;" /> Requires your consumer to be enabled for type `Streaming API`
```
GET     /api/EventHubs
GET     /api/EventHubs/{eventHubId}
PATCH   /api/EventHubs/{eventHubId}
```

EventHubs are configured for a consumer where the Streaming API is selected. EventHubs allow developers to consume streaming data as it is processed in real-time by the Building Data Platform.

Information on configured EventHubs can be obtained from the Data API routes above.

### EventHub Telemetry Messaging Specification
This section defines the message format for telemetry messages in the data feed. The message is a JSON object, where certain properties will vary depending on the message type. 

#### Common Message Properties 
| Property      | Type   | Value   |
| ------------- | ------------- | ------------- |
| Version | Int | 1.0 |
| MessageType | String | MeasurementValue, ConfigurationChange |
| BuildingId| GUID | 
| Timestamp| TimeStamp | ISO8601-formatted timestamp in UTC time |

#### MeasurementValue Message 

This message is used to send the latest value for a given measurement. 
| Property      | Type   | Value   |
| ------------- | ------------- | ------------- |
| Version | Int | 1.0 |
| MessageType | String | MeasurementValue |
| MeasurementId | GUID | 
| Value| dynamic| Varies with the data type of the measurement: integer, double, Boolean or string.  |
Sample Message with boolean
```json
{ 
   "Version" : "1.0", 
   "MessageType" : "MeasurementValue", 
   "BuildingId" : "8ce7810e-9528-45d2-a637-b7e618f364e8", 
   "MeasurementId" : "b0406597-4f82-4337-8122-a8ae3b2341999", 
   "Timestamp" : "2024-08-12T21:53:41.85Z", 
   "Value" : true 
} 
```
Sample Message with double value
```json
{ 
   "Version" : "1.0", 
   "MessageType" : "MeasurementValue", 
   "BuildingId" : "8ce7810e-9528-45d2-a637-b7e618f364e8", 
   "MeasurementId" : "b0406597-4f82-4337-8122-a8ae3b2341999", 
   "Timestamp" : "2024-08-12T21:53:41.85Z", 
   "Value" : 23.4
} 
```

#### ConfigurationChange Message 
This message is sent as a notification of various configuration change events. To understand the specifics of the change, the consumer must query the Graph API. 

| Property      | Type   | Value   |
| ------------- | ------------- | ------------- |
| Version | Int | 1.0 |
| MessageType | String | ConfigurationChange|
| BuildingId  | GUID | 
| Timestamp| TimeStamp| ISO8601-formatted timestamp in UTC time |
| ChangeType| string| MapUpdated  |

Sample Message
```json
{ 
   "Version" : "1.0", 
   "MessageType" : "ConfigurationChange", 
   "BuildingId" : "8ce7810e-9528-45d2-a637-b7e618f364e8", 
   "Timestamp" : "2024-06-12T21:53:41.85Z", 
   "ChangeType" : "MapUpdated" 
} 
```

___

_Usage of APIs is subject to an agreement between the customer and Schneider Electric._
