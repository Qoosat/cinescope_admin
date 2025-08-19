import time

from playwright.sync_api import Page, expect


def test_codegen(page: Page):
    page.goto("https://demoqa.com/")
    page.pause()
    page.locator("svg").first.click()
    page.get_by_text("Text Box").click()
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Name_example")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("main@example.ru")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("Adress")
    page.get_by_role("textbox", name="Current Address").click()
    page.locator("#permanentAddress").click()
    page.locator("#permanentAddress").fill("address")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#name")).to_contain_text("Name:Name_example")
    page.get_by_text("Email:main@example.ru").click()
    expect(page.locator("#email")).to_contain_text("Email:main@example.ru")
    expect(page.locator("#output")).to_contain_text("Current Address :Adress")
    expect(page.locator("#output")).to_contain_text("Permananet Address :address")


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', wait_until='domcontentloaded')
    page.get_by_role("textbox", name="First Name").fill('Piter')
    page.get_by_role("textbox", name="Last Name").fill('Parker')
    page.get_by_role("textbox", name="name@example.com").type('adms23847@mail.com')
    # page.locator('[value="Female"]').focus()
    # page.locator('#genterWrapper').locator('[value="Female"]').click(force=True)
    page.locator('label[for="gender-radio-2"]').click()
    time.sleep(5)
