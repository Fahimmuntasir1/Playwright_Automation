from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # create new req
    req = playwright.request.new_context()

    # send a get req
    res = req.get('https://jsonplaceholder.typicode.com/posts')

    # print status code and body

    print("status code: ", res.status)
    print("response body: ", res.body)

    # Assertions
    assert res.status == 200, "Status code is not 200!"


# <<---<<---<<---<<--- Create a request to get first post--->>---->>--->>--->>
def test_get_post():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get('https://jsonplaceholder.typicode.com/posts/1')
        assert response.ok
        assert response.status == 200
        data = response.json()
        assert data['id'] == 1
        print("get data")
        print(data)
        print(response.status)
        print(response.body)

# <<---<<---<<---<<--- Create a request to create a post--->>---->>--->>--->>
def test_create_post():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.post('https://jsonplaceholder.typicode.com/posts', data={
            'title': 'foo',
            'body': 'bar',
            'userId': 1,
        })
        assert response.ok
        assert response.status == 201
        data = response.json()
        assert data['id'] is not None
        print("create")
        print(data)
        print(response.status)
        print(response.body)

# <<---<<---<<---<<--- Create a request to delete a post--->>---->>--->>--->>
def test_delete_post():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.delete('https://jsonplaceholder.typicode.com/posts/1')
        assert response.ok
        assert response.status == 200
        print("delete data")
        print(response.status)
        print(response.body)

test_create_post()
test_delete_post()
test_get_post()