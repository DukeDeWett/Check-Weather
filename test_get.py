import get

API_KEY = "8bb4ff781c10f7e725d2e91fff93a987"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

request_url = f"{BASE_URL}?appid={API_KEY}&q=London"

def test_get():
    name = get.name(request_url)
    city = 'London' in name
    assert True == city