from pages.login_page import LoginPage


def test_successful_login(browser):
    page = browser.new_page()
    login = LoginPage(page)
    login.goto()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_flash_message()
    page.close()

def test_failed_login(browser):
    page = browser.new_page()
    login = LoginPage(page)
    login.goto()
    login.login("tomsmith", "wrongpassword")
    assert "Your password is invalid!" in login.get_flash_message()
    page.close()