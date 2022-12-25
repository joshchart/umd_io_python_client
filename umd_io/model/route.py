# coding: utf-8

"""
    umd.io

    Welcome to umd.io, the open-source API for University of Maryland data. If you are building a University data-focused app, hack, or project, you’re in the right place. This site will walk you through basic API use and document all supported API calls.  umd.io is a GETful API. It follows RESTful conventions, but for now, you can only get data – you can’t create, update, or destroy.  We're now in version 1! We might add new endpoints or more data to existing responses, but we won't remove anything without a major version change.  If you're looking for the v0 docs, you can find them at https://docs.umd.io/. Please note that v0 is deprecated. It will continue to be supported until at least 2021, but will get no further feature updates, and will eventually be discontinued.  We are actively looking for contributors! Tweet, email, or otherwise get in touch with us.  # noqa: E501

    The version of the OpenAPI document: 1.0.0 Beta
    Contact: hi@umd.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from umd_io import schemas  # noqa: F401


class Route(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Bus route
    """


    class MetaOapg:
        
        class properties:
            route_id = schemas.StrSchema
            title = schemas.StrSchema
            
            
            class stops(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Stop']:
                        return Stop
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Stop'], typing.List['Stop']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stops':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Stop':
                    return super().__getitem__(i)
            
            
            class directions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                direction_id = schemas.StrSchema
                                title = schemas.StrSchema
                                
                                
                                class stops(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.StrSchema
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'stops':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "direction_id": direction_id,
                                    "title": title,
                                    "stops": stops,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["direction_id"]) -> MetaOapg.properties.direction_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["stops"]) -> MetaOapg.properties.stops: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["direction_id", "title", "stops", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["direction_id"]) -> typing.Union[MetaOapg.properties.direction_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["stops"]) -> typing.Union[MetaOapg.properties.stops, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["direction_id", "title", "stops", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            direction_id: typing.Union[MetaOapg.properties.direction_id, str, schemas.Unset] = schemas.unset,
                            title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
                            stops: typing.Union[MetaOapg.properties.stops, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                direction_id=direction_id,
                                title=title,
                                stops=stops,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'directions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class paths(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        lat = schemas.Float32Schema
                                        long = schemas.Float32Schema
                                        __annotations__ = {
                                            "lat": lat,
                                            "long": long,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["lat"]) -> MetaOapg.properties.lat: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["long"]) -> MetaOapg.properties.long: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["lat", "long", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["lat"]) -> typing.Union[MetaOapg.properties.lat, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["long"]) -> typing.Union[MetaOapg.properties.long, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lat", "long", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    lat: typing.Union[MetaOapg.properties.lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                    long: typing.Union[MetaOapg.properties.long, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        lat=lat,
                                        long=long,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paths':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            lat_max = schemas.Float32Schema
            lat_min = schemas.Float32Schema
            long_max = schemas.Float32Schema
            long_min = schemas.Float32Schema
            __annotations__ = {
                "route_id": route_id,
                "title": title,
                "stops": stops,
                "directions": directions,
                "paths": paths,
                "lat_max": lat_max,
                "lat_min": lat_min,
                "long_max": long_max,
                "long_min": long_min,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["route_id"]) -> MetaOapg.properties.route_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stops"]) -> MetaOapg.properties.stops: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directions"]) -> MetaOapg.properties.directions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paths"]) -> MetaOapg.properties.paths: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat_max"]) -> MetaOapg.properties.lat_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat_min"]) -> MetaOapg.properties.lat_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["long_max"]) -> MetaOapg.properties.long_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["long_min"]) -> MetaOapg.properties.long_min: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["route_id", "title", "stops", "directions", "paths", "lat_max", "lat_min", "long_max", "long_min", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["route_id"]) -> typing.Union[MetaOapg.properties.route_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stops"]) -> typing.Union[MetaOapg.properties.stops, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directions"]) -> typing.Union[MetaOapg.properties.directions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paths"]) -> typing.Union[MetaOapg.properties.paths, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat_max"]) -> typing.Union[MetaOapg.properties.lat_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat_min"]) -> typing.Union[MetaOapg.properties.lat_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["long_max"]) -> typing.Union[MetaOapg.properties.long_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["long_min"]) -> typing.Union[MetaOapg.properties.long_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["route_id", "title", "stops", "directions", "paths", "lat_max", "lat_min", "long_max", "long_min", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        route_id: typing.Union[MetaOapg.properties.route_id, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        stops: typing.Union[MetaOapg.properties.stops, list, tuple, schemas.Unset] = schemas.unset,
        directions: typing.Union[MetaOapg.properties.directions, list, tuple, schemas.Unset] = schemas.unset,
        paths: typing.Union[MetaOapg.properties.paths, list, tuple, schemas.Unset] = schemas.unset,
        lat_max: typing.Union[MetaOapg.properties.lat_max, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lat_min: typing.Union[MetaOapg.properties.lat_min, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        long_max: typing.Union[MetaOapg.properties.long_max, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        long_min: typing.Union[MetaOapg.properties.long_min, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Route':
        return super().__new__(
            cls,
            *_args,
            route_id=route_id,
            title=title,
            stops=stops,
            directions=directions,
            paths=paths,
            lat_max=lat_max,
            lat_min=lat_min,
            long_max=long_max,
            long_min=long_min,
            _configuration=_configuration,
            **kwargs,
        )

from umd_io.model.stop import Stop
