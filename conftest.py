import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Launch the browser once per test session."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_default_timeout(10000)
    context.set_default_navigation_timeout(15000)
    yield browser
    context.close()
    browser.close()
    playwright.stop()