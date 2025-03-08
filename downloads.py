from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.fixture
def browser ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()



def test_downloads(browser):
    page = browser.new_page()
    page.goto("https://commitquality.com/practice-file-download")

    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.get_by_text("Download file").click()
    download = download_info.value

    # Wait for the download process to complete and save the downloaded file somewhere
    download.save_as("/home/ssdt/Automation/testDownloads/" + download.suggested_filename)
    page.close()