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
    page.close()
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
    page.wait_for_timeout(4000)
    page.close()

def test_range_slider(browser):
    page = browser.new_page()
    page.goto("https://jqueryui.com/slider/#range")
    page.wait_for_load_state("domcontentloaded")
    frame = page.frame_locator("iframe.demo-frame")
    frame.locator("body").wait_for()
    lower = frame.locator("span.ui-slider-handle").first
    expect(lower).to_be_visible()
    lower_x = lower.bounding_box()["x"]+ lower.bounding_box()["width"] / 2
    lower_y = lower.bounding_box()["y"]+ lower.bounding_box()["height"] / 2
    page.mouse.move(lower_x, lower_y)
    page.mouse.down()
    page.mouse.move(lower_x + 100, lower_y)
    page.mouse.up()


    upper = frame.locator("span.ui-slider-handle").nth(1)
    expect(upper).to_be_visible()
    upper_x = upper.bounding_box()["x"]+ upper.bounding_box()["width"] / 2
    upper_y = upper.bounding_box()["y"]+ upper.bounding_box()["height"] / 2
    page.mouse.move(upper_x, upper_y)
    page.mouse.down()
    page.mouse.move(upper_x +50, upper_y)
    page.mouse.up()
    page.wait_for_timeout(5000)
    page.close()
