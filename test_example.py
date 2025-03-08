import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("listitem").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("machranga")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("bird")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("macahranga@gg.com")
    page.get_by_text("Male", exact=True).click()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("3456456523")
    page.locator("#dateOfBirthInput").click()
    page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("4")
    page.get_by_role("combobox").nth(1).select_option("1992")
    page.get_by_role("option", name="Choose Wednesday, May 20th,").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("Subject")
    page.get_by_text("Music").click()
    with page.expect_file_chooser() as file_chooser_info:
        page.get_by_label("Select picture").click()  # File picker ওপেন হবে
    file_chooser = file_chooser_info.value
    file_chooser.set_files("input[type='file']", "/home/ssdt/Downloads/demo.jpg")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("Addresssssssssssss")
    page.locator("#state svg").click()
    page.get_by_text("Haryana", exact=True).click()
    page.locator(".css-tlfecz-indicatorContainer").click()
    page.get_by_text("Karnal", exact=True).click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
