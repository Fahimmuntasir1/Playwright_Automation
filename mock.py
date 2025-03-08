from playwright.sync_api import sync_playwright, expect

def test_gets_the_json_from_api_and_adds_a_new_fruit():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Define the route handler
        def handle(route):
            response = route.fetch()
            json = response.json()
            json.append({"name": "Loquat", "id": 100})
            # Fulfill using the original response, while patching the response body
            route.fulfill(response=response, json=json)

        # Mock the API response
        page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", handle)

        # Navigate to the page
        page.goto("https://demo.playwright.dev/api-mocking")

        # Wait for the new fruit (Loquat) to appear
        page.wait_for_selector("text=Loquat")

        # Assert that the new fruit is visible
        # assert(page.locator("text=Loquat")).is_visible()
        expect(page.locator("text = Loquat")).is_visible()

        # Close the browser after the test
        browser.close()
