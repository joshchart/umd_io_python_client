# umd_io.model.section.Section

Represents a single section of a course.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a single section of a course. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**course** | str,  | str,  | The associated course id | [optional] 
**section_id** | str,  | str,  | A unique section identifier, always the course_id with a four-digit section number appended to it. | [optional] 
**semester** | str,  | str,  | Numeric representation of the semester, in format YYYYMM | [optional] 
**number** | str,  | str,  | The other half of section_id | [optional] 
**seats** | str,  | str,  | The number of seats for the section. | [optional] 
**[meetings](#meetings)** | list, tuple,  | tuple,  | Array of section meetings. | [optional] 
**open_seats** | str,  | str,  | The number of open seats for the section. | [optional] 
**waitlist** | str,  | str,  | The number of people on the waitlist. | [optional] 
**[instructors](#instructors)** | list, tuple,  | tuple,  | An array of professor names for the section | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# meetings

Array of section meetings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of section meetings. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Meeting**](Meeting.md) | [**Meeting**](Meeting.md) | [**Meeting**](Meeting.md) |  | 

# instructors

An array of professor names for the section

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of professor names for the section | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

