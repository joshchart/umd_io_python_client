# umd_io.model.route.Route

Bus route

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Bus route | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**route_id** | str,  | str,  | A unique three digit route number | [optional] 
**title** | str,  | str,  | String name of the route | [optional] 
**[stops](#stops)** | list, tuple,  | tuple,  | Array of stops on the route | [optional] 
**[directions](#directions)** | list, tuple,  | tuple,  | Array of directions the bus travels | [optional] 
**[paths](#paths)** | list, tuple,  | tuple,  | Lat/Long points to draw the route on a map | [optional] 
**lat_max** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**lat_min** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**long_max** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**long_min** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stops

Array of stops on the route

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of stops on the route | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Stop**](Stop.md) | [**Stop**](Stop.md) | [**Stop**](Stop.md) |  | 

# directions

Array of directions the bus travels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of directions the bus travels | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A direction for a bus route. Many buses only have one direction, ‘loop’ , which has all stops on the route. Otherwise, there are usually two directions, mostly named for the final stop in that direction. | 

# items

A direction for a bus route. Many buses only have one direction, ‘loop’ , which has all stops on the route. Otherwise, there are usually two directions, mostly named for the final stop in that direction.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A direction for a bus route. Many buses only have one direction, ‘loop’ , which has all stops on the route. Otherwise, there are usually two directions, mostly named for the final stop in that direction. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**direction_id** | str,  | str,  | Unique (relative to the route) string titling the direction | [optional] 
**title** | str,  | str,  | String name of the direction | [optional] 
**[stops](#stops)** | list, tuple,  | tuple,  | Names of stops along the route | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stops

Names of stops along the route

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Names of stops along the route | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# paths

Lat/Long points to draw the route on a map

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Lat/Long points to draw the route on a map | 

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
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**long** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

