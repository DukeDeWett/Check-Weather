import get

API_KEY = "8bb4ff781c10f7e725d2e91fff93a987"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

request_url = f"{BASE_URL}?appid={API_KEY}&q=London"
request_url_2 = f"{BASE_URL}?appid={API_KEY}&q=Norilsk"
request_url_wrong = f"{BASE_URL}?appid={API_KEY}&q=jnfvjfvn"
request_url_wrong_2 = f"{BASE_URL}?appid={API_KEY}&q=2242122"
request_url_wrong_3 = f"{BASE_URL}?appid={API_KEY}&q="


def test_get():
    name = get.name(request_url)
    city = 'London' in name
    assert True == city
def test_get_2():
    name = get.name(request_url_2)
    city = "Norilsk"
    assert True == city
    
def test_wrong():
    name = get.name(request_url_wrong)
    city = "jnfvjfvn"
    assert False == city
   
def test_wrong_2():
    name = get.name(request_url_wrong_2)
    city = "2242122"
    assert False == city
def test_wrong_3():
    name = get.name(request_url_wrong_3)
    city = ""