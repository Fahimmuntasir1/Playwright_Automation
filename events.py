from playwright.sync_api import sync_playwright
import logging, pytest

logging.basicConfig(level=logging.INFO)

def test_events():
    logging.info("Test execution started")
    with sync_playwright() as p:
        # Launch browser and open page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Listen for the first dialog and automatically accept it with "2021"
        page.once("dialog", lambda dialog: dialog.accept("2021"))
        # Trigger a prompt in the page
        page.evaluate("prompt('Enter a number:')")

        page.wait_for_timeout(4000)
        logging.info("Test finished")
