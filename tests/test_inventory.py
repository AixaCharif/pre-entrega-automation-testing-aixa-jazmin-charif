#tests/test_inventory.py
import pytest
from selenium.webdriver.common.by import By
from utils.functions import login
import json

#Lee usuario desde JSON
with open("data/user.json") as f:
    user_json = json.load(f)
user = user_json["user"]


@pytest.fixture
def login_driver(driver):
    """Login y retorna el driver en la página de inventario"""
    login(driver, user["username"], user["password"])
    return driver


def test_inventory_navigation(login_driver):
    """Verifica navegación y elementos del catálogo"""
    driver = login_driver

    #Título
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", "El título de la página de inventario es incorrecto"

    #Verifica al menos un producto
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No se encontraron productos en la página"

    #Nombre y precio del primer producto
    first_product = products[0]
    name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {name} - Precio: {price}")

    #Valida menú/filtros
    filter_button = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_button.is_displayed(), "El filtro de productos no se muestra"


def test_add_to_cart(login_driver):
    """Verifica interacción con productos y carrito"""
    driver = login_driver

    #Primer producto y botón "Add to cart"
    first_product = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    first_product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    add_button = first_product.find_element(By.TAG_NAME, "button")
    add_button.click()

    #Verifica contador del carrito
    cart_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_counter == "1", "El contador del carrito no se actualizó"

    # Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Verifica producto en carrito
    cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
    name_in_cart = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert name_in_cart == first_product_name, "El producto en el carrito no coincide"
