from playwright.sync_api import sync_playwright
import pytest


def test_iframe():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://commitquality.com/practice-iframe")
        myframe = page.frame_locator("iframe")
        myframe.get_by_test_id("banner-container").is_visible()
        element = myframe.locator(".filter-textbox").fill("baby")

        page.pause()
        browser.close()