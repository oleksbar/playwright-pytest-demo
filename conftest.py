import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default="10000", help="Default timeout for Playwright actions")

@pytest.fixture(scope="session")
def browser(request):
    timeout = int(request.config.getoption("--timeout"))
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.set_default_timeout(timeout)
        context.set_default_navigation_timeout(timeout * 2)
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()