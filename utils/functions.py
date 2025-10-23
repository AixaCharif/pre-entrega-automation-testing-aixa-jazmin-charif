# utils/functions.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

def login(driver, username, password):
    """Realiza el login con esperas explícitas"""
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    user_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    pass_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    user_field.send_keys(username)
    pass_field.send_keys(password)
    login_button.click()

def validate_login_success(driver):
    """Valida que el login fue exitoso"""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    title_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    assert "Products" in title_element.text, "El texto 'Products' no se encontró en la página"
    assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
