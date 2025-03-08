from playwright.sync_api import sync_playwright, expect
import pytest


def test_browser_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com/browser-windows")
        
        # new page of browser
        with context.expect_page() as new_page_info:
            page.locator("#tabButton").click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page.locator("#sampleHeading")).to_be_visible()
        # new window  of browser
        with context.expect_page() as new_win_info:
            page.locator("#windowButton").click()
        new_win = new_win_info.value
        expect(new_win.locator("#sampleHeading")).to_be_visible()

        # handle new window messages
        with context.expect_page() as new_win_msg:
            page.locator("#messageWindowButton").click()
        new_msg = new_win_msg.value
        expect(new_msg.get_by_text("Knowledge increases by sharing but not by saving.")).to_be_visible()
        page.pause()
        browser.close()

        