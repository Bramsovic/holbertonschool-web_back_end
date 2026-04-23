#!/usr/bin/env python3
"""Create a basic Flask application for the i18n project."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the landing page for the basic Flask application."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
