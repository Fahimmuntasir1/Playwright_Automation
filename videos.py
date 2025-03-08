from playwright.sync_api import playwright, sync_playwright

def test_videos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 1280, "height": 720})
        page = context.new_page()
        page.goto("https://playwright.dev/python/")
        page.click("text=Get started")
        page.close()
        context.close()
