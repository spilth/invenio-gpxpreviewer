# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 CERN.
#
# Invenio-GPXPreviewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that adds more fun to the platform."""

from invenio_i18n import gettext as _

from . import config


class InvenioGPXPreviewer(object):
    """Invenio-GPXPreviewer extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-gpxpreviewer"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "GPXPREVIEWER_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"],
            )
        for k in dir(config):
            if k.startswith("GPXPREVIEWER_"):
                app.config.setdefault(k, getattr(config, k))
