from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"CloudSentinel" in response.data


def test_health_check():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"


def test_api_info():
    client = app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "CloudSentinel"
    assert data["status"] == "running"