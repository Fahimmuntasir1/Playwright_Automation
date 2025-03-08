from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # -------CheckBox----------
    # page.goto("https://demoqa.com/checkbox")
    # page.locator("label:has-text('Home')").check()
    # -------Menu Select-----
    page.goto("https://demoqa.com/select-menu")
    page.wait_for_load_state()
    page.locator("#withOptGroup").click()
    page.wait_for_selector("#withOptGroup", state="visible")
    # page.get_by_text("Group 1, option 2", exact=True).click()
    page.get_by_text("A root option", exact=True).click()
    page.locator("#selectOne").click()
    page.wait_for_selector("#selectOne", state="visible")
    page.get_by_text("Dr.", exact=True).click()
    # page.get_by_text("Prof.", exact=True).click()
    
    page.locator("#oldSelectMenu").select_option("Yellow")
    page.locator(".css-1wa3eu0-placeholder").click()
    page.wait_for_selector(".css-1wa3eu0-placeholder", state="visible")
    page.locator("#react-select-4-option-0").click()
    page.locator("#react-select-4-option-1").click()
    page.locator("#react-select-4-option-2").click()
    page.locator("#react-select-4-option-3").click()
    
    page.wait_for_timeout(5000)
    
    
    
    
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)