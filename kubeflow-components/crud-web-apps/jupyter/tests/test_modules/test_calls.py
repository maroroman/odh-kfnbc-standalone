from cgitb import reset
from email import header
from unittest import mock
from urllib import response
from pytest import fixture
import requests
import time
import json
from .. import mock_data

ADDRESS = "http://0.0.0.0:5000"

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
    response = requests.get(ADDRESS + "/api/config", headers=get_headers)
    assert response is not None
    assert response.status_code == 200, response
    assert response.json() == mock_data.get_mock_data("/mock_config.json")
    
def test_get_gpu(get_headers):
    response = requests.get(ADDRESS + "/api/gpus", headers=get_headers)
    assert response is not None
    assert response.status_code == 200, response
    assert response.json() == mock_data.get_mock_data("/mock_gpu.json")

def test_get_poddefaults(get_headers):
    response = requests.get(ADDRESS + "/api/namespaces/kubeflow-user/poddefaults", headers=get_headers)
    assert response is not None
    assert response.status_code == 200, response

def test_get_pvcs(get_headers):
    response = requests.get(ADDRESS + "/api/namespaces/kubeflow-user/pvcs", headers=get_headers)
    assert response is not None
    assert response.status_code == 200, response
    assert response.json() == mock_data.get_mock_data("/mock_pvcs.json")

def test_get_notebooks(get_headers):
    response = requests.get(ADDRESS + "/api/namespaces/kubeflow-user/notebooks",headers=get_headers)
    assert response is not None
    assert response.status_code == 200, response
    assert response.json() == mock_data.get_mock_data("/mock_notebooks.json")

def test_start_stop_notebook(get_headers):
    stop_response = requests.patch(ADDRESS + "/api/namespaces/kubeflow-user/notebooks", headers=get_headers, data={"stopped":"true"})
    assert stop_response.status_code == 200, stop_response.json()
    start_response = requests.patch(ADDRESS + "/api/namespaces/kubeflow-user/notebooks", headers=get_headers, data={"stopped":"false"})
    assert start_response.status_code == 200, stop_response.json()