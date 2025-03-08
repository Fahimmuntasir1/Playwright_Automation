from playwright.sync_api import sync_playwright

def test_api_key_auth():
    with sync_playwright() as p:
        request = p.request.new_context()
        api_key = "66c7de2faaa5e5c7252ac24458a454de"  # Replace with your API key
        response = request.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={
                "q": "Bangladesh",
                "appid": "66c7de2faaa5e5c7252ac24458a454de"
            }
        )
        assert response.ok
        assert response.status == 200
        data = response.json()
        print(data)
        print("Weather in ${data.name}:", data['weather'][0]['description'])