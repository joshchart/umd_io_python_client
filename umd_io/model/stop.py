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


class Stop(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Bus stop
    """


    class MetaOapg:
        
        class properties:
            stop_id = schemas.StrSchema
            title = schemas.StrSchema
            lat = schemas.Float32Schema
            long = schemas.Float32Schema
            __annotations__ = {
                "stop_id": stop_id,
                "title": title,
                "lat": lat,
                "long": long,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_id"]) -> MetaOapg.properties.stop_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat"]) -> MetaOapg.properties.lat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["long"]) -> MetaOapg.properties.long: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stop_id", "title", "lat", "long", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop_id"]) -> typing.Union[MetaOapg.properties.stop_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat"]) -> typing.Union[MetaOapg.properties.lat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["long"]) -> typing.Union[MetaOapg.properties.long, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stop_id", "title", "lat", "long", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        stop_id: typing.Union[MetaOapg.properties.stop_id, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        lat: typing.Union[MetaOapg.properties.lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        long: typing.Union[MetaOapg.properties.long, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Stop':
        return super().__new__(
            cls,
            *_args,
            stop_id=stop_id,
            title=title,
            lat=lat,
            long=long,
            _configuration=_configuration,
            **kwargs,
        )
