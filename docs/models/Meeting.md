# umd_io.model.meeting.Meeting

A Meeting for a section of a course

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Meeting for a section of a course | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**days** | str,  | str,  | The days of the week that a course meets. Will be some combination of M, Tu, W, Th, F in that order. | [optional] 
**room** | str,  | str,  | The room number the meeting is in. | [optional] 
**building** | str,  | str,  | The building the meeting is in. | [optional] 
**classtype** | str,  | str,  | Lecutre, Discussion, Lab, etc. | [optional] 
**start_time** | str,  | str,  | The time the meeting starts, in format (x)y:zw[a|p]m (e.g. 10:45am, or 6:30pm) | [optional] 
**end_time** | str,  | str,  | The time the meeting ends, in format (x)y:zw[a|p]m (e.g. 10:45am, or 6:30pm) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

