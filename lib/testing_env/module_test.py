from versions import python_version, requests_version, pytest_version

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3, f"Expected major version 3 but got {version_info.major}"
    assert version_info.minor >= 8, f"Expected minor version >= 8 but got {version_info.minor}"

def test_requests_version():
    version = requests_version()
    assert version is not None and len(version) > 0, "Requests version should not be empty"

def test_pytest_version():
    version = pytest_version()
    assert version is not None and len(version) > 0, "Pytest version should not be empty"
