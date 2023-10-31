from flask import Flask
import pytest
import requests
import ssl
import os
from requests.exceptions import ConnectionError
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from application.app import app

def test_Is_online_index():
    '''Här görs en request.get fär att kolla om våran endpoint är funktionell'''
    assert requests.get("http://127.0.0.1:5000", timeout=10)

def test_url_up_and_running():
    '''Här skriver vi ett test för att simulera en request till Flask applikationen utan att köra servern, detta görs genom att använda Flask 'test_client' '''
    with app.test_client() as client:
        try:
            response = client.get('/')
            assert response.status_code == 200
        except ConnectionError:
            pytest.fail("Failed to connect to the URL")

def test_file_structure():
    '''Denna test_case kollar filstrukturer och kollar om den stämmer'''
    assert "application" in os.listdir(os.curdir)
    assert "docs" in os.listdir(os.curdir)
    assert "tests" in os.listdir(os.curdir)
    assert "__init__.py" in os.listdir(os.curdir+"/application")
    assert "app.py" in os.listdir(os.curdir+"/application")
    assert "func.py" in os.listdir(os.curdir+"/application")
    assert "form.html" in os.listdir(os.curdir+"/application"+"/templates")
    assert "index.html" in os.listdir(os.curdir+"/application"+"/templates")
    assert "layout.html" in os.listdir(os.curdir+"/application"+"/templates")