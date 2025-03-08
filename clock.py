from playwright.sync_api import Playwright, sync_playwright, expect
import datetime


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     # page.goto("https://www.timeanddate.com/worldclock/fullscreen.html?n=73")
#     page.goto("https://commitquality.com/practice-clock")
#     page.clock.pause_at(datetime.datetime(2025, 2, 17, 10, 0, 0))
#     page.clock.resume()
#     page.pause()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.clock.install()
    page.goto("https://commitquality.com/practice-clock")
    page.pause()
    # jump 5 mins
    page.clock.fast_forward("05:00")
    expect(page.get_by_test_id("message")).to_be_visible()


with sync_playwright() as playwright:
    run(playwright)