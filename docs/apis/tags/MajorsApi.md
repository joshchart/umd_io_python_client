<a name="__pageTop"></a>
# umd_io.apis.tags.majors_api.MajorsApi

All URIs are relative to *https://api.umd.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_majors**](#get_majors) | **get** /majors/list | List majors

# **get_majors**
<a name="get_majors"></a>
> [Major] get_majors()

List majors

Get a list of all majors

### Example

```python
import umd_io
from umd_io.apis.tags import majors_api
from umd_io.model.major import Major
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = majors_api.MajorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List majors
        api_response = api_instance.get_majors()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling MajorsApi->get_majors: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_majors.ApiResponseFor200) | Successful Operation

#### get_majors.ApiResponseFor200
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
[**Major**]({{complexTypePrefix}}Major.md) | [**Major**]({{complexTypePrefix}}Major.md) | [**Major**]({{complexTypePrefix}}Major.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

