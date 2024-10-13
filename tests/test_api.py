import requests


# def test_get_stocks():
#    url = "http://127.0.0.1:8000/api/stocks"  # Replace with your mock API URL
#    response = requests.get(url)
#
#    # Verify status code
#    assert response.status_code == 200
#
#    # Verify content-type
#    # assert response.headers["Content-Type"] == "application/json; charset=UTF-8"
#
#
# def test_gest_stock_by_id():
#    for i in range(1, 25):
#        url = f"http://127.0.0.1:8000/api/stocks/{i}"
#        response = requests.get(url)
#
#        # Verify status code
#        assert response.status_code == 200
#
#        # Verify content-type
#        assert response.headers["Content-Type"] == "application/json"
#
#        # Verify response structure (Assuming a book object with 'id', 'title', and 'author')
#        data = response.json()
#        assert isinstance(data, dict)
#
#        assert "id" in data
#        assert "name" in data
#        assert "current_price" in data
#
#
# def test_get_index():
#    url = "http://127.0.0.1:8000/api/stocks"  # Replace with your mock API URL
#    response = requests.get(url)
#
#    # Verify status code
#    assert response.status_code == 200


def test_all_stocks():
    response = requests.get("http://localhost:8000/stocks/", allow_redirects=False)
    assert response.status_code == 200


def test_all_stocks():
    response = requests.get("http://localhost:8000/stocks/", allow_redirects=False)
    assert response.status_code == 200


def test_favorite_stocks():
    response = requests.get(
        "http://localhost:8000/stocks/favorites/", allow_redirects=False
    )
    assert response.status_code == 302


def test_index():
    response = requests.get("http://localhost:8000/", allow_redirects=False)
    assert response.status_code == 200


def test_portfolio():
    response = requests.get(
        "http://localhost:8000/my-portfolio/", allow_redirects=False
    )
    assert response.status_code == 302


def test_single_stock():
    response = requests.get("http://localhost:8000/stocks/1/", allow_redirects=False)
    assert response.status_code == 200


def test_user_login():
    response = requests.get("http://localhost:8000/login/", allow_redirects=False)
    assert response.status_code == 200


def test_user_logout():
    response = requests.get("http://localhost:8000/logout/", allow_redirects=False)
    assert response.status_code == 302


def test_user_register():
    response = requests.get("http://localhost:8000/register/", allow_redirects=False)
    assert response.status_code == 200
