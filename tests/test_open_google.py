def test_open_google(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    page.close()

def test_google_search(page):
    page.goto("https://www.google.com")
    page.locator("textarea[name='q']").click()
    page.locator("textarea[name='q']").fill("Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_selector("text=playwright.dev")
    assert "Playwright" in page.content()
    page.close()