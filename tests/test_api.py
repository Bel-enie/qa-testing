"""
API TESTS (Week 7)  —  testing the app's data layer, not its buttons.

A UI test drives the browser. An API test skips the screen and talks straight
to the server with HTTP requests. It's faster and less fragile, which is why
APIs sit LOWER on the test pyramid than UI tests.

REST refresher:
  * METHOD  = what you want to do:  GET (read), POST (create),
              PUT (update), DELETE (remove)
  * STATUS CODE = how it went:  200 OK, 201 Created, 404 Not Found
  * JSON    = the data format the server sends back

API under test: JSONPlaceholder (https://jsonplaceholder.typicode.com) — a free,
public REST API made for practice. It fakes writes (POST/PUT/DELETE) but returns
realistic responses, so these tests run anywhere with no setup or API key.

Every test gets the `api` client from conftest.py (an ApiClient instance).
"""
import pytest
from jsonschema import validate

pytestmark = pytest.mark.api  # tag every test in this file as an API test


# 1) GET one item — check the status code and the JSON body
def test_get_single_post_returns_200_and_correct_id(api):
    response = api.get("/posts/1")
    assert response.status_code == 200          # 200 = OK
    body = response.json()                       # parse the JSON
    assert body["id"] == 1
    assert "title" in body                       # the field exists


# 2) GET a list — check we get many items back
def test_get_all_posts_returns_a_list_of_100(api):
    response = api.get("/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100                      # JSONPlaceholder has 100 posts


# 3) GET something that doesn't exist — expect 404 (negative test)
def test_get_missing_post_returns_404(api):
    response = api.get("/posts/99999")
    assert response.status_code == 404            # 404 = Not Found


# 4) POST — create a new item, expect 201 Created and the data echoed back
def test_create_post_returns_201_and_echoes_data(api):
    new_post = {"title": "Eniola's test", "body": "hello", "userId": 7}
    response = api.post("/posts", json=new_post)
    assert response.status_code == 201            # 201 = Created
    body = response.json()
    assert body["title"] == "Eniola's test"       # server echoed our title
    assert "id" in body                           # it assigned an id


# 5) PUT — update an existing item, expect 200 and the new value
def test_update_post_returns_200_and_new_value(api):
    update = {"id": 1, "title": "updated title", "body": "x", "userId": 1}
    response = api.put("/posts/1", json=update)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


# 6) DELETE — remove an item, expect a success status
def test_delete_post_returns_200(api):
    response = api.delete("/posts/1")
    assert response.status_code == 200


# 7) SCHEMA check — the response's SHAPE is correct, not just one field.
#    This catches a server that returns 200 but the wrong structure.
POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}


def test_post_response_matches_expected_schema(api):
    response = api.get("/posts/1")
    assert response.status_code == 200
    # validate() raises if the JSON doesn't match the schema -> test fails
    validate(instance=response.json(), schema=POST_SCHEMA)


# 8) DATA-DRIVEN API test — one test, several ids, checks each comes back right.
@pytest.mark.parametrize("post_id", [1, 5, 50, 100])
def test_each_post_id_matches_itself(api, post_id):
    response = api.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
