from playwright.sync_api import sync_playwright, expect
import pytest, json



def test_snapshoht():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto('https://playwright.dev/')
        page.wait_for_load_state("domcontentloaded")

        # ---- First part ----
        # snapshot = page.accessibility.snapshot()

        # # Save snapshot as JSON file
        # with open("accessibility_snapshot.json", "w") as f:
        #     json.dump(snapshot, f, indent=2)


        # ---- Second part ----
        banner = page.get_by_role("banner")

        # Assert the snapshot
        expect(banner).to_match_aria_snapshot("""
        - banner:
            - heading /Playwright enables reliable end-to-end/ [level=1]
            - link "Get started"
            - link "Star microsoft/playwright on GitHub"
            - link /[\\d]+k\\+ stargazers on GitHub/
        """)


        context.tracing.stop(path = "trace.zip")
        
