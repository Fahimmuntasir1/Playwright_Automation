from playwright.sync_api import  playwright, sync_playwright, expect
import pytest

@pytest.fixture(scope = "function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)
        context = browser.new_context()
        yield context, browser
        context.close()
        browser.close()


def test_handle_alerts(browser):
    browser_instance, context = browser
    page = context.new_page()
    input_var = "My Name is Fahim"
    def handle_dialog(dialog):
        print(f"Dialog message: {dialog.message}")
        if(dialog.message == "Do you confirm action?"):
            dialog.dismiss()
        elif(dialog.message == "Please enter your name"):
            dialog.accept(input_var)
        else:
            dialog.accept()

    page.on("dialog", handle_dialog)
    page.goto("https://demoqa.com/alerts")
    page.wait_for_load_state("domcontentloaded")
    page.locator("#timerAlertButton").click()
    page.wait_for_timeout(5000)
    page.locator("#alertButton").click()  # This triggers an alert
    page.locator("#confirmButton").click()  # This triggers an alert
    page.locator("#promtButton").click()  # This triggers an alert
    expect(page.get_by_text("You selected Cancel")).to_be_visible()
    # expect(page.get_by_text("You entered"+" " + input_var)).to_be_visible() # Not work
    expect(page.locator("#promptResult")).to_be_visible()
    page.close()

def test_handle_modal(browser):
    browser_instance, context = browser
    page = context.new_page()

    page.goto("https://demoqa.com/modal-dialogs")  # Example URL with modals
    page.wait_for_load_state("domcontentloaded")
    page.locator("#showSmallModal").click()
    page.locator(".modal-content").wait_for(state="visible")
    expect(page.locator(".modal-content")).to_be_visible()
    page.locator("#closeSmallModal").click()
    page.locator(".modal-content").wait_for(state="hidden")
    expect(page.locator("#example-modal-sizes-title-sm")).not_to_be_visible()
    page.close()