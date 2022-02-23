from flask import Blueprint
from .. import config_app

bp = Blueprint("base_routes", __name__)

from . import delete, get, patch  # noqa: F401, E402
