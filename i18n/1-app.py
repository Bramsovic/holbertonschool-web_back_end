#!/usr/bin/env python3
"""Configure a basic Flask application with Flask-Babel support."""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Define the application configuration for available locales."""

    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Render the home page for the Babel-enabled Flask app."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
