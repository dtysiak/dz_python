import logging
import requests
from requests.auth import HTTPBasicAuth
import pytest

logger = logging.getLogger("search_tests")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(file_handler)git status

@pytest.fixture(scope="class")
def api_session():
    session = requests.Session()

    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token is not None

    session.headers.update({"Authorization": f"Bearer {token}"})
    logger.info("Success")

    return session

class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 1),
            ("price", 3),
            ("year", 2),
            ("year", 5),
            ("brand", 4),
            ("engine_volume", 10),
        ]
    )
    def test_cars_search(self, api_session, sort_by, limit):
        url = "http://127.0.0.1:8080/cars"
        params = {"sort_by": sort_by, "limit": limit}

        logger.info(f"params={params}")

        response = api_session.get(url, params=params)

        logger.info(f"Status: {response.status_code}")
        logger.info(f"Response: {response.text}")

        assert response.status_code == 200

        cars = response.json()
        assert isinstance(cars, list)
        assert len(cars) <= limit
