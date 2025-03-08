from playwright.sync_api import playwright, sync_playwright, expect

def test_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        
        page.goto("https://commitquality.com/practice-random-popup")

        # Try to catch popups after 5 seconds
        page.wait_for_timeout(5000)
        popup = page.locator(".overlay-content")
        if popup.is_visible():
            popup.get_by_role("button", name="Close").click()

        # # Get popup after a specific action (e.g., click)
        # with page.expect_popup() as popup_info:
        #     page.get_by_test_id("accordion-1").click()
        # print(popup_info)
        # popup = popup_info.value

        # # Interact with the popup normally
        # popup.get_by_test_id("basic-click").click()
        # expect(popup.get_by_text("Button clicked")).to_be_visible()






















        # ----- Wait for new tab after clicking a link ------
        # with context.expect_page() as new_page_info:
        #     page.get_by_text("Open my youtube in a new tab", exact=True).click()  # Make sure this text exists on the page
        # new_page = new_page_info.value
        # page = new_page.get_by_role("button", name="Subscribe")
        # page.click()
        # print(new_page.title(), page)

        # ---- Get all new pages (including popups) in the context -----
        # def handle_page(page):
        #     page.wait_for_load_state()
        #     print(page.title())

        # page.goto("https://commitquality.com/practice-random-popup")

        # context.on("page", handle_page)

        browser.close()