from flask import render_template
import os

from app.features.home import home_bp


@home_bp.route("/")
def index():
    return render_template("home/index.html")
