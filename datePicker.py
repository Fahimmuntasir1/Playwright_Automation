from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://demoqa.com/date-picker")
    page.goto("https://demoqa.com/date-picker")
    page.locator("#datePickerMonthYearInput").click()
    page.locator("#datePickerMonthYearInput").clear() 
    page.locator("#datePickerMonthYearInput").fill("2020-02-02")
    page.locator("#datePickerContainer").click()
    page.locator("#dateAndTimePickerInput").click()
    page.locator("#dateAndTimePickerInput").clear() 
    page.locator("#dateAndTimePickerInput").fill("2020-03-02T05:15")
    
    page.wait_for_timeout(5000)
    
    
    
    
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)