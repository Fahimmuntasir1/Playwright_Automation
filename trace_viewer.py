from playwright.sync_api import sync_playwright

def test_trace_viewer():
    with sync_playwright() as p:
        # Launch browser and create context
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Enable tracing (recording)
        context.tracing.start(screenshots=True, snapshots=True)

        page = context.new_page()
        
        # Example interaction: navigating to a page
        page.goto("https://demoqa.com/date-picker")
        page.locator("#datePickerMonthYearInput").click()
        page.locator("#datePickerMonthYearInput").clear() 
        page.locator("#datePickerMonthYearInput").fill("2020-02-02")
        page.locator("#datePickerContainer").click()
        page.locator("#dateAndTimePickerInput").click()
        page.locator("#dateAndTimePickerInput").clear() 
        page.locator("#dateAndTimePickerInput").fill("2020-03-02T05:15")
        
        # Stop tracing and save the trace as a .zip file
        context.tracing.stop(path="trace.zip")

        # Close the browser
        browser.close()

test_trace_viewer()