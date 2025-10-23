# tests/test_login.py
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.functions import login, validate_login_success

#Lee usuarios desde el JSON
with open("data/user.json") as f:
    user_json = json.load(f)
user = user_json["user"]

def test_login(driver):
    """Verifica login correcto con credenciales válidas"""
    login(driver,  user["username"], user["password"])
    validate_login_success(driver)
