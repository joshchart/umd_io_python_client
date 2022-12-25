<a name="__pageTop"></a>
# umd_io.apis.tags.map_api.MapApi

All URIs are relative to *https://api.umd.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_building_by_id**](#get_building_by_id) | **get** /map/buildings/{building_id} | Get buildings
[**get_buildings**](#get_buildings) | **get** /map/buildings | List buildings

# **get_building_by_id**
<a name="get_building_by_id"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_building_by_id(building_id)

Get buildings

Get location data about one or more buildings. Comma separated building numbers are the parameters.

### Example

```python
import umd_io
from umd_io.apis.tags import map_api
from umd_io.model.error import Error
from umd_io.model.building import Building
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = map_api.MapApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'building_id': ["226"],
    }
    try:
        # Get buildings
        api_response = api_instance.get_building_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling MapApi->get_building_by_id: %s\n" % e)
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
building_id | BuildingIdSchema | | 

# BuildingIdSchema

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
200 | [ApiResponseFor200](#get_building_by_id.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_building_by_id.ApiResponseFor400) | Malformed building code
404 | [ApiResponseFor404](#get_building_by_id.ApiResponseFor404) | Unknown building code

#### get_building_by_id.ApiResponseFor200
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
**data** | [**Building**]({{complexTypePrefix}}Building.md) | [**Building**]({{complexTypePrefix}}Building.md) |  | [optional] 
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of buildings returned | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_building_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_building_by_id.ApiResponseFor404
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

# **get_buildings**
<a name="get_buildings"></a>
> [Building] get_buildings()

List buildings

Get a list of the available buildings.

### Example

```python
import umd_io
from umd_io.apis.tags import map_api
from umd_io.model.building import Building
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = map_api.MapApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List buildings
        api_response = api_instance.get_buildings()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling MapApi->get_buildings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_buildings.ApiResponseFor200) | Successful Operation

#### get_buildings.ApiResponseFor200
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
[**Building**]({{complexTypePrefix}}Building.md) | [**Building**]({{complexTypePrefix}}Building.md) | [**Building**]({{complexTypePrefix}}Building.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

