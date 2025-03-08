from playwright.sync_api import playwright, sync_playwright, expect


def test_network():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            http_credentials={"username": "bill", "password": "pa55w0rd"}
        )
        # context = borwser.new_context()
        # page = context.new_page()
        page = context.new_page()
        page.goto("https://commitquality.com/login")
        expect(page.get_by_role("heading", name = "Login")).to_be_visible()
        page.pause()
