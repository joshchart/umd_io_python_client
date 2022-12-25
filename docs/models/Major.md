# umd_io.model.major.Major

Represents a major

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a major | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**major_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Numeric id of a major. No real meaning here, just an ascending count. | [optional] 
**name** | str,  | str,  | The name of the major. | [optional] 
**college** | str,  | str,  | The college the major is under. | [optional] 
**url** | str,  | str,  | Home page for the major. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

