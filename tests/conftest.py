import pytest
import time
import requests
from unittest import mock


def mock_robots_txt(**kwargs):
    return "\n".join(["User-agent: *", "Disallow: /test", "Allow: Cool"])


def mock_cdx_records(**kwargs):
    return [f"2010010101010{num} 0" for num in range(0, 5)]


class MockStream:
    def __init__(self, *args, **kwargs):
        pass

    def iter_lines(self, **kwargs):
        return mock_cdx_records()


@pytest.fixture
def mock_request(monkeypatch):
    def mock_get(url, *args, **kwargs):
        return mock.MagicMock(text=mock_robots_txt(), __enter__=MockStream)

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_sleep(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda *args: True)
