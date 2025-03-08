import pytest
from playwright.sync_api import sync_playwright, Playwright


@pytest.fixture
def browser():
    with sync_playwright() as p:
        # iphone_13 = p.devices['iPhone 13']
        browser = p.firefox.launch(headless=False)

        # # Devices tests -------*-------
        # context = browser.new_context(
        #     **iphone_13,
        # )
        # # Viewport tests -------*------- and IsMobile tests
        # context = browser.new_context(
        #     viewport={ 'width': 720, 'height': 1280 },
        #     is_mobile=False
        # )
        # # Locale and Timezone -------*-------
        # context = browser.new_context(
        #     locale='en-US',
        #     timezone_id='America/New_York',
        # )
        # # Permissions Tests -------*-------
        # context = browser.new_context()
        # context.grant_permissions(["camera"])

        # # Geolocation Tests -------*-------
        # context = browser.new_context(
        #     permissions=["geolocation"]
        # )
        # # Set the geolocation -------*-------
        # context.set_geolocation({"latitude": 37.7749, "longitude": -122.4194})

        yield browser
        # context.close()
        browser.close()

# # Webcam Tests -------*-------
# def test_webCams(browser):
#     page = browser.new_page()
#     page.goto("https://webcamtests.com/")
#     page.locator("#webcam-launcher").wait_for(state="visible")
#     page.locator("#webcam-launcher").click()
#     page.pause()

# # Geolocation Tests -------*-------
# def test_location(browser):
#     page = browser.new_page()
#     # page.goto("https://www.bennish.net/web-notifications.html")
#     page.goto("https://my-location.org/")
#     page.pause()

def test_user_agent(browser):
        # Set a custom User-Agent
        # context = browser.new_context(
        #     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        # )

        page = browser.new_page()
        page.goto("https://www.whatismybrowser.com/")
        ua = page.evaluate("navigator.userAgent")
        print("Current User-Agent:", ua)
 
        page.pause()