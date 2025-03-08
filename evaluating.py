from playwright.sync_api import sync_playwright


def test_evaluating():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://commitquality.com/practice")
        page.evaluate("document.body.style.backgroundColor = 'skyBlue'")
        # Execute JavaScript and return the result
        href = page.evaluate("document.location.href")
        print("Page href:", href)




        page.pause()
        browser.close()