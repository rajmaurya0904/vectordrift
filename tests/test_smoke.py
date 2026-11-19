"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import vectordrift


def test_version_is_set() -> None:
    assert vectordrift.__version__
