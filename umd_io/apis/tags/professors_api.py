# coding: utf-8

"""
    umd.io

    Welcome to umd.io, the open-source API for University of Maryland data. If you are building a University data-focused app, hack, or project, you’re in the right place. This site will walk you through basic API use and document all supported API calls.  umd.io is a GETful API. It follows RESTful conventions, but for now, you can only get data – you can’t create, update, or destroy.  We're now in version 1! We might add new endpoints or more data to existing responses, but we won't remove anything without a major version change.  If you're looking for the v0 docs, you can find them at https://docs.umd.io/. Please note that v0 is deprecated. It will continue to be supported until at least 2021, but will get no further feature updates, and will eventually be discontinued.  We are actively looking for contributors! Tweet, email, or otherwise get in touch with us.  # noqa: E501

    The version of the OpenAPI document: 1.0.0 Beta
    Contact: hi@umd.io
    Generated by: https://openapi-generator.tech
"""

from umd_io.paths.professors.get import GetProfessors


class ProfessorsApi(
    GetProfessors,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
