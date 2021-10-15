# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from sweetrpg_library_model.model.studio import Studio
from sweetrpg_api_core.schema.base import BaseAPISchema


class StudioAPISchema(BaseAPISchema):
    model_class = Studio

    class Meta:
        type_ = "studio"
        self_view = "studio_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "studio_list"

    name = fields.Str()  # , load_only=True)
    slug = fields.Str()  # , load_only=True)
    system = fields.Str()  # , load_only=True)
