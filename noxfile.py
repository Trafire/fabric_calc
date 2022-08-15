import os
import tempfile
from typing import Any, IO

import nox
from nox import Session

locations = "src", "tests"
nox.options.sessions = "tests", "safety", "mypy", "lint"


# noxfile.py
@nox.session(python="3.8")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.run("black", *args)


@nox.session(python=["3.8.13"])
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs
    session.run("pytest", *args)


@nox.session(python=["3.10"])
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.run("mypy", *args)


@nox.session(python=["3.8"])
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.run("black", *locations)
    session.run("flake8", *args)


@nox.session(python="3.8")
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    session.run(
        "safety",
        "check",
        "--full-report",
        external=True,
    )
