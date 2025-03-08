from playwright.sync_api import Playwright, sync_playwright


def test_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://commitquality.com/practice-clock")
        page.wait_for_url("**/practice-clock")
        page.evaluate("document.querySelector('h2').style.color = 'rgb(0, 255, 0)';")
        page.reload()
        page.wait_for_timeout(3000)
        page.close()
        