# umd_io.model.course.Course

Represents a course on Testudo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a course on Testudo | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**course_id** | str,  | str,  | A unique string ID with a four-letter dept_id followed by a three digit course number and an optional letter. | [optional] 
**semester** | decimal.Decimal, int, float,  | decimal.Decimal,  | Numeric representation of the semester, in format YYYYMM | [optional] 
**name** | str,  | str,  | String name of the course. | [optional] 
**dept_id** | str,  | str,  | Four letter department code | [optional] 
**department** | str,  | str,  | Full name of the department that offers the course. | [optional] 
**credits** | str,  | str,  | The number of credits the course is worth. | [optional] 
**description** | str,  | str,  | String description of the course, as it appears on Testudo. | [optional] 
**[grading_method](#grading_method)** | list, tuple,  | tuple,  | Array of string grading options available. The possible options are “Regular”, “Pass-Fail”, “Audit”, and “Sat-Fail” | [optional] 
**[gen_ed](#gen_ed)** | list, tuple,  | tuple,  | Strings representing the General Education requirements the course fulfills. Note that this is an array of arrays of strings. The outmost \&quot;layer\&quot; represents \&quot;or\&quot;, while the inner one represents an and relationship. Additionally, if a gened credit is granted only when taken with another class, this will be represented using a pipe (|) with that class name. For instance, \&quot;X, Y or Z (if taken with C)\&quot; on Testudo will be returned as [[X, Y], [Z|C]] here. | [optional] 
**[core](#core)** | list, tuple,  | tuple,  | Array of strings of CORE requirements filled by a course. | [optional] 
**[relationships](#relationships)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[sections](#sections)** | list, tuple,  | tuple,  | The sections of this course. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# grading_method

Array of string grading options available. The possible options are “Regular”, “Pass-Fail”, “Audit”, and “Sat-Fail”

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of string grading options available. The possible options are “Regular”, “Pass-Fail”, “Audit”, and “Sat-Fail” | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# gen_ed

Strings representing the General Education requirements the course fulfills. Note that this is an array of arrays of strings. The outmost \"layer\" represents \"or\", while the inner one represents an and relationship. Additionally, if a gened credit is granted only when taken with another class, this will be represented using a pipe (|) with that class name. For instance, \"X, Y or Z (if taken with C)\" on Testudo will be returned as [[X, Y], [Z|C]] here.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Strings representing the General Education requirements the course fulfills. Note that this is an array of arrays of strings. The outmost \&quot;layer\&quot; represents \&quot;or\&quot;, while the inner one represents an and relationship. Additionally, if a gened credit is granted only when taken with another class, this will be represented using a pipe (|) with that class name. For instance, \&quot;X, Y or Z (if taken with C)\&quot; on Testudo will be returned as [[X, Y], [Z|C]] here. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# core

Array of strings of CORE requirements filled by a course.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of strings of CORE requirements filled by a course. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relationships

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**coreqs** | None, str,  | NoneClass, str,  | courses that must be taken with this one. | [optional] 
**prereqs** | None, str,  | NoneClass, str,  | Requirements for taking this course. | [optional] 
**formerly** | None, str,  | NoneClass, str,  | Previous course codes that were the same course. | [optional] 
**restrictions** | None, str,  | NoneClass, str,  | Additional restrictions/requirements for taking the course. | [optional] 
**additional_info** | None, str,  | NoneClass, str,  | Any additional information listed on Testudo | [optional] 
**also_offered_as** | None, str,  | NoneClass, str,  | Other course codes representing the same course, like in the case of cross-listing | [optional] 
**credit_granted_for** | None, str,  | NoneClass, str,  | Courses that are equivalent in credit. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sections

The sections of this course.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The sections of this course. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  |  | 
[Section](Section.md) | [**Section**](Section.md) | [**Section**](Section.md) |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

