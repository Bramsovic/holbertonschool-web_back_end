#!/usr/bin/env python3
"""Configure a Flask application with translated template messages."""

from typing import Optional

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Define the application configuration for available locales."""

    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> Optional[str]:
    """Select the best supported locale from the incoming request."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """Render the translated home page for the locale-aware Flask app."""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
