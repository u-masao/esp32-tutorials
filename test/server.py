import sys
import urllib.request

import pytest  # noqa: F401




def test_flask_simple():
    
    data = urllib.parse.urlencode({"Name": "1234"}).encode("utf-8")
    request = urllib.request.Request("http://localhost:8000/", data)
    response = urllib.request.urlopen(request)
    assert response.getcode() == 200
    assert response.read().decode("utf-8") == "hello"
