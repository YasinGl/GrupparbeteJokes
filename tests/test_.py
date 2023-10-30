import os

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