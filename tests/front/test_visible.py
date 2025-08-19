from playwright.sync_api import Page


def test_visible(page: Page):
    page.goto("https://demoqa.com/checkbox", timeout=100000)
    page.wait_for_load_state()
    home = page.locator('#tree-node .rct-title:has-text("Home")')
    assert home.is_visible() is True
    desktop = page.locator('#tree-node .rct-title:has-text("Desktop")')
    assert desktop.is_visible() is False

    page.get_by_role("button", name="Toggle").click()
    assert desktop.is_visible() is True

