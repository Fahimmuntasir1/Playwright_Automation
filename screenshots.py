from playwright.sync_api import playwright, sync_playwright, expect
import base64


def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://dribbble.com/")
        page.wait_for_load_state("domcontentloaded")
        page.locator(".shots-search-hero").screenshot(path = "/home/ssdt/Automation/playwrightAuto/screenshot.png")

        page.close()