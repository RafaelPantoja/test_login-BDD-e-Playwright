from ast import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page

scenarios('../features/tela_login.feature')

user = 'rafael.pantoja'
senha_acesso = '@fpf2023'


@given(parse("Dado que o usuário está na página de login"))
def user_is_on_login_page(browser: Page):
    browser.goto('https://bit.fpf.br/#/login?u=%2F')


@when('o usuário preenche o campo de usuario com "usuario"')
def user_enters_usuario_senha(browser: Page, usuario):
    usuario_field = browser.locator('[formcontrolname="username"]')
    usuario_field.fill(user)


@when('E o usuário preenche o campo de senha com "senha"')
def user_enters_password(browser: Page, password):
    password_field = browser.locator('[formcontrolname="password"]')
    password_field.fill(senha_acesso)


@then('E o usuário clica no botão de login "enviar"')
def user_clicks_login_button(browser: Page):
    login_button = browser.locator('[type="submit"]')
    login_button.click()


@then("Então o usuário deve ser redirecionado para a página inicial do sistema")
def user_is_redirected_to_homepage(browser: Page):
    assert browser.url == 'https://bit.fpf.br/#/login?u=%2F'
