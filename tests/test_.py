import pytest
import requests
import ssl
import os

def test_server_has_endpoint():
    context = ssl._create_unverified_context()
    endpoint_url = 'http://127.0.0.1:5000/'

    with pytest.raises(requests.HTTPError):
        response = requests.get(endpoint_url, verify=False)
        response.raise_for_status()



def test_file_structure():
    assert "application" in os.listdir(os.curdir)
    assert "docs" in os.listdir(os.curdir)
    assert "tests" in os.listdir(os.curdir)
    assert "__init__.py" in os.listdir(os.curdir+"/application")
    assert "app.py" in os.listdir(os.curdir+"/application")
    assert "func.py" in os.listdir(os.curdir+"/application")
    assert "form.html" in os.listdir(os.curdir+"/application"+"/templates")
    assert "index.html" in os.listdir(os.curdir+"/application"+"/templates")
    assert "layout.html" in os.listdir(os.curdir+"/application"+"/templates")


