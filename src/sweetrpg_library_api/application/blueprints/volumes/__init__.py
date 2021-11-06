# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Volume routes.
"""

import functools
# from flask_rest_jsonapi import Api
from .manager import VolumeList, VolumeDetail, VolumeAuthorRelationship
from ...blueprints import api


def setup_routes(app):
    # app.logger.info("Registering volume models...")
    # for model_name, model_info in volume_model_info.items():
    #     APIData.add_model(model_name, model_info)

    app.logger.info("Setting up routes for Volumes API")
    # api = Api(app)
    api.route(VolumeList, "volume_list", "/volumes/")
    api.route(VolumeDetail, "volume_detail", "/volumes/<id>")
    api.route(VolumeAuthorRelationship, "volume_authors", "/volumes/<id>/relationships/authors")
