"""JS/CSS Webpack bundles for Invenio GPX Previewer."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "gpx_js": "./js/invenio_gpxpreviewer/gpx.js",
                "gpx_css": "./css/invenio_gpxpreviewer/gpx.css",
            },
            dependencies={"leaflet": "^1.9.4", "leaflet-gpx": "^2.1.2"},
        ),
    },
)
