from playwright.sync_api import sync_playwright, expect
import pytest

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.applegadgetsbd.com/")
        searchBox = page.locator("#search")
        searchBox.click()
        searchBox.fill("iphone")
        page.locator("button[type = 'submit']").click()
        sortFilter = page.locator("select[name = 'sortFilter']")
        sortFilter.click()
        sortFilter.select_option("sort__price-desc").click()
        page.wait_for_timeout(3000)
        page.close()