"""
A tiny API client — the API-testing equivalent of a Page Object.

Instead of every test writing out the full URL and calling requests directly,
they go through this one client. It knows the base URL and returns the raw
`requests` response so tests can check status codes and JSON. Keeping it here
means if the API moves, I change the base URL in one place (config.py).

REST in one line: you send an HTTP METHOD (GET/POST/PUT/DELETE) to a URL and
get back a STATUS CODE (200 ok, 201 created, 404 not found...) and usually JSON.
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from framework.config import API_BASE_URL


def _session_with_retries():
    """
    A requests Session that automatically RETRIES a few times if the connection
    drops or the server hiccups. This stops a flaky network from failing an
    otherwise-good API test — the same idea as an explicit wait in UI tests:
    don't fail on a momentary timing problem, give it a moment and try again.
    """
    session = requests.Session()
    retry = Retry(
        total=3,                       # try up to 3 more times
        backoff_factor=0.5,            # wait 0.5s, 1s, 2s between tries
        status_forcelist=[502, 503, 504],   # retry on these server errors
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


class ApiClient:
    def __init__(self, base_url=API_BASE_URL, timeout=15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = _session_with_retries()

    def _url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, **kwargs):
        return self.session.get(self._url(path), timeout=self.timeout, **kwargs)

    def post(self, path, json=None, **kwargs):
        return self.session.post(self._url(path), json=json, timeout=self.timeout, **kwargs)

    def put(self, path, json=None, **kwargs):
        return self.session.put(self._url(path), json=json, timeout=self.timeout, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self._url(path), timeout=self.timeout, **kwargs)
