from unittest import mock
import pytest
from .. import mock_data
from ... import form, utils

from kubeflow.kubeflow.crud_backend import helpers

def test_set_notebook_cpu():
    mock_notebook = helpers.load_param_yaml(
        utils.NOTEBOOK_TEMPLATE_YAML,
        name=mock_data.get_mock_body["name"],
        namespace=mock_data.NAMESPACE,
        serviceAccount="default-editor",
    )
    form.set_notebook_cpu(mock_notebook, mock_data.get_mock_body(), utils.load_spawner_ui_config())
    mock_notebook_container = mock_notebook["spec"]["template"]["spec"]["containers"][0]
    assert mock_notebook_container["resources"]["requests"]["cpu"] == mock_data.get_mock_body().get("cpu")
    assert mock_notebook_container["resources"]["limits"]["cpu"] == mock_data.get_mock_body().get("cpuLimit") #Needs to be modified to account for limit factor

def test_set_notebook_memory():
    pass