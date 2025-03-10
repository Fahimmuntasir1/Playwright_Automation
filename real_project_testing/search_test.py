from playwright.sync_api import sync_playwright, expect
import pytest

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.applegadgetsbd.com/")
        searchBox = page.locator("#search")
        searchBox.click()
        searchBox.fill("iphone")
        page.locator("button[type = 'submit']").click()
        sortFilter = page.locator("select[name = 'sortFilter']")
        sortFilter.click()
        sortFilter.select_option("sort__price-desc")
        page.wait_for_load_state("domcontentloaded")
        # filter by storage
        storage = page.locator("p", has_text="Storage")
        expect(storage).to_be_visible()
        page.get_by_label("256GB").click()
        page.wait_for_load_state("domcontentloaded")
        # filter by type
        typee = page.locator("p", has_text="Type")
        expect(typee).to_be_visible()
        page.get_by_label("Active",exact=True).click()
        page.wait_for_load_state("domcontentloaded")
        # filter by sim
        simType = page.locator("p", has_text="Sim")
        expect(simType).to_be_visible()
        page.get_by_label("Dual",exact=True).click()
        page.wait_for_load_state("domcontentloaded")
        # filter by Region
        region = page.locator("p", has_text="Region")
        expect(region).to_be_visible()
        page.get_by_label("USA",exact=True).click()
        page.pause()
        page.close()