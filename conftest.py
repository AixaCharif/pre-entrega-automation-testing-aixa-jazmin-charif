# conftest.py
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Configura y cierra el navegador para cada test"""
    options = Options()
    #options.add_argument("--headless")  #navegador oculto
    options.add_argument("--window-size=1920,1080")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Screenshots automáticas si el test falla"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"reports/screenshots/{item.name}_{timestamp}.png"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            driver.save_screenshot(filename)
            print(f"\n📸 Captura guardada: {filename}")
