from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#firstName").click()
    page.locator("#firstName").fill("Fahim")
    page.locator("#lastName").click()
    page.locator("#lastName").fill("Muntasir")
    page.locator("#userEmail").click()
    page.locator("#userEmail").fill("sdfsdf@gfgf.com")
    page.locator("#gender-radio-1").check(force=True)
    page.locator("#userNumber").click()
    page.locator("#userNumber").fill("2354654643")
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").click()
    page.locator(".react-datepicker__month-select").select_option("11")
    page.locator(".react-datepicker__year-select").click()
    page.locator(".react-datepicker__year-select").select_option("2000")
    page.locator(".react-datepicker__day--017", has_text="17").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("subject one")
    page.locator("#hobbies-checkbox-2").wait_for(state="visible")
    page.locator("#hobbies-checkbox-2").check(force=True)
    # page.locator("#hobbies-checkbox-1").check(force=True)
    page.locator("#hobbies-checkbox-3").check(force=True)
    
    # --------- upload file in website ------
    # with page.expect_file_chooser() as file_chooser_info:
    #     page.locator("#uploadPicture").click()
    # file_chooser = file_chooser_info.value
    # file_chooser.set_files("/home/ssdt/Downloads/demo.jpg")
    
    # ----- another Way to Upload file -----
    page.locator("#uploadPicture").set_input_files("/home/ssdt/Downloads/demo.jpg")
    page.locator("#currentAddress").click()
    page.locator("#currentAddress").fill("Addresss")
    page.locator("#state").click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city").click()
    page.get_by_text("Delhi", exact=True).click()
    page.locator("#submit").click()
    page.wait_for_timeout(5000)
    
    
    
with sync_playwright() as playwright:
    run(playwright)