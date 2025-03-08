from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.fixture(scope="function")  
def browser(): 
    with sync_playwright() as p:  
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()  
        browser.close()  
def test_debugging(browser):
        page = browser.new_page() 
        page.goto('https://demoqa.com/buttons')
        page.wait_for_load_state("domcontentloaded")
        page.locator("#doubleClickBtn", has_text="Double Click Me").dblclick()
        expect(page.get_by_text("You have done a double click")).to_be_visible()
        page.wait_for_timeout(5000)
        page.close()

