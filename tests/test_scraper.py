from historical_robots.scraper import WaybackScraper
from unittest import mock


def test_request(mock_request):
    req = WaybackScraper("foo.com").get_cdx_records()
    assert "20100101010100" in req
    assert len(req) == 5


def test_retrieve_data(mock_request, mock_sleep):
    data = WaybackScraper("foo.com").retrieve_data(["20100101010100"])
    mock_record = ["*", "/test", "2010-01-01 01:01:00", None]
    assert len(data) == 1
    assert data[0] == mock_record


def test_retrieve_data_with_accept_allow(mock_request, mock_sleep):
    data = WaybackScraper("foo.com", accept_allow=True).retrieve_data(
        ["20100101010100"]
    )
    mock_record = ["*", "/test", "2010-01-01 01:01:00", None, "Disallow"]
    assert len(data) == 2
    assert data[0] == mock_record


def test_scrape_and_serialize(mock_request, mock_sleep, monkeypatch):
    mocked = mock.MagicMock()
    monkeypatch.setattr(WaybackScraper, "write_data", mocked)
    scraper = WaybackScraper("foo.com")
    scraper.scrape_and_serialize("test.csv")
    mock_record = ["*", "/test", "2010-01-01 01:01:00", None]
    mocked.assert_called_with("test.csv", [mock_record])
