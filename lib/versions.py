import sys
import requests
import pytest

def python_version():
    """Return the current Python version info."""
    return sys.version_info

def requests_version():
    """Return the installed Requests library version."""
    return requests.__version__

def pytest_version():
    """Return the installed Pytest version."""
    return pytest.__version__
