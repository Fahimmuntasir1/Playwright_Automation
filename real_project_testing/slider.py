from playwright.sync_api import playwright, sync_playwright, expect
import pytest

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        browser.close()
def test_slider(browser):
    page = browser.new_page()
    page.goto("https://demoqa.com/slider")
    page.wait_for_load_state("domcontentloaded")
    slider = page.locator("input.range-slider")
    slider.wait_for(state="visible")
    slider_x = slider.bounding_box()["x"]
    slider_y = slider.bounding_box()["y"]
    page.mouse.move(slider_x, slider_y)
    page.mouse.down()
    page.mouse.move(slider_x + 150, slider_y)
    page.mouse.up()
    page.pause()
    page.close()

# def test_range_slider(browser):
#     page = browser.new_page()
#     page.goto("https://www.startech.com.bd/laptop-notebook")
#     expect(page.locator("span", has_text="Price Range")).to_be_visible()
#     page.close()
