#!/usr/bin/env python3
"""Configure a Flask application with locale and timezone selection."""

from typing import Optional

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel


users: dict[int, dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Define the application configuration for available locales."""

    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_user() -> Optional[dict[str, Optional[str]]]:
    """Return the mocked user matching the login_as request argument."""
    user_id = request.args.get("login_as")
    if user_id is None:
        return None
    try:
        return users.get(int(user_id))
    except ValueError:
        return None


@app.before_request
def before_request() -> None:
    """Store the mocked logged-in user on the request global."""
    g.user = get_user()


def get_locale() -> str:
    """Select the locale using URL, user preference, headers, then default."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user is not None:
        user_locale = g.user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale
    locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if locale is not None:
        return locale
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone() -> str:
    """Select the timezone using URL, user preference, then default UTC."""
    timezone = request.args.get("timezone")
    if timezone is not None:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user is not None:
        user_timezone = g.user.get("timezone")
        if user_timezone is not None:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


@app.route("/")
def index() -> str:
    """Render the translated home page for the locale-aware Flask app."""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
