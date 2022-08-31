import pytest
import requests
import get

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

request_url = f"{BASE_URL}?q=London"

def test_get_description(requests_mock):
    requests_mock.get(request_url, json={'weather': [ {'description': 'clear sky'} ]})
    response = get.description(request_url)
    assert 'clear sky' == response