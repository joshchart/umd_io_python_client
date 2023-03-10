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


class Professor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a professor
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            
            
            class taught(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                semester = schemas.IntSchema
                                course = schemas.StrSchema
                                __annotations__ = {
                                    "semester": semester,
                                    "course": course,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["semester"]) -> MetaOapg.properties.semester: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["course"]) -> MetaOapg.properties.course: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["semester", "course", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["semester"]) -> typing.Union[MetaOapg.properties.semester, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["course"]) -> typing.Union[MetaOapg.properties.course, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["semester", "course", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            semester: typing.Union[MetaOapg.properties.semester, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            course: typing.Union[MetaOapg.properties.course, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                semester=semester,
                                course=course,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taught':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "taught": taught,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taught"]) -> MetaOapg.properties.taught: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "taught", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taught"]) -> typing.Union[MetaOapg.properties.taught, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "taught", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        taught: typing.Union[MetaOapg.properties.taught, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Professor':
        return super().__new__(
            cls,
            *_args,
            name=name,
            taught=taught,
            _configuration=_configuration,
            **kwargs,
        )
