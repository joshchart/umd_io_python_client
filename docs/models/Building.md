# umd_io.model.building.Building

Represents a building on campus.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a building on campus. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of the building | [optional] 
**code** | str,  | str,  | Shortened building code. Not all buildings have these. | [optional] 
**id** | str,  | str,  | Unique building id | [optional] 
**long** | decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | [optional] 
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

