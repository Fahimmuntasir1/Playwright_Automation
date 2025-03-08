from playwright.sync_api import sync_playwright, expect
import pytest

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.daraz.com.bd/")
        expect(page).to_have_title(re.compile == "Online Shopping in Bangladesh: Order Now from Daraz.com.bd")

        page.close()