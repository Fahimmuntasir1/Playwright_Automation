from playwright.sync_api import sync_playwright, expect
import pytest

def test_progressbar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com/progress-bar")
        page.locator("#startStopButton").click()
        page.wait_for_timeout(15000)
        # page.locator("#startStopButton").click()
        resetBtn = page.locator("#resetButton")
        if resetBtn == True:
            resetBtn.click()
        progress_bar = page.get_by_role("progressbar")
        value = progress_bar.get_attribute("aria-valuenow")
        print(value)
        page.close()