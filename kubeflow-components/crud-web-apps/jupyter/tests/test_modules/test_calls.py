from cgitb import reset
from email import header
from pytest import fixture
import requests
import time

@fixture
def get_headers():
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    return headers

def teardown_function(function):   # the function parameter is optional
    time.sleep(3)


def test_get_config(get_headers):
    response = requests.get("http://0.0.0.0:5000/api/config", headers=get_headers)
    assert response is not None
    assert response.status_code not in [404, 403, 401], response
    body = response.content
    assert response.content == mock_config
def test_get_gpu(get_headers):
    response = requests.get("http://0.0.0.0:5000/api/gpus", headers=get_headers)
    assert response is not None
    assert response.status_code not in [404, 403, 401], response
def test_get_poddefaults(get_headers):
    response = requests.get("http://0.0.0.0:5000/api/namespaces/kubeflow-user/poddefaults", headers=get_headers)
    assert response is not None
    assert response.status_code not in [404, 403, 401], response
def test_get_pvcs(get_headers):
    response = requests.get("http://0.0.0.0:5000/api/namespaces/kubeflow-user/pvcs", headers=get_headers)
    assert response is not None
    assert response.status_code not in [404, 403, 401], response
def test_get_notebooks(get_headers):
    response = requests.get("http://0.0.0.0:5000/api/namespaces/kubeflow-user/notebooks",headers=get_headers)
    assert response is not None
    assert response.status_code not in [404, 403, 401], response