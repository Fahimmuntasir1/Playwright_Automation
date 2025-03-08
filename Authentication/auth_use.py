from playwright.sync_api import sync_playwright

def send_authenticated_request():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Load saved authentication session
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        # Send an authenticated API request
        response = page.request.get("https://example.com/api/protected-data")

        # Print response status and data
        print(f"Status: {response.status}")
        print(f"Response: {response.text()}")

        browser.close()

# Run the function to send an authenticated request
send_authenticated_request()
