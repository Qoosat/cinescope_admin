import time
from playwright.sync_api import Page, expect
from pathlib import Path
from datetime import datetime
from utils.data_generator import DataGenerator


def test_box(page: Page):
    page.goto('https://dev-cinescope.coconutqa.ru/register')

    full_name = DataGenerator.generate_random_name()
    email = DataGenerator.generate_random_email()
    password = DataGenerator.generate_random_password()

    page.fill(selector='[data-qa-id="register_full_name_input"]', value=full_name)

    page.fill(selector='[data-qa-id="register_email_input"]', value=email)

    page.fill(selector='[data-qa-id="register_password_input"]', value=password)

    page.fill(selector='[data-qa-id="register_password_repeat_input"]', value=password)

    page.click('[data-qa-id="register_submit_button"]')

    page.wait_for_url('https://dev-cinescope.coconutqa.ru/login')
    expect(page.get_by_text("Подтвердите свою почту")).to_be_visible(visible=True)
    time.sleep(3)

    page.goto('https://dev-cinescope.coconutqa.ru/login')

    page.fill(selector='[data-qa-id="login_email_input"]', value=email)

    page.fill(selector='[data-qa-id="login_password_input"]', value=password)

    page.click('[data-qa-id="login_submit_button"]')

    page.wait_for_url('https://dev-cinescope.coconutqa.ru/')
    expect(page.get_by_text("Последние фильмы")).to_be_visible(visible=True)

    time.sleep(5)
