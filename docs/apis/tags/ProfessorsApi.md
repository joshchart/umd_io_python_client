<a name="__pageTop"></a>
# umd_io.apis.tags.professors_api.ProfessorsApi

All URIs are relative to *https://api.umd.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_professors**](#get_professors) | **get** /professors | List professors

# **get_professors**
<a name="get_professors"></a>
> [Professor] get_professors()

List professors

Returns list of all professors

### Example

```python
import umd_io
from umd_io.apis.tags import professors_api
from umd_io.model.error import Error
from umd_io.model.professor import Professor
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = professors_api.ProfessorsApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "Aaron Bartlett",
        'course_id': "CMSC216",
    }
    try:
        # List professors
        api_response = api_instance.get_professors(
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling ProfessorsApi->get_professors: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
course_id | CourseIdSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CourseIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_professors.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_professors.ApiResponseFor400) | Malformed query parameters
404 | [ApiResponseFor404](#get_professors.ApiResponseFor404) | No Professors Found

#### get_professors.ApiResponseFor200
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
[**Professor**]({{complexTypePrefix}}Professor.md) | [**Professor**]({{complexTypePrefix}}Professor.md) | [**Professor**]({{complexTypePrefix}}Professor.md) |  | 

#### get_professors.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_professors.ApiResponseFor404
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

