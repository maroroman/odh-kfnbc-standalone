#import pytest
#from .. import mock_data

# def test_app(client):
#     response = client.get("/", headers={"kubeflow-userid": "mroman"})
#     assert response.status_code == 200

# def test_set_notebook_cpu_valid():
#     mock_notebook = mock_data.get_mock_notebook()
#     form.set_notebook_cpu(mock_notebook, mock_data.get_mock_body(), utils.load_spawner_ui_config())
#     mock_notebook_container = mock_notebook["spec"]["template"]["spec"]["containers"][0]
#     assert mock_notebook_container["resources"]["requests"]["cpu"] == mock_data.get_mock_body().get("cpu")
#     assert mock_notebook_container["resources"]["limits"]["cpu"] == mock_data.get_mock_body().get("cpuLimit") #Needs to be modified to account for limit factor

# def test_set_notebook_cpu_limit_factor():
#     pass

# def test_set_notebook_cpu_invalid():
#     pass

# def test_set_notebook_memory_valid():
#     mock_notebook = mock_data.get_mock_notebook()
#     form.set_notebook_gpus(mock_notebook, mock_data.get_mock_body(), utils.load_spawner_ui_config())
#     mock_notebook_container = mock_notebook["spec"]["template"]["spec"]["containers"][0]
#     assert mock_notebook_container["resources"]["requests"]["memory"] == mock_data.get_mock_body().get("memory")
#     assert mock_notebook_container["resources"]["limits"]["memory"] == mock_data.get_mock_body().get("memoryLimit")

# def test_set_notebook_tolerations():
#     pass