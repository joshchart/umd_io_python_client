<a name="__pageTop"></a>
# umd_io.apis.tags.courses_api.CoursesApi

All URIs are relative to *https://api.umd.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_course_list**](#get_course_list) | **get** /courses/list | List of minified courses
[**get_course_sections_by_id**](#get_course_sections_by_id) | **get** /courses/{course_ids}/sections/{section_ids} | View specific sections for a course
[**get_courses**](#get_courses) | **get** /courses | List of courses
[**get_courses_by_id**](#get_courses_by_id) | **get** /courses/{course_ids} | View specific courses
[**get_departments**](#get_departments) | **get** /courses/departments | List departments
[**get_sections**](#get_sections) | **get** /courses/sections | List of sections
[**get_sections_by_ids**](#get_sections_by_ids) | **get** /courses/sections/{section_ids} | View specific sections
[**get_sections_for_course**](#get_sections_for_course) | **get** /courses/{course_ids}/sections | View sections for a course
[**get_semesters**](#get_semesters) | **get** /courses/semesters | List semesters

# **get_course_list**
<a name="get_course_list"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_course_list()

List of minified courses

Returns list of all course codes and names

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only optional values
    query_params = {
        'sort': "course_id,-credits",
        'page': 3,
        'per_page': 3,
        'semester': "202008|leq",
    }
    try:
        # List of minified courses
        api_response = api_instance.get_course_list(
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_course_list: %s\n" % e)
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
sort | SortSchema | | optional
page | PageSchema | | optional
per_page | PerPageSchema | | optional
semester | SemesterSchema | | optional


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_course_list.ApiResponseFor200) | Successful Operation

#### get_course_list.ApiResponseFor200
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
**course_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_course_sections_by_id**
<a name="get_course_sections_by_id"></a>
> [Section] get_course_sections_by_id(course_idssection_ids)

View specific sections for a course

Returns info about one or more courses

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.error import Error
from umd_io.model.section import Section
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
        'section_ids': ["ENGL101-0101","MATH140-0201"],
    }
    query_params = {
    }
    try:
        # View specific sections for a course
        api_response = api_instance.get_course_sections_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_course_sections_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
        'section_ids': ["ENGL101-0101","MATH140-0201"],
    }
    query_params = {
        'semester': "202008|leq",
    }
    try:
        # View specific sections for a course
        api_response = api_instance.get_course_sections_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_course_sections_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
semester | SemesterSchema | | optional


# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
course_ids | CourseIdsSchema | | 
section_ids | SectionIdsSchema | | 

# CourseIdsSchema

One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SectionIdsSchema

One or more comma separated section ids, of format DEPTNNN-XXXX.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more comma separated section ids, of format DEPTNNN-XXXX. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_course_sections_by_id.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_course_sections_by_id.ApiResponseFor400) | Malformed course id or section id
404 | [ApiResponseFor404](#get_course_sections_by_id.ApiResponseFor404) | Unknown course id or section id

#### get_course_sections_by_id.ApiResponseFor200
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
[**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) |  | 

#### get_course_sections_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_course_sections_by_id.ApiResponseFor404
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

# **get_courses**
<a name="get_courses"></a>
> [Course] get_courses()

List of courses

Returns paginated list of courses

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.course import Course
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only optional values
    query_params = {
        'sort': "course_id,-credits",
        'page': 3,
        'per_page': 3,
        'semester': "202008|leq",
        'credits': "3|leq",
        'dept_id': "CMSC",
        'gen_ed': "DSNS",
    }
    try:
        # List of courses
        api_response = api_instance.get_courses(
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_courses: %s\n" % e)
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
sort | SortSchema | | optional
page | PageSchema | | optional
per_page | PerPageSchema | | optional
semester | SemesterSchema | | optional
credits | CreditsSchema | | optional
dept_id | DeptIdSchema | | optional
gen_ed | GenEdSchema | | optional


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreditsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeptIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GenEdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_courses.ApiResponseFor200) | Successful Operation

#### get_courses.ApiResponseFor200
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
[**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_courses_by_id**
<a name="get_courses_by_id"></a>
> [Course] get_courses_by_id(course_ids)

View specific courses

Returns info about one or more courses

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.error import Error
from umd_io.model.course import Course
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
    }
    query_params = {
    }
    try:
        # View specific courses
        api_response = api_instance.get_courses_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_courses_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
    }
    query_params = {
        'semester': "202008|leq",
    }
    try:
        # View specific courses
        api_response = api_instance.get_courses_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_courses_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
semester | SemesterSchema | | optional


# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
course_ids | CourseIdsSchema | | 

# CourseIdsSchema

One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_courses_by_id.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_courses_by_id.ApiResponseFor400) | Malformed course id
404 | [ApiResponseFor404](#get_courses_by_id.ApiResponseFor404) | Unknown course id

#### get_courses_by_id.ApiResponseFor200
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
[**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) |  | 

#### get_courses_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_courses_by_id.ApiResponseFor404
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

# **get_departments**
<a name="get_departments"></a>
> [str] get_departments()

List departments

Returns list of all available departments

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List departments
        api_response = api_instance.get_departments()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_departments: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_departments.ApiResponseFor200) | Successful Operation

#### get_departments.ApiResponseFor200
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
items | str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sections**
<a name="get_sections"></a>
> [Section] get_sections()

List of sections

Returns paginated list of sections

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.section import Section
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only optional values
    query_params = {
        'sort': "course_id,-credits",
        'page': 3,
        'per_page': 3,
        'course_id': "CMSC216",
        'seats': "200",
        'open_seats': "5",
        'waitlist': "10",
        'semester': "202008|leq",
    }
    try:
        # List of sections
        api_response = api_instance.get_sections(
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_sections: %s\n" % e)
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
sort | SortSchema | | optional
page | PageSchema | | optional
per_page | PerPageSchema | | optional
course_id | CourseIdSchema | | optional
seats | SeatsSchema | | optional
open_seats | OpenSeatsSchema | | optional
waitlist | WaitlistSchema | | optional
semester | SemesterSchema | | optional


# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# CourseIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeatsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OpenSeatsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WaitlistSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sections.ApiResponseFor200) | Successful Operation

#### get_sections.ApiResponseFor200
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
[**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sections_by_ids**
<a name="get_sections_by_ids"></a>
> [Section] get_sections_by_ids(section_ids)

View specific sections

Returns paginated list of sections

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.error import Error
from umd_io.model.section import Section
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'section_ids': ["ENGL101-0101","MATH140-0201"],
    }
    query_params = {
    }
    try:
        # View specific sections
        api_response = api_instance.get_sections_by_ids(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_sections_by_ids: %s\n" % e)

    # example passing only optional values
    path_params = {
        'section_ids': ["ENGL101-0101","MATH140-0201"],
    }
    query_params = {
        'semester': "202008|leq",
    }
    try:
        # View specific sections
        api_response = api_instance.get_sections_by_ids(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_sections_by_ids: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
semester | SemesterSchema | | optional


# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
section_ids | SectionIdsSchema | | 

# SectionIdsSchema

One or more comma separated section ids, of format DEPTNNN-XXXX.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more comma separated section ids, of format DEPTNNN-XXXX. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sections_by_ids.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_sections_by_ids.ApiResponseFor400) | Malformed section id
404 | [ApiResponseFor404](#get_sections_by_ids.ApiResponseFor404) | Unknown section id

#### get_sections_by_ids.ApiResponseFor200
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
[**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) |  | 

#### get_sections_by_ids.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_sections_by_ids.ApiResponseFor404
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

# **get_sections_for_course**
<a name="get_sections_for_course"></a>
> [Section] get_sections_for_course(course_ids)

View sections for a course

Returns info about one or more courses

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from umd_io.model.error import Error
from umd_io.model.section import Section
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
    }
    query_params = {
    }
    try:
        # View sections for a course
        api_response = api_instance.get_sections_for_course(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_sections_for_course: %s\n" % e)

    # example passing only optional values
    path_params = {
        'course_ids': ["ENGL101","MATH140","CMSC388F"],
    }
    query_params = {
        'semester': "202008|leq",
    }
    try:
        # View sections for a course
        api_response = api_instance.get_sections_for_course(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_sections_for_course: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
semester | SemesterSchema | | optional


# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
course_ids | CourseIdsSchema | | 

# CourseIdsSchema

One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more comma separated course ids, in format DEPTNNN with up to 2 trailing characters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sections_for_course.ApiResponseFor200) | Successful Operation
400 | [ApiResponseFor400](#get_sections_for_course.ApiResponseFor400) | Malformed course id
404 | [ApiResponseFor404](#get_sections_for_course.ApiResponseFor404) | Unknown course id

#### get_sections_for_course.ApiResponseFor200
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
[**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) | [**Section**]({{complexTypePrefix}}Section.md) |  | 

#### get_sections_for_course.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_sections_for_course.ApiResponseFor404
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

# **get_semesters**
<a name="get_semesters"></a>
> [str] get_semesters()

List semesters

Returns list of all available semesters, each in format YYYYMM

### Example

```python
import umd_io
from umd_io.apis.tags import courses_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.umd.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = umd_io.Configuration(
    host = "https://api.umd.io/v1"
)

# Enter a context with an instance of the API client
with umd_io.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List semesters
        api_response = api_instance.get_semesters()
        pprint(api_response)
    except umd_io.ApiException as e:
        print("Exception when calling CoursesApi->get_semesters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_semesters.ApiResponseFor200) | Successful Operation

#### get_semesters.ApiResponseFor200
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
items | str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

