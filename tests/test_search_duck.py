def test_search_duck(page):
    page.goto("https://duckduckgo.com")
    page.fill("input[name='q']", "Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_selector("article")
    page.click("[data-testid='result-title-a']")
    assert "Playwright" in page.content()
    page.wait_for_timeout(1000)
    page.close()