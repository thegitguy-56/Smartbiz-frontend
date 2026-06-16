import os
import pytest
import requests

# Default to the backend URL used in the workflow
DEFAULT_API_URL = "https://smartbiz-backend-c7ru.onrender.com/api"

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for the API."""
    return os.environ.get("SMARTBIZ_API_URL", DEFAULT_API_URL)

@pytest.fixture(scope="session")
def api_session():
    """Return a requests Session object to persist cookies/headers if needed."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session
