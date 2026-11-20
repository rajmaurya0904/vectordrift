"""Test that the package version is a non-empty string."""

import vectordrift


def test_version_is_non_empty_string() -> None:
    version = vectordrift.__version__
    assert isinstance(version, str)
    assert version != ""
