import pytest
from .. import mock_data
from ... import form, utils

def test_set_notebook_cpu():
    mock_notebook = utils.load_notebook_template()
    form.set_notebook_cpu(mock_notebook, mock_data.get_mock_body(), utils.load_spawner_ui_config())
    mock_notebook_container = mock_notebook["spec"]["template"]["spec"]["containers"][0]
    assert mock_notebook_container["resources"]["requests"]["cpu"] == mock_data.get_mock_body().get("cpu")
    assert mock_notebook_container["resources"]["limits"]["cpu"] == mock_data.get_mock_body().get("cpuLimit") #Needs to be modified to account for limit factor

def test_set_notebook_memory():
    pass