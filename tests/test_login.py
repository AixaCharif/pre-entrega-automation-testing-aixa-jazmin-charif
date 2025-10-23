# tests/test_login.py
import json
from utils.functions import login, validate_login_success

#Lee usuarios desde el JSON
with open("data/user.json") as f:
    user_json = json.load(f)
user = user_json["user"]

def test_login(driver):
    """Verifica login correcto con credenciales válidas"""
    login(driver,  user["username"], user["password"])
    validate_login_success(driver)
