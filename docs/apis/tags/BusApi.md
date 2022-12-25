<a name="__pageTop"></a>
# umd_io.apis.tags.bus_api.BusApi

All URIs are relative to *https://api.umd.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_arrival**](#get_arrival) | **get** /bus/routes/{route_id}/arrivals/{stop_id} | Get arrivals for a stop for a route
[**get_locations**](#get_locations) | **get** /bus/routes/{route_id}/locations | Current bus locations by route
[**get_routes**](#get_routes) | **get** /bus/routes | List routes
[**get_routes_by_id**](#get_routes_by_id) | **get** /bus/routes/{route_ids} | View specific routes
[**get_schedules**](#get_schedules) | **get** /bus/routes/{route_id}/schedules | Bus schedules
[**get_stops**](#get_stops) | **get** /bus/stops | List stops
[**get_stops_by_id**](#get_stops_by_id) | **get** /bus/stops/{stop_ids} | Get specific stops

# **get_arrival**
<a name="get_arrival"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_arrival(route_idstop_id)

Get arrivals for a stop for a route

Get arrivals for a stop for a route

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from umd_io.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'route_id': "route_id_example",
        'stop_id': "stop_id_example",
    }
    try:
        # Get arrivals for a stop for a route
        api_response = api_instance.get_arrival(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_arrival: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
route_id | RouteIdSchema | | 
stop_id | StopIdSchema | | 

# RouteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StopIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_arrival.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_arrival.ApiResponseFor400) | Malformed route id or stop id
404 | [ApiResponseFor404](#get_arrival.ApiResponseFor404) | Unknown route id or stop id

#### get_arrival.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**copyright** | str,  | str,  |  | [optional] 
**[predictions](#predictions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# predictions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**routeTag** | str,  | str,  |  | [optional] 
**stopTag** | str,  | str,  |  | [optional] 
**routeTitle** | str,  | str,  |  | [optional] 
**agencyTitle** | str,  | str,  |  | [optional] 
**dirTitleBecauseNoPredictions** | str,  | str,  |  | [optional] 
**[message](#message)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# message

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**priority** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_arrival.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_arrival.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_locations**
<a name="get_locations"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_locations(route_id)

Current bus locations by route

Get bus locations for a route

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from umd_io.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'route_id': "route_id_example",
    }
    try:
        # Current bus locations by route
        api_response = api_instance.get_locations(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_locations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
route_id | RouteIdSchema | | 

# RouteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_locations.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_locations.ApiResponseFor400) | Malformed route code
404 | [ApiResponseFor404](#get_locations.ApiResponseFor404) | Unknown route code

#### get_locations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Bus location object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Bus location object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[lastTime](#lastTime)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**copyright** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lastTime

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | str,  | str,  | A unix timestamp | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_locations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_locations.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_routes**
<a name="get_routes"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_routes()

List routes

Get a list of the available routes.

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List routes
        api_response = api_instance.get_routes()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_routes: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_routes.ApiResponseFor200) | Successful Operation

#### get_routes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**route_id** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_routes_by_id**
<a name="get_routes_by_id"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_routes_by_id(route_ids)

View specific routes

Get route data for one or more routes

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from umd_io.model.route import Route
from umd_io.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'route_ids': [
        "route_ids_example"
    ],
    }
    try:
        # View specific routes
        api_response = api_instance.get_routes_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_routes_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
route_ids | RouteIdsSchema | | 

# RouteIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_routes_by_id.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_routes_by_id.ApiResponseFor400) | Malformed route code
404 | [ApiResponseFor404](#get_routes_by_id.ApiResponseFor404) | Unknown route code

#### get_routes_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**Route**]({{complexTypePrefix}}Route.md) | [**Route**]({{complexTypePrefix}}Route.md) |  | [optional] 
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of routes returned | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_routes_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_routes_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_schedules**
<a name="get_schedules"></a>
> [BusSchedule] get_schedules(route_id)

Bus schedules

Get bus schedules for a route

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from umd_io.model.bus_schedule import BusSchedule
from umd_io.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'route_id': "route_id_example",
    }
    try:
        # Bus schedules
        api_response = api_instance.get_schedules(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_schedules: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
route_id | RouteIdSchema | | 

# RouteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_schedules.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_schedules.ApiResponseFor400) | Malformed route code
404 | [ApiResponseFor404](#get_schedules.ApiResponseFor404) | Unknown route code

#### get_schedules.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BusSchedule**]({{complexTypePrefix}}BusSchedule.md) | [**BusSchedule**]({{complexTypePrefix}}BusSchedule.md) | [**BusSchedule**]({{complexTypePrefix}}BusSchedule.md) |  | 

#### get_schedules.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_schedules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_stops**
<a name="get_stops"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_stops()

List stops

Get a list of the available stops.

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List stops
        api_response = api_instance.get_stops()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_stops: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stops.ApiResponseFor200) | Successful Operation

#### get_stops.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**stop_id** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_stops_by_id**
<a name="get_stops_by_id"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stops_by_id(stop_ids)

Get specific stops

Get data for one or more stops

### Example

```python
import umd_io
from umd_io.apis.tags import bus_api
from umd_io.model.error import Error
from umd_io.model.stop import Stop
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bus_api.BusApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stop_ids': [
        "stop_ids_example"
    ],
    }
    try:
        # Get specific stops
        api_response = api_instance.get_stops_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling BusApi->get_stops_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
stop_ids | StopIdsSchema | | 

# StopIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stops_by_id.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_stops_by_id.ApiResponseFor400) | Malformed route code
404 | [ApiResponseFor404](#get_stops_by_id.ApiResponseFor404) | Unknown route code

#### get_stops_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**Stop**]({{complexTypePrefix}}Stop.md) | [**Stop**]({{complexTypePrefix}}Stop.md) |  | [optional] 
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of routes returned | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_stops_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_stops_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

